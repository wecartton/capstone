import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import LoginForm from '../components/LoginForm';
import logo from '../assets/ellc-logo.png';
import '../styles/LoginPage.css';

const LoginPage = () => {
  const { isAuthenticated } = useAuth();

  // Redirect if already authenticated
  if (isAuthenticated) {
    return <Navigate to="/dashboard" />;
  }

  return (
    <div className="login-page">
      <div className="login-container">
        <div className="login-left">
          {/* This is where we'd put the background image with equipment */}
        </div>
        <div className="login-right">
          <div className="login-content">
            <h1>Hi, Welcome to PresUniv ELLC Systems</h1>
            <p>Enter your details to log in your account</p>
            <div className="logo-container">
              <img src={logo} alt="ELLC Logo" className="logo" />
            </div>
            <LoginForm />
            <p className="cookies-notice">Cookies notice!</p>
            <p className="copyright">2023 © CAPSTONE Design Project. All Rights Reserved.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;









