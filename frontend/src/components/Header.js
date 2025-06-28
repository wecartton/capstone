import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import logo from '../assets/ellc-logo.png';
import '../styles/Header.css';

const Header = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
  };

  return (
    <header className="header">
      <div className="header-content">
        <div className="logo-container">
          <img src={logo} alt="ELLC Logo" className="logo" />
          <h1>Dashboard</h1>
        </div>
        <button className="logout-button" onClick={handleLogout}>
          Logout Here!
        </button>
      </div>
    </header>
  );
};

export default Header;