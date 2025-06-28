from flask import Blueprint, jsonify, request, session, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
import random
from quiz_data import get_questions_for_level, is_passing_score

# Create the quiz blueprint
quiz_bp = Blueprint('quiz', __name__)

# Global user progress storage (in a real app, this would be a database)
user_progress = {}

def get_user_id():
    """Get user ID from JWT token or session fallback."""
    print(f"=== GET USER ID DEBUG ===")
    
    try:
        verify_jwt_in_request(optional=True)
        user_id = get_jwt_identity()
        print(f"JWT User ID: {user_id}")
        if user_id:
            result = str(user_id)  # Convert to string for consistency
            print(f"Using JWT User ID: {result}")
            return result
    except Exception as e:
        print(f"JWT Error: {e}")
    
    # Fallback to session
    session_user_id = session.get('user_id', 'default_user')
    print(f"Using Session User ID: {session_user_id}")
    return session_user_id

def initialize_user_progress(user_id):
    """Initialize user progress if not exists."""
    if user_id not in user_progress:
        user_progress[user_id] = {
            'completed_levels': [],
            'highest_unlocked': 1
        }
    return user_progress[user_id]

@quiz_bp.route('/levels', methods=['GET'])
def get_available_levels():
    """Get all available levels and their status (locked/unlocked)"""
    user_id = get_user_id()
    user_prog = initialize_user_progress(user_id)
    
    # Prepare level data for the frontend
    levels = []
    for level in range(1, 6):  # 5 levels total
        level_status = {
            'level': level,
            'unlocked': level <= user_prog['highest_unlocked'],
            'completed': level in user_prog['completed_levels']
        }
        levels.append(level_status)
    
    return jsonify({'levels': levels})

@quiz_bp.route('/<int:level>', methods=['GET'])
def get_quiz(level):
    """Get questions for a specific level"""
    user_id = get_user_id()
    user_prog = initialize_user_progress(user_id)
    
    print(f"=== GET QUIZ DEBUG ===")
    print(f"User ID: {user_id}")
    print(f"User Progress: {user_prog}")
    print(f"Requested Level: {level}")
    print(f"Highest Unlocked: {user_prog['highest_unlocked']}")
    print(f"Level Check: {level} <= {user_prog['highest_unlocked']} = {level <= user_prog['highest_unlocked']}")
    
    # Check if level is unlocked for this user
    if level > user_prog['highest_unlocked']:
        print(f"ACCESS DENIED: Level {level} > Highest Unlocked {user_prog['highest_unlocked']}")
        return jsonify({'error': 'Level not unlocked yet'}), 403
    
    # Get questions for the level
    questions = get_questions_for_level(level)
    
    if not questions:
        print(f"NO QUESTIONS: No questions found for level {level}")
        return jsonify({'error': 'No questions available for this level'}), 404
    
    print(f"SUCCESS: Returning {len(questions)} questions for level {level}")
    
    # Randomize questions order
    random.shuffle(questions)
    
    return jsonify({'level': level, 'questions': questions})

@quiz_bp.route('/submit/<int:level>', methods=['POST'])
def submit_quiz(level):
    """Submit quiz answers and get results"""
    user_id = get_user_id()
    user_prog = initialize_user_progress(user_id)
    
    # Check if level is unlocked for this user
    if level > user_prog['highest_unlocked']:
        return jsonify({'error': 'Level not unlocked yet'}), 403
    
    # Get submitted answers
    data = request.get_json()
    if not data or 'answers' not in data:
        return jsonify({'error': 'Invalid submission'}), 400
    
    submitted_answers = data['answers']
    
    # Get questions for the level
    questions = get_questions_for_level(level)
    
    if not questions:
        return jsonify({'error': 'No questions available for this level'}), 404
    
    # Calculate score
    correct_count = 0
    total_questions = len(questions)
    
    # Create a dictionary of question IDs to correct answers
    correct_answers = {q['id']: q['correct_answer'] for q in questions}
    
    # Check each submitted answer
    for answer in submitted_answers:
        question_id = answer.get('question_id')
        selected_option = answer.get('selected_option')
        
        if question_id in correct_answers and selected_option == correct_answers[question_id]:
            correct_count += 1
    
    # Calculate percentage
    percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
    
    # Determine if user passed the level
    passed = is_passing_score(level, correct_count, total_questions)
    
    # Update user progress if they passed
    if passed:
        # Mark level as completed
        if level not in user_prog['completed_levels']:
            user_prog['completed_levels'].append(level)
        
        # Unlock next level if available
        if level == user_prog['highest_unlocked'] and level < 5:
            user_prog['highest_unlocked'] = level + 1
    
    # Prepare result
    result = {
        'level': level,
        'correct': correct_count,
        'total': total_questions,
        'percentage': round(percentage, 2),
        'passed': passed
    }
    
    return jsonify(result)

@quiz_bp.route('/progress', methods=['GET'])
def get_progress():
    """Get user progress"""
    user_id = get_user_id()
    user_prog = initialize_user_progress(user_id)
    return jsonify(user_prog)

@quiz_bp.route('/reset', methods=['POST'])
def reset_progress():
    """Reset user progress (for testing)"""
    user_id = get_user_id()
    user_progress[user_id] = {
        'completed_levels': [],
        'highest_unlocked': 1
    }
    return jsonify({'status': 'success', 'message': 'Progress reset successfully'})