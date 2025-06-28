from flask import Flask, jsonify, current_app, request, session
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_mail import Mail
from routes.quiz import quiz_bp
from config import get_config
from models.user import db
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from utils.email_service import mail
from routes.recognition import recognition_bp
from quiz_data import get_questions_for_level, is_passing_score
import random
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

    # All quiz-related routes are now handled by quiz_bp
    
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
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)