import React, { useState, useEffect, useRef } from 'react';
import '../styles/AgentChat.css';

const AgentChat = () => {
  // States
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [showGif, setShowGif] = useState(false);
  const [aiResponse, setAiResponse] = useState('');
  const [grammarCorrection, setGrammarCorrection] = useState(null);

  // Voice recognition states
  const [transcript, setTranscript] = useState('');
  const [isListening, setIsListening] = useState(false);
  const recognition = useRef(null);

  // WebSocket reference
  const ws = useRef(null);

  // Setup SpeechRecognition
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert('Browser kamu tidak mendukung Speech Recognition!');
      return;
    }
    recognition.current = new SpeechRecognition();
    recognition.current.continuous = true;
    recognition.current.interimResults = true;
    recognition.current.lang = 'en-US';

    recognition.current.onresult = (event) => {
      let interimTranscript = '';
      let finalTranscript = '';
      for (let i = event.resultIndex; i < event.results.length; i++) {
        const textChunk = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          finalTranscript += textChunk;
        } else {
          interimTranscript += textChunk;
        }
      }
      setTranscript(finalTranscript + interimTranscript);
    };

    recognition.current.onerror = (event) => {
      console.error('Speech recognition error:', event.error);
      setIsListening(false);
    };

    recognition.current.onend = () => {
      setIsListening(false);
    };
  }, []);

  // Setup WebSocket connection
  useEffect(() => {
  ws.current = new WebSocket('ws://localhost:8090');

  ws.current.onopen = () => {
    console.log('WebSocket connected');
  };

  ws.current.onmessage = (event) => {
  try {
    const data = JSON.parse(event.data); // coba parse sebagai JSON

    if (data.type === 'grammar_correction') {
      setGrammarCorrection(data.text);
    } else {
      // fallback untuk text biasa dari AI
      setAiResponse(prev => prev + (data.text || ''));
    }

  } catch (e) {
    // fallback untuk non-JSON (AI response string langsung dari stream)
    if (event.data === '[END]') {
      setShowGif(false);
    } else {
      setAiResponse(prev => prev + event.data);
    }
  }
};


  ws.current.onerror = (error) => {
    console.error('WebSocket error:', error);
    setShowGif(false);
  };

  ws.current.onclose = () => {
    console.log('WebSocket disconnected');
  };

  // Cleanup on unmount
  return () => {
    ws.current.close();
  };
}, []);


  // Send message to backend and update UI
  const sendMessage = (message) => {
  if (!message.trim()) return;

  // Save user message in chat history
  setMessages(prev => [...prev, { text: message.trim(), isUser: true }]);
  
  setGrammarCorrection(null); // Reset grammar correction setiap kirim pesan baru
  setAiResponse('');          // Reset AI response
  setShowGif(true);           // Show loading GIF

  if (ws.current.readyState === WebSocket.OPEN) {
    ws.current.send(message.trim());
  } else {
    console.error('WebSocket belum connected');
    setShowGif(false);
    setAiResponse('Error: Unable to connect to the server.');
  }
};


  // Toggle voice recognition & send transcript when stopped
  const toggleListening = () => {
    if (isListening) {
      recognition.current.stop();
      setIsListening(false);

      if (transcript.trim()) {
        sendMessage(transcript);
      }
    } else {
      setTranscript('');
      recognition.current.start();
      setIsListening(true);
    }
  };

  // Handle input text send
  const handleSendMessage = (e) => {
    e.preventDefault();
    if (input.trim() === '') return;

    sendMessage(input);
    setInput('');
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  return (
    <div className="agent-chat-container">

      {/* Chat messages GIF + AI response */}
      <div className="chat-messages" style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
        {showGif ? (
          <>
            <img
              src="/voice_chatbot_talking_sharpened_fixed.gif"
              alt="Chatbot Talking"
              className="chatbot-gif"
              style={{ width: '500px', height: '300px' }}
            />
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {/* Show grammar correction first */}
              {grammarCorrection && (
              <div className="grammar-correction" style={{ color: 'orange', fontStyle: 'italic' }}>
                Grammar correction: {grammarCorrection}
              </div>
            )}

              {/* Then AI response streaming */}
              <p className="chat-response-text" style={{ margin: 0 }}>{aiResponse}</p>
            </div>
          </>
        ) : (
          <>
            <img
              src="/assistant_idle.png"
              alt="AI Agent Idle"
              className="chatbot-gif"
              style={{ width: '500px', height: '300px' }}
            />
            {aiResponse && (
              <div style={{ marginTop: '10px' }}>
                {grammarCorrection && (
                  <div className="grammar-correction" style={{ color: 'orange', fontStyle: 'italic' }}>
                    Grammar correction: {grammarCorrection}
                  </div>
                )}
                <p className="chat-response-text" style={{ margin: 0 }}>{aiResponse}</p>
              </div>
            )}
          </>
        )}
      </div>

      {/* Input ketikan */}
      <div className="chat-input-area">
        <form onSubmit={handleSendMessage}>
          <input
            type="text"
            value={input}
            onChange={handleInputChange}
            placeholder="Type your message here..."
          />
          <button type="submit">Send</button>
        </form>
      </div>

      {/* Voice recognition realtime output */}
      <div className="voice-recognition-section" style={{ marginTop: '20px' }}>
        <p style={{ whiteSpace: 'pre-wrap' }}>
          {transcript || "This section and text will be shown result of user voice recognition"}
        </p>
        <button onClick={toggleListening} className="voice-button">
          {isListening ? 'Stop Recording' : 'Start Recording'}
        </button>
      </div>

      {/* Chat history (optional) */}
      <div className="chat-history" style={{ marginTop: '30px' }}>
        <h3>Chat History</h3>
        {messages.length === 0 && <p>No messages yet.</p>}
        <ul>
          {messages.map((msg, idx) => (
            <li key={idx} style={{ fontWeight: msg.isUser ? 'bold' : 'normal' }}>
              {msg.isUser ? "User:" : "AI:"} {msg.text}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AgentChat;