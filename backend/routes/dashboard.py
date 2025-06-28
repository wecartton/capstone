from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user import User, JourneyTrack

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get the user's profile information."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'user': user.to_dict()
    }), 200

@dashboard_bp.route('/journey', methods=['GET'])
@jwt_required()
def get_journey():
    """Get the user's journey tracking information."""
    current_user_id = get_jwt_identity()
    
    # For now, return placeholder data
    return jsonify({
        'status': 'Under Maintenance',
        'message': 'The Journey Tracking feature is currently under development.'
    }), 200

@dashboard_bp.route('/quiz', methods=['GET'])
@jwt_required()
def get_quizzes():
    """Get available quizzes for the user."""
    # For now, return placeholder data
    return jsonify({
        'status': 'Under Maintenance',
        'message': 'The Quiz feature is currently under development.'
    }), 200