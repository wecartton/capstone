import React from 'react';
import ForgotPasswordForm from '../components/ForgotPasswordForm';
import logo from '../assets/ellc-logo.png';
import '../styles/ForgotPasswordPage.css';

const ForgotPasswordPage = () => {
  return (
    <div className="forgot-password-page">
      <div className="forgot-password-container">
        <div className="forgot-password-left">
          {/* This is where we'd put the background image with equipment */}
        </div>
        <div className="forgot-password-right">
          <div className="forgot-password-content">
            <div className="logo-container">
              <img src={logo} alt="ELLC Logo" className="logo" />
            </div>
            <ForgotPasswordForm />
            <p className="copyright">2023 © CAPSTONE Design Project. All Rights Reserved.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ForgotPasswordPage;