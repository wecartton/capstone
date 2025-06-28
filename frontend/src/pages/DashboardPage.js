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
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lorem magna, maximus a sagittis id, interdum hendrerit nulla." 
            linkTo="/talk-with-agent" 
          />
          <DashboardCard 
            title="Quiz Exercise" 
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lorem magna, maximus a sagittis id, interdum hendrerit nulla." 
            linkTo="/quiz" 
          />
          <DashboardCard 
            title="Track Journey" 
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lorem magna, maximus a sagittis id, interdum hendrerit nulla." 
            linkTo="/journey" 
          />
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;