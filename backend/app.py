from flask import Flask, jsonify, current_app, request, session
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_mail import Mail
from routes.quiz import quiz_bp
from config import get_config
from models.user import db
from models.quiz import QuizLevel, QuizQuestion, QuizAttempt, QuizAnswer, UserQuizProgress  # Import quiz models
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from utils.email_service import mail
from routes.recognition import recognition_bp
import os
    
def create_app():
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(get_config())
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    # configure CORS
    CORS(app, supports_credentials=True)
    
    print("Loaded config:", app.config)

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    jwt = JWTManager(app)
    
    # Register blueprints
    print("Registering blueprints...")
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')
    app.register_blueprint(recognition_bp, url_prefix='/api/recognition')
    app.register_blueprint(quiz_bp, url_prefix='/api/quiz')

    print("Blueprints registered")

    @app.route('/')
    def index():
        return jsonify({'message': 'ELLC API is running', 'status': 'OK'})

    @app.route('/api/health')
    def health_check():
        """Health check endpoint"""
        try:
            # Test database connection
            db.session.execute('SELECT 1')
            db_status = "OK"
        except Exception as e:
            db_status = f"Error: {str(e)}"
        
        # Check quiz data
        try:
            level_count = QuizLevel.query.count()
            question_count = QuizQuestion.query.count()
            quiz_status = f"OK - {level_count} levels, {question_count} questions"
        except Exception as e:
            quiz_status = f"Error: {str(e)}"
        
        return jsonify({
            'status': 'OK',
            'database': db_status,
            'quiz_data': quiz_status,
            'message': 'ELLC API is running'
        })
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({'error': 'Internal server error'}), 500

    # JWT error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'error': 'Token has expired',
            'message': 'Please log in again'
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'error': 'Invalid token',
            'message': 'Please log in again'
        }), 401

    @jwt.unauthorized_loader
    def unauthorized_callback(error):
        return jsonify({
            'error': 'Missing Authorization Header',
            'message': 'Please log in'
        }), 401

    # Create database tables
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully")
            
            # Check if quiz data exists
            level_count = QuizLevel.query.count()
            if level_count == 0:
                print("WARNING: No quiz levels found in database!")
                print("Please run 'python migrate_quiz_data.py' to populate quiz data")
            else:
                print(f"Found {level_count} quiz levels in database")
                
        except Exception as e:
            print(f"Error creating database tables: {e}")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)