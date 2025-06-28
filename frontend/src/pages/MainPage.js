import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Navigation from './Navigation';
import Star from './Star';
import '../styles/MainPage.css';

const MainPage = () => {
  const [levels, setLevels] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLevels = async () => {
      try {
        // Use the correct endpoint with JWT authentication
        const token = localStorage.getItem('accessToken');
        const config = token ? {
          headers: { Authorization: `Bearer ${token}` }
        } : {};
        
        const response = await axios.get('/api/quiz/levels', config);
        setLevels(response.data.levels);
        setLoading(false);
        
        console.log('Levels loaded:', response.data.levels);
      } catch (err) {
        setError('Failed to load levels. Please try again later.');
        setLoading(false);
        console.error('Error fetching levels:', err);
        
        // If token expired, try to refresh or redirect to login
        if (err.response && err.response.status === 401) {
          console.log('Token expired, user might need to login again');
        }
      }
    };

    fetchLevels();
  }, []);

  if (loading) {
    return (
      <>
        <Navigation />
        <div className="loading">Loading...</div>
      </>
    );
  }

  if (error) {
    return (
      <>
        <Navigation />
        <div className="error">{error}</div>
      </>
    );
  }

  // Organize levels according to the layout: Level 5 on top, then 3-4, then 1-2
  const getStarByLevel = (levelNum) => levels.find(level => level.level === levelNum);

  return (
    <>
      <Navigation />
      <div className="main-page">
        <p className="instructions">
          Complete each level to unlock the next one. Click on a star to start the quiz for that level.
        </p>

        <div className="container">
          <div className="stars-container">
            {/* Level 5 - Top center */}
            <div className="stars-row single">
              {getStarByLevel(5) && (
                <Star
                  key={5}
                  level={5}
                  unlocked={getStarByLevel(5).unlocked}
                  completed={getStarByLevel(5).completed}
                />
              )}
            </div>
            
            {/* Level 3 and 4 - Middle row */}
            <div className="stars-row double middle-row">
              {getStarByLevel(3) && (
                <Star
                  key={3}
                  level={3}
                  unlocked={getStarByLevel(3).unlocked}
                  completed={getStarByLevel(3).completed}
                />
              )}
              {getStarByLevel(4) && (
                <Star
                  key={4}
                  level={4}
                  unlocked={getStarByLevel(4).unlocked}
                  completed={getStarByLevel(4).completed}
                />
              )}
            </div>
            
            {/* Level 1 and 2 - Bottom row */}
            <div className="stars-row double bottom-row">
              {getStarByLevel(1) && (
                <Star
                  key={1}
                  level={1}
                  unlocked={getStarByLevel(1).unlocked}
                  completed={getStarByLevel(1).completed}
                />
              )}
              {getStarByLevel(2) && (
                <Star
                  key={2}
                  level={2}
                  unlocked={getStarByLevel(2).unlocked}
                  completed={getStarByLevel(2).completed}
                />
              )}
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default MainPage;