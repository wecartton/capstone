import React from 'react';
import { useAuth } from '../context/AuthContext';
import Header from '../components/Header';
import DashboardCard from '../components/DashboardCard';
import '../styles/DashboardPage.css';

const DashboardPage = () => {
  const { user } = useAuth();

  return (
    <div className="dashboard-page">
      <Header />
      <div className="dashboard-content">
        <h1>English Learning and Literacy Center</h1>
        <p>Have a great day, {user ? user.username : 'User'}!</p>
        
        <div className="dashboard-cards">
          <DashboardCard 
            title="Talk with AI Agent" 
            description="Engage in interactive conversations with our intelligent AI assistant. Get personalized help, ask questions, and receive instant feedback on your learning progress. Whether you need clarification on concepts or want to practice discussions, our AI agent is available 24/7 to support your educational journey." 
            linkTo="/talk-with-agent" 
          />
          <DashboardCard 
            title="Quiz Exercise" 
            description="Test your knowledge with interactive quizzes designed to reinforce your learning. Choose from various question types including multiple choice, true/false, and short answers. Track your scores, identify areas for improvement, and challenge yourself with progressively difficult questions tailored to your skill level." 
            linkTo="/quiz" 
          />
          <DashboardCard 
            title="Track Journey" 
            description="Monitor your learning progress with detailed analytics and visual progress tracking. View completed lessons, time spent studying, achievement badges, and performance trends. Set personal goals, celebrate milestones, and stay motivated as you advance through your educational path." 
            linkTo="/journey" 
          />
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;