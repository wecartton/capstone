import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Star.css';

const Star = ({ level, unlocked, completed }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    if (unlocked) {
      navigate(`/quiz/${level}`);
    }
  };

  // Tentukan gambar berdasarkan status
  const getStarImage = () => {
    if (completed) {
      return '/images/star-completed.png';
    } else if (unlocked) {
      return '/images/star-unlocked.png';
    } else {
      return '/images/star-locked.png';
    }
  };

  const getStarClass = () => {
    if (completed) return 'star-image completed';
    if (unlocked) return 'star-image unlocked';
    return 'star-image locked';
  };

  return (
    <div className="star-container">
      <div 
        className={getStarClass()} 
        onClick={handleClick}
        title={unlocked ? `Level ${level}` : `Complete previous level to unlock`}
      >
        <img 
          src={getStarImage()}
          alt={`Level ${level} star`}
          className="star-image-file"
        />
        <div className="star-level">{level}</div>
      </div>
      <div className="star-label">
        {unlocked ? (
          completed ? 'Completed' : 'Level ' + level
        ) : (
          'Locked'
        )}
      </div>
    </div>
  );
};

export default Star;