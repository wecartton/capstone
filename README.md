Project Root Structure

```
capstone-ellc/
├── backend/                 # Flask backend application
├── frontend/                # React frontend application
├── README.md                # Project documentation
└── .gitignore               # Git ignore rules
```

Backend Structure (Flask)

```
backend/
├── .env                     # Environment variables (create from .env.example)
├── .env.example             # Environment template
├── app.py                   # Main Flask application
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── credentials.json         # Google OAuth2 credentials (download from Google Cloud)
├── token.pickle             # Auto-generated OAuth2 token file
├── models/
│   ├── __init__.py          # Makes models a Python package
│   └── user.py              # User and authentication models
├── routes/
│   ├── __init__.py          # Makes routes a Python package  
│   ├── auth.py              # Authentication routes
│   └── dashboard.py         # Dashboard routes
├── utils/
│   ├── __init__.py          # Makes utils a Python package
│   ├── auth_utils.py        # Authentication utilities
│   ├── email_service.py     # Email service (OAuth2 primary)
│   └── email_service_oauth2.py  # Gmail OAuth2 implementation
└── test_scripts/
    ├── test_db.py           # Database connection test
    ├── test_email_oauth2.py # OAuth2 email test
    ├── reset_oauth_token.py # Reset OAuth2 token
    ├── check_oauth_status.py # Check OAuth2 status
    ├── reset_password.py    # Manual password reset
    └── fix_password.py      # Fix password hashing
```

Frontend Structure (React)

```
frontend/
├── package.json             # NPM package configuration
├── public/
│   ├── index.html           # HTML template
│   ├── favicon.ico          # Site favicon
│   ├── logo192.png          # App logo (192x192)
│   ├── logo512.png          # App logo (512x512)
│   ├── manifest.json        # Web app manifest
│   └── robots.txt           # Robots configuration
└── src/
    ├── index.js             # Application entry point
    ├── App.js               # Main App component
    ├── reportWebVitals.js   # Performance reporting
    ├── assets/
    │   ├── ellc-logo.png    # ELLC logo image
    │   └── login-bg.jpg     # Login background image
    ├── components/
    │   ├── AgentChat.js     # AI Agent chat component
    │   ├── DashboardCard.js # Dashboard card component
    │   ├── ForgotPasswordForm.js # Forgot password form
    │   ├── Header.js        # Header component
    │   ├── LoginForm.js     # Login form component
    │   ├── RegisterForm.js  # Registration form component
    │   └── ResetPasswordForm.js # Password reset form
    ├── context/
    │   └── AuthContext.js   # Authentication context
    ├── pages/
    │   ├── DashboardPage.js # Main dashboard page
    │   ├── ForgotPasswordPage.js # Forgot password page
    │   ├── JourneyPage.js   # Journey tracking page
    │   ├── LoginPage.js     # Login page
    │   ├── QuizPage.js      # Quiz page
    │   ├── RegisterPage.js  # Registration page
    │   ├── ResetPasswordPage.js # Password reset page
    │   └── TalkWithAgentPage.js # AI Agent page
    ├── services/
    │   └── api.service.js   # API communication service
    ├── styles/
    │   ├── App.css          # Main app styles
    │   ├── index.css        # Base styles
    │   ├── AgentChat.css    # Agent chat styles
    │   ├── DashboardCard.css # Dashboard card styles
    │   ├── DashboardPage.css # Dashboard page styles
    │   ├── ForgotPasswordForm.css # Forgot password form styles
    │   ├── ForgotPasswordPage.css # Forgot password page styles
    │   ├── Header.css       # Header styles
    │   ├── LoginForm.css    # Login form styles
    │   ├── LoginPage.css    # Login page styles
    │   ├── RegisterForm.css # Register form styles
    │   ├── RegisterPage.css # Register page styles
    │   ├── ResetPasswordForm.css # Reset password form styles
    │   ├── ResetPasswordPage.css # Reset password page styles
    │   ├── TalkWithAgentPage.css # Talk with agent page styles
    │   └── UnderMaintenancePage.css # Under maintenance page styles
    └── utils/               
```

Database Structure

