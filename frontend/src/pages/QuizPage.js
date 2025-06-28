import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import Navigation from './Navigation';
import '../styles/QuizPage.css';

const QuizPage = () => {
  const { level } = useParams();
  const navigate = useNavigate();
  
  const [questions, setQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [timeLeft, setTimeLeft] = useState(null);
  const [questionProgress, setQuestionProgress] = useState({
      current: 1,
      total: 0
  });

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const token = localStorage.getItem('accessToken');
        const config = token ? {
          headers: { Authorization: `Bearer ${token}` }
        } : {};

        console.log('Fetching quiz for level:', level);
        console.log('Using token:', token ? 'Yes' : 'No');

        const response = await axios.get(`/api/quiz/${level}`, config);
        console.log('Quiz response:', response.data);
        
        const { questions: quizQuestions, total_questions } = response.data;

        setQuestions(quizQuestions);
        setQuestionProgress({
            current: 1,
            total: quizQuestions.length // Use actual length from response
        });
            
        const totalTime = quizQuestions.length * 30; // 30 seconds per question
        setTimeLeft(totalTime);
        
        console.log(`Loaded ${quizQuestions.length} questions for level ${level}`);

        setLoading(false);
      } catch (err) {
        console.error('Error fetching quiz:', err);
        console.error('Error response:', err.response);
        
        if (err.response && err.response.status === 403) {
          setError('This level is not unlocked yet. Please complete previous levels first.');
        } else if (err.response && err.response.status === 401) {
          setError('Authentication required. Please log in again.');
          // Optionally redirect to login
          setTimeout(() => navigate('/login'), 2000);
        } else if (err.response && err.response.status === 404) {
          setError('Quiz not found. Please try again later.');
        } else {
          setError('Failed to load quiz. Please try again later.');
        }
        setLoading(false);
      }
    };

    fetchQuestions();
  }, [level, navigate]);

  // Timer countdown
  useEffect(() => {
    if (loading || timeLeft === null) return;

    const timer = setInterval(() => {
      setTimeLeft((prevTime) => {
        if (prevTime <= 1) {
          clearInterval(timer);
          handleSubmit();
          return 0;
        }
        return prevTime - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [loading, timeLeft]);

  const handleSelectAnswer = (questionId, option) => {
    setSelectedAnswers({ ...selectedAnswers, [questionId]: option });
  };

  const handleQuestionClick = (index) => {
      setCurrentQuestionIndex(index);
      setQuestionProgress(prev => ({
          ...prev,
          current: index + 1
      }));
  };

  const handleSubmit = async () => {
    // Prepare answers in the format expected by the API
    const formattedAnswers = Object.keys(selectedAnswers).map(questionId => ({
      question_id: parseInt(questionId),
      selected_option: selectedAnswers[questionId]
    }));

    console.log(`Submitting ${formattedAnswers.length} answers out of ${questions.length} questions`);

    try {
      // Get JWT token and set up axios config
      const token = localStorage.getItem('accessToken');
      const config = token ? {
        headers: { Authorization: `Bearer ${token}` }
      } : {};

      console.log('Submitting quiz answers:', formattedAnswers);

      const response = await axios.post(`/api/quiz/submit/${level}`, {
        answers: formattedAnswers
      }, config);
      
      console.log('Submit response:', response.data);
      
      // Navigate to result page with the result data
      navigate(`/result/${level}`, { state: { result: response.data } });
    } catch (err) {
      console.error('Error submitting quiz:', err);
      setError('Failed to submit quiz. Please try again.');
    }
  };

  if (loading) {
    return (
      <>
        <Navigation />
        <div className="loading">Loading quiz...</div>
      </>
    );
  }

  if (error) {
    return (
      <>
        <Navigation />
        <div className="container error-container">
          <h2>Error</h2>
          <p className="error">{error}</p>
          <button onClick={() => navigate('/quiz')}>Return to Level Selection</button>
        </div>
      </>
    );
  }

  // If no questions found
  if (questions.length === 0) {
    return (
      <>
        <Navigation />
        <div className="container">
          <h2>No questions available for this level</h2>
          <button onClick={() => navigate('/quiz')}>Return to Level Selection</button>
        </div>
      </>
    );
  }

  const currentQuestion = questions[currentQuestionIndex];

  // Format time left
  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;
  const formattedTime = `${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

  // Check if current question is answered
  const isCurrentQuestionAnswered = selectedAnswers[currentQuestion.id] !== undefined;

  return (
    <>
      <Navigation />
      <div className="quiz-page">
        <div className="quiz-container">
          {/* Left column - Question and options */}
          <div className="question-column">
            <div className="question-card">
              <h3>{currentQuestion.question}</h3>
              
              <div className="options">
                {currentQuestion.options.map((option, index) => (
                  <div 
                    key={index} 
                    className={`option ${selectedAnswers[currentQuestion.id] === option.charAt(0) ? 'selected' : ''}`}
                    onClick={() => handleSelectAnswer(currentQuestion.id, option.charAt(0))}
                  >
                    <span className="option-circle"></span>
                    {option}
                  </div>
                ))}
              </div>
            </div>
            
            <div className="navigation-buttons">
              <button 
                onClick={() => setCurrentQuestionIndex(Math.max(0, currentQuestionIndex - 1))}
                disabled={currentQuestionIndex === 0}
                className="nav-button"
              >
                Previous
              </button>
              
              <button 
                onClick={() => setCurrentQuestionIndex(Math.min(questions.length - 1, currentQuestionIndex + 1))}
                disabled={currentQuestionIndex === questions.length - 1}
                className="nav-button"
              >
                Next
              </button>
            </div>
          </div>

          {/* Right column - Level star, timer, question grid, submit */}
          <div className="sidebar">
            {/* Level star with timer */}
            <div className="level-star">
              <div className="star-container">
                <div className="star-shape">
                  <span className="level-text">LV{level}</span>
                </div>
              </div>
              <div className="timer">{formattedTime}</div>
            </div>

            <div className="question-progress">
                <span>Question {questionProgress.current} of {questionProgress.total}</span>
                <div className="progress-bar">
                    <div 
                        className="progress-fill" 
                        style={{
                            width: `${(questionProgress.current / questionProgress.total) * 100}%`
                        }}
                    />
                </div>
            </div>

            {/* Question grid */}
            <div className="question-grid">
              {questions.map((_, index) => (
                <div
                  key={index}
                  className={`question-number ${
                    index === currentQuestionIndex ? 'current' : ''
                  } ${
                    selectedAnswers[questions[index].id] !== undefined ? 'answered' : ''
                  }`}
                  onClick={() => handleQuestionClick(index)}
                >
                  {index + 1}
                </div>
              ))}
            </div>

            {/* Submit button */}
            <button 
              className="submit-button"
              onClick={handleSubmit}
            >
              Submit
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default QuizPage;