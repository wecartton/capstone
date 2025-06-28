import React from 'react';
import Header from '../components/Header';
import AgentChat from '../components/AgentChat';
import '../styles/TalkWithAgentPage.css';

const TalkWithAgentPage = () => {
  return (
    <div className="talk-with-agent-page">
      <Header />
      <div className="agent-content">
        <h1>AI Agent ELLC</h1>
        <p>
          Hi, now you can talk to AI Agent, tap the start button to start a conversation,
          just ask what you want to know...
        </p>
        <AgentChat />
      </div>
    </div>
  );
};

export default TalkWithAgentPage;