```sql
-- Database: ellc_system

-- Users table for authentication
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Password reset tokens
CREATE TABLE password_reset_tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    token VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- User sessions for session management
CREATE TABLE user_sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    session_token VARCHAR(255) NOT NULL UNIQUE,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Quiz placeholders (for future implementation)
CREATE TABLE quizzes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Journey tracking placeholders (for future implementation)
CREATE TABLE journey_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    progress INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

Key Features Implemented

Backend Features 
1. User Authentication
   - User registration and login
   - JWT token management (access & refresh tokens)
   - Password hashing with bcrypt
   - Session management

2. Password Reset
   - Email-based password reset
   - Token-based reset links
   - Gmail OAuth2 integration
   - Secure token expiration

3. Security Features
   - Data encryption for sensitive information
   - CORS configuration
   - Route protection with JWT
   - SQL injection protection with SQLAlchemy

4. Database Integration
   - MySQL connection with PyMySQL
   - Database models with relationships
   - Migration support

Frontend Features 
1. Authentication UI
   - Login page with form validation
   - Registration page
   - Forgot password functionality
   - Password reset page

2. Protected Routes
   - Dashboard with navigation
   - Route protection based on authentication
   - Automatic token refresh

3. Dashboard
   - Three main feature cards
   - Talk with AI Agent interface
   - Placeholder pages for Quiz and Journey

4. Responsive Design
   - Professional UI with matching design
   - Consistent styling across pages
   - Loading states and error handling

Configuration Files

Backend .env.example
```env
# Flask configuration
FLASK_ENV=development
FLASK_APP=app.py
SECRET_KEY=your-secret-key-change-in-production

# Database configuration
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ellc_system

# JWT configuration
JWT_SECRET_KEY=your-jwt-secret-key-change-in-production

# Gmail OAuth2 configuration
GOOGLE_CREDENTIALS_FILE=credentials.json
GOOGLE_TOKEN_FILE=token.pickle
GMAIL_USER_EMAIL=your-email@gmail.com
```

Frontend package.json (key dependencies)
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.16.0",
    "axios": "^1.5.1"
  },
  "proxy": "http://localhost:5000"
}
```

Backend requirements.txt
```txt
Flask==2.3.3
Flask-Cors==4.0.0
Flask-JWT-Extended==4.5.3
Flask-SQLAlchemy==3.1.1
Flask-Mail==0.9.1
PyMySQL==1.1.0
python-dotenv==1.0.0
bcrypt==4.0.1
cryptography==41.0.4
email-validator==2.0.0
google-auth==2.23.4
google-auth-oauthlib==1.0.0
google-auth-httplib2==0.1.1
google-api-python-client==2.108.0
```

API Endpoints

Authentication Endpoints
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/refresh` - Refresh access token
- `POST /api/auth/forgot-password` - Request password reset
- `POST /api/auth/reset-password/<token>` - Reset password
- `GET /api/auth/validate-token` - Validate current token

Dashboard Endpoints
- `GET /api/dashboard/profile` - Get user profile
- `GET /api/dashboard/journey` - Get journey data (placeholder)
- `GET /api/dashboard/quiz` - Get quiz data (placeholder)

Setup Instructions

1. Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Configure .env file
# Setup MySQL database
# Download credentials.json from Google Cloud
flask run --debug
```

2. Frontend Setup
```bash
cd frontend
npm install
npm start
```

3. Google OAuth2 Setup
1. Create Google Cloud Project
2. Enable Gmail API
3. Create OAuth2 credentials
4. Download credentials.json
5. Configure OAuth consent screen
6. Add test users

Security Considerations

1. Environment Variables - All secrets in .env
2. Password Hashing - Bcrypt with salt
3. JWT Security - Secure secret keys and expiration
4. Data Encryption - Sensitive data encrypted at rest
5. CORS Protection - Configured for specific origins
6. SQL Injection Protection - SQLAlchemy ORM
7. OAuth2 Security - Following Google best practices

Future Enhancements

1. Quiz System - Full implementation with database
2. Journey Tracking - Progress tracking system  
3. AI Agent Backend - Connect to actual AI service
4. Admin Panel - User management interface
5. Analytics - Usage tracking and reports
6. Mobile App - React Native implementation
7. Real-time Features - WebSocket integration
