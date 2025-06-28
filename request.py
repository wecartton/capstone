import requests

api_key = "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"  # contoh: sk-ABC123...

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Apa itu API?"}
    ]
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=data
)

print(response.json())
