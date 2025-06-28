import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import RegisterForm from '../components/RegisterForm';
import logo from '../assets/ellc-logo.png';
import '../styles/RegisterPage.css';

const RegisterPage = () => {
  const { isAuthenticated } = useAuth();

  // Redirect if already authenticated
  if (isAuthenticated) {
    return <Navigate to="/dashboard" />;
  }

  return (
    <div className="register-page">
      <div className="register-container">
        <div className="register-left">
          {/* This is where we'd put the background image with equipment */}
        </div>
        <div className="register-right">
          <div className="register-content">
            <h1>Create an ELLC Account</h1>
            <p>Enter your details to create your account</p>
            <div className="logo-container">
              <img src={logo} alt="ELLC Logo" className="logo" />
            </div>
            <RegisterForm />
            <p className="cookies-notice">Cookies notice!</p>
            <p className="copyright">2023 © CAPSTONE Design Project. All Rights Reserved.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;