import React, { createContext, useState, useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { authService } from '../services/api.service';

// Create context
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Initialize auth state on app load
  useEffect(() => {
    const initAuth = async () => {
      const storedUser = localStorage.getItem('user');
      const token = localStorage.getItem('accessToken');

      if (storedUser && token) {
        try {
          // Validate the token
          const response = await authService.validateToken();
          if (response.data.valid) {
            setUser(JSON.parse(storedUser));
          } else {
            // Token is invalid
            handleLogout();
          }
        } catch (error) {
          console.error('Auth initialization error:', error);
          handleLogout();
        }
      }
      
      setLoading(false);
    };

    initAuth();
  }, []);

  // Login the user
  const login = async (credentials) => {
    try {
      const response = await authService.login(credentials);
      const { user, access_token, refresh_token } = response.data;
      
      // Store tokens and user data
      localStorage.setItem('accessToken', access_token);
      localStorage.setItem('refreshToken', refresh_token);
      localStorage.setItem('user', JSON.stringify(user));
      
      setUser(user);
      return { success: true };
    } catch (error) {
      return { 
        success: false, 
        message: error.response?.data?.error || 'Login failed' 
      };
    }
  };

  // Register a new user
  const register = async (userData) => {
    try {
      const response = await authService.register(userData);
      return { success: true, data: response.data };
    } catch (error) {
      return { 
        success: false, 
        message: error.response?.data?.error || 'Registration failed' 
      };
    }
  };

  // Logout the user
  const handleLogout = async () => {
    try {
      if (user) {
        await authService.logout();
      }
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      // Clear stored data
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('user');
      setUser(null);
      navigate('/login');
    }
  };

  // Forgot password
  const forgotPassword = async (email) => {
    try {
      await authService.forgotPassword(email);
      return { success: true };
    } catch (error) {
      return { 
        success: false, 
        message: error.response?.data?.error || 'Failed to send reset email' 
      };
    }
  };

  // Reset password
  const resetPassword = async (token, password) => {
    try {
      await authService.resetPassword(token, password);
      return { success: true };
    } catch (error) {
      return { 
        success: false, 
        message: error.response?.data?.error || 'Password reset failed' 
      };
    }
  };

  // Context value
  const value = {
    user,
    isAuthenticated: !!user,
    loading,
    login,
    register,
    logout: handleLogout,
    forgotPassword,
    resetPassword
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to use the auth context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export default AuthContext;