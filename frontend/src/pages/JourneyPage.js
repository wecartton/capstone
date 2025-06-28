import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from '../components/Header';
import { useAuth } from '../context/AuthContext';
import apiService from '../services/api.service';
import '../styles/JourneyPage.css';

const JourneyPage = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [quizSessions, setQuizSessions] = useState([]);
  const [conversations, setConversations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is authenticated
    if (!user) {
      navigate('/login');
      return;
    }
    
    fetchJourneyData();
  }, [user, navigate]);

  const fetchJourneyData = async () => {
    try {
      setLoading(true);
      
      // For now, we'll use placeholder data since the backend is under maintenance
      // In the future, this would fetch real data from the API
      
      // Placeholder quiz sessions
      const placeholderQuizSessions = [
        { id: 1, level: 1, date: '2024-01-15', score: 85, status: 'Passed' },
        { id: 2, level: 2, date: '2024-01-18', score: 90, status: 'Passed' },
        { id: 3, level: 3, date: '2024-01-22', score: 78, status: 'Failed' },
      ];
      
      // Placeholder conversation sessions
      const placeholderConversations = [
        { id: 1, date: '2024-01-14', corrected_by_agent: 'She goes to school every day', user_input: 'She go to school everyday' },
        { id: 2, date: '2024-01-17', corrected_by_agent: 'He doesn’t like coffee', user_input: 'He don’t like coffee' },
        { id: 3, date: '2024-01-21', corrected_by_agent: 'I can play guitar', user_input: 'I can plays guitar' },
      ];
      
      setQuizSessions(placeholderQuizSessions);
      setConversations(placeholderConversations);
      
      // When the backend is ready, replace above with:
      // const response = await apiService.get('/api/dashboard/journey');
      // setQuizSessions(response.data.quizSessions || []);
      // setConversations(response.data.conversations || []);
      
    } catch (error) {
      console.error('Error fetching journey data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="journey-page">
      <Header />
      <div className="journey-container">
        <div className="journey-header">
          <h1>Track Your Journey Here!</h1>
          <p>Let's see how far your activities with us, {user?.username || 'User'}!</p>
        </div>
        
        <div className="journey-content">
          {/* Quiz Sessions Section */}
          <div className="journey-section">
            <h2 className="section-title">List Quiz Session</h2>
            <div className="section-content">
              {loading ? (
                <>
                  <div className="placeholder-item"></div>
                  <div className="placeholder-item"></div>
                  <div className="placeholder-item"></div>
                </>
              ) : quizSessions.length > 0 ? (
                <div className="sessions-list">
                  {quizSessions.map((session) => (
                    <div key={session.id} className="session-item">
                      <div className="session-info">
                        <span className="session-level">Level {session.level}</span>
                        <span className="session-date">{new Date(session.date).toLocaleDateString()}</span>
                      </div>
                      <div className="session-details">
                        <span className="session-score">Score: {session.score}%</span>
                        <span className={`session-status ${session.status.toLowerCase().replace(' ', '-')}`}>
                          {session.status}
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="empty-state">
                  <p>No quiz sessions yet</p>
                  <button onClick={() => navigate('/quiz')} className="start-button">
                    Start Your First Quiz
                  </button>
                </div>
              )}
            </div>
          </div>
          
          {/* Conversation Agent Section */}
          <div className="journey-section">
            <h2 className="section-title">List Conversation Agent</h2>
            <div className="section-content">
              {loading ? (
                <>
                  <div className="placeholder-item"></div>
                  <div className="placeholder-item"></div>
                  <div className="placeholder-item"></div>
                </>
              ) : conversations.length > 0 ? (
                <div className="sessions-list">
                  {conversations.map((conversation) => (
                    <div key={conversation.id} className="session-item">
                      <div className="session-info">
                        <span className="session-topic">{conversation.user_input}</span>
                        <span className="session-date">{new Date(conversation.date).toLocaleDateString()}</span>
                      </div>
                      <div className="session-details">
                        <span className="session-duration">Corrected by Agent: {conversation.corrected_by_agent}</span>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="empty-state">
                  <p>No conversations yet</p>
                  <button onClick={() => navigate('/talk-with-agent')} className="start-button">
                    Start Talking with Agent
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default JourneyPage;