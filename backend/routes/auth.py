from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import (
    create_access_token, create_refresh_token, 
    jwt_required, get_jwt_identity
)
from email_validator import validate_email, EmailNotValidError
from datetime import datetime, timedelta
import uuid

from models.user import db, User, PasswordResetToken, UserSession
from utils.email_service import send_password_reset_email
from utils.auth_utils import encrypt_data, decrypt_data

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    
    # Validate input
    if not data or not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Check if username or email already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 409
    
    # Validate email
    try:
        valid = validate_email(data['email'])
        email = valid.email
    except EmailNotValidError as e:
        return jsonify({'error': str(e)}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 409
    
    # Create new user
    try:
        new_user = User(
            username=data['username'],
            email=email,
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'message': 'User registered successfully',
            'user': new_user.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Registration failed: {str(e)}'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return tokens."""
    data = request.get_json()
    
    if not data or not all(k in data for k in ('username', 'password')):
        return jsonify({'error': 'Missing username or password'}), 400
    
    # Find user by username
    user = User.query.filter_by(username=data['username']).first()
    
    # Check if user exists and password is correct
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    # Create access and refresh tokens
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    
    # Create user session
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    
    # Encrypt sensitive data
    encrypted_ua = encrypt_data(user_agent)
    encrypted_ip = encrypt_data(ip_address)
    
    session = UserSession(
        user_id=user.id, 
        ip_address=encrypted_ip,
        user_agent=encrypted_ua
    )
    
    db.session.add(session)
    db.session.commit()
    
    return jsonify({
        'message': 'Login successful',
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': user.to_dict()
    }), 200

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Refresh access token."""
    current_user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user_id)
    
    return jsonify({
        'access_token': new_access_token
    }), 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """Log out a user by invalidating their session."""
    current_user_id = get_jwt_identity()
    
    # Delete the user's active sessions
    try:
        UserSession.query.filter_by(user_id=current_user_id).delete()
        db.session.commit()
        return jsonify({'message': 'Logged out successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Logout failed: {str(e)}'}), 500

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    """Generate a password reset token and send it via email."""
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400
    
    try:
        # Validate email
        valid = validate_email(data['email'])
        email = valid.email
    except EmailNotValidError:
        return jsonify({'error': 'Invalid email format'}), 400
    
    # Find user by email
    user = User.query.filter_by(email=email).first()
    
    # Always return success even if email doesn't exist (security best practice)
    if not user:
        return jsonify({'message': 'Password reset link sent if email exists'}), 200
    
    # Delete any existing reset tokens for this user
    PasswordResetToken.query.filter_by(user_id=user.id).delete()
    
    # Create a new reset token
    reset_token = PasswordResetToken(user_id=user.id)
    db.session.add(reset_token)
    db.session.commit()
    
    # Send email with reset link
    reset_url = f"http://localhost:3000/reset-password/{reset_token.token}"
    send_password_reset_email(user.email, reset_url)
    
    return jsonify({'message': 'Password reset link sent if email exists'}), 200

@auth_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    """Reset a user's password using a valid reset token."""
    data = request.get_json()
    
    if not data or 'password' not in data:
        return jsonify({'error': 'New password is required'}), 400
    
    # Find the token
    reset_token = PasswordResetToken.query.filter_by(token=token).first()
    
    if not reset_token or not reset_token.is_valid():
        return jsonify({'error': 'Invalid or expired token'}), 400
    
    # Find the user and update password
    user = User.query.get(reset_token.user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    try:
        # Update password
        user.set_password(data['password'])
        
        # Delete the used token
        db.session.delete(reset_token)
        db.session.commit()
        
        return jsonify({'message': 'Password reset successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Password reset failed: {str(e)}'}), 500

@auth_bp.route('/validate-token', methods=['GET'])
@jwt_required()
def validate_token():
    """Validate the current access token."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'valid': False}), 401
    
    return jsonify({
        'valid': True,
        'user': user.to_dict()
    }), 200