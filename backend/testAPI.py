import asyncio
import websockets
import os
import openai
from dotenv import load_dotenv
import language_tool_python
import json
from dbAIAgent_Handler import store_to_database

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize grammar checker
tool = language_tool_python.LanguageTool('en-US')

def correct_grammar_manual(text):
    matches = tool.check(text)
    corrected_text = tool.correct(text)

    grammar_issues = [
        {
            "message": match.message,
            "context": match.context,
            "offset": match.offset,
            "length": match.errorLength,
            "replacements": match.replacements
        }
        for match in matches
    ]

    # Hanya kembalikan hasil jika memang berbeda
    if corrected_text != text:
        return corrected_text, grammar_issues
    return None, []


async def handle_message(message, websocket):
    try:
        print("[WebSocket] Received message:", message)

        # Grammar correction
        corrected, issues = correct_grammar_manual(message)
        prompt_to_ask = corrected if corrected else message

        # Hanya kirim grammar correction jika ada kesalahan grammar
        if corrected:
            correction_msg = json.dumps({
                "type": "grammar_correction",
                "text": corrected,
                "issues": issues
            })
            await websocket.send(correction_msg)
            store_to_database(message, corrected)
        print("[Handle Message] Used Prompt:", prompt_to_ask)

        # Intent Greeting Detection (case-insensitive + fleksibel)
        greeting_keywords = [
            "hi", "hai", "hello", "hello there", "how are you", "who are you"
        ]
        lower_prompt = prompt_to_ask.strip().lower()

        if any(greet in lower_prompt for greet in greeting_keywords):
            greeting = "Hi! I am ELLC Agent, I am ready to become your assistant here."
            await websocket.send(greeting)
            await websocket.send("[END]")
            print("[Handle Message] Assistant Response:", greeting)
            return

        # Generate OpenAI response if bukan greeting
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are ELLC Agent, a smart and friendly assistant. "
                        "Only greet the user if their message is a greeting. Otherwise, just answer normally."
                    )
                },
                {"role": "user", "content": prompt_to_ask}
            ],
            stream=True
        )

        assistant_response = ""

        async for chunk in response:
            delta = chunk.choices[0].delta.get("content")
            if delta:
                assistant_response += delta
                await websocket.send(delta)

        await websocket.send("[END]")
        print("[Handle Message] Assistant Response:", assistant_response)

    except Exception as e:
        await websocket.send("Failed to connect with OpenAI")
        print("[Handle Message] Error:", e)


async def echo(websocket):
    try:
        async for message in websocket:
            await handle_message(message, websocket)
    except websockets.exceptions.ConnectionClosed:
        print("[WebSocket] Client disconnected")
    except Exception as e:
        print("[WebSocket] Error:", e)


async def main():
    port = int(os.environ.get("PORT", 8090))
    print(f"[Server] WebSocket server starting on port {port}...")
    async with websockets.serve(echo, "0.0.0.0", port):
        print(f"[Server] WebSocket server running on port {port}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
