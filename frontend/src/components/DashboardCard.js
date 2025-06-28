import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/DashboardCard.css';

const DashboardCard = ({ title, description, linkTo }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(linkTo);
  };

  return (
    <div className="dashboard-card" onClick={handleClick}>
      <div className="card-content">
        <h2>{title}</h2>
        <p>{description}</p>
      </div>
    </div>
  );
};

export default DashboardCard;