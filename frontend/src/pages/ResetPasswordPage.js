import React from 'react';
import { useParams } from 'react-router-dom';
import ResetPasswordForm from '../components/ResetPasswordForm';
import logo from '../assets/ellc-logo.png';
import '../styles/ResetPasswordPage.css';

const ResetPasswordPage = () => {
  const { token } = useParams();

  if (!token) {
    return (
      <div className="reset-password-page">
        <div className="reset-password-container">
          <div className="reset-password-content">
            <h1>Invalid Reset Link</h1>
            <p>The password reset link is invalid or has expired.</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="reset-password-page">
      <div className="reset-password-container">
        <div className="reset-password-left">
          {/* This is where we'd put the background image with equipment */}
        </div>
        <div className="reset-password-right">
          <div className="reset-password-content">
            <div className="logo-container">
              <img src={logo} alt="ELLC Logo" className="logo" />
            </div>
            <ResetPasswordForm />
            <p className="copyright">2023 © CAPSTONE Design Project. All Rights Reserved.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResetPasswordPage;