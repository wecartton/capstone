import React from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import Navigation from './Navigation';
import '../styles/ResultPage.css';

const ResultPage = () => {
  const { level } = useParams();
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state?.result;

  // Redirect to main page if no result data
  if (!result) {
    navigate('/quiz'); // Changed from '/' to '/quiz'
    return null;
  }

  const { correct, total, percentage, passed } = result;

  // Get feedback based on percentage
  const getFeedback = () => {
    if (percentage >= 80) {
      return "Excellent! You have a great understanding of English grammar.";
    } else if (percentage >= 70) {
      return "Good job! You have a solid grasp of English grammar concepts.";
    } else if (percentage >= 60) {
      return "Not bad! You have a basic understanding of English grammar.";
    } else {
      return "Keep practicing! You'll improve with more study and practice.";
    }
  };

  // Get badge based on performance
  const getBadgeClass = () => {
    if (percentage >= 80) {
      return "badge excellent";
    } else if (percentage >= 70) {
      return "badge good";
    } else if (percentage >= 60) {
      return "badge satisfactory";
    } else {
      return "badge needs-improvement";
    }
  };

  // Get badge text
  const getBadgeText = () => {
    if (percentage >= 80) {
      return "Excellent";
    } else if (percentage >= 70) {
      return "Good";
    } else if (percentage >= 60) {
      return "Satisfactory";
    } else {
      return "Needs Improvement";
    }
  };

  // Next steps text based on result
  const getNextSteps = () => {
    if (passed) {
      const nextLevel = parseInt(level) + 1;
      if (nextLevel <= 5) {
        return `You've unlocked Level ${nextLevel}! Continue your journey to improve your English grammar skills.`;
      } else {
        return "Congratulations! You've completed all levels. You have an excellent grasp of English grammar!";
      }
    } else {
      return "You need to score higher to unlock the next level. Try again to improve your score.";
    }
  };

  return (
    <div className="result-page-wrapper">
      <Navigation />
      <div className="result-page">
        <div className="result-content">
          {/* Level Star */}
          <div className="level-star-result">
            <div className="star-shape-result">
              <img 
                src={passed ? "/images/star-completed.png" : "/images/star-unlocked.png"}
                alt={`Level ${level} star`}
                className="star-image-result"
              />
              <div className="star-level-result">LV {level}</div>
            </div>
          </div>
          
          {/* Badge */}
          <div className={getBadgeClass()}>
            {getBadgeText()}
          </div>
          
          {/* Score Container */}
          <div className="score-container">
            <div className="score-circle">
              <div className="score-percentage">{Math.round(percentage)}%</div>
              <div className="score-text">{correct} / {total}</div>
            </div>
          </div>
          
          {/* Result Status */}
          <div className="result-status">
            {passed ? (
              <div className="passed">You passed this level!</div>
            ) : (
              <div className="failed">You didn't pass this level yet.</div>
            )}
          </div>
          
          {/* Feedback */}
          <p className="feedback">{getFeedback()}</p>
          
          {/* Next Steps */}
          <p className="next-steps">{getNextSteps()}</p>
          
          {/* Buttons */}
          <div className="buttons">
            <button 
              className="result-button try-again"
              onClick={() => navigate(`/quiz/${level}`)}
            >
              Try Again
            </button>
            <button 
              className="result-button back-to-levels"
              onClick={() => navigate('/quiz')}
            >
              Back to Levels
            </button>
            {passed && parseInt(level) < 5 && (
              <button 
                className="result-button next-level-button"
                onClick={() => navigate(`/quiz/${parseInt(level) + 1}`)}
              >
                Go to Level {parseInt(level) + 1}
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultPage;