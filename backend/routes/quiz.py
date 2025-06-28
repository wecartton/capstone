from flask import Blueprint, jsonify, request, session, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from services.quiz_service import QuizService
from models.user import db
import random

# Create the quiz blueprint
quiz_bp = Blueprint('quiz', __name__)

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

@quiz_bp.route('/levels', methods=['GET'])
def get_available_levels():
    try:
        user_id = get_user_id()
        
        # Convert user_id to integer if it's from JWT
        if user_id != 'default_user':
            try:
                user_id = int(user_id)
            except (ValueError, TypeError):
                user_id = 'default_user'
        
        if user_id == 'default_user':
            # Return default levels for non-authenticated users
            levels = [
                {'level': 1, 'title': 'Level 1 - Basic Grammar', 'unlocked': True, 'completed': False},
                {'level': 2, 'title': 'Level 2 - Intermediate Grammar', 'unlocked': False, 'completed': False},
                {'level': 3, 'title': 'Level 3 - Advanced Grammar', 'unlocked': False, 'completed': False},
                {'level': 4, 'title': 'Level 4 - Complex Grammar', 'unlocked': False, 'completed': False},
                {'level': 5, 'title': 'Level 5 - Expert Grammar', 'unlocked': False, 'completed': False}
            ]
        else:
            levels = QuizService.get_available_levels(user_id)
        
        return jsonify({'levels': levels})
        
    except Exception as e:
        print(f"Error in get_available_levels: {e}")
        return jsonify({'error': 'Failed to fetch levels'}), 500

@quiz_bp.route('/<int:level>', methods=['GET'])
def get_quiz(level):
    #Get questions for a specific level
    try:
        user_id = get_user_id()
        
        print(f"=== GET QUIZ DEBUG ===")
        print(f"User ID: {user_id}")
        print(f"Requested Level: {level}")
        
        # Convert user_id to integer if it's from JWT
        if user_id != 'default_user':
            try:
                user_id = int(user_id)
                # Check if level is unlocked for authenticated users
                if not QuizService.is_level_unlocked(user_id, level):
                    print(f"ACCESS DENIED: Level {level} not unlocked for user {user_id}")
                    return jsonify({'error': 'Level not unlocked yet'}), 403
            except (ValueError, TypeError):
                user_id = 'default_user'
        
        # For default users, only allow level 1
        if user_id == 'default_user' and level > 1:
            print(f"ACCESS DENIED: Default user can only access level 1")
            return jsonify({'error': 'Please login to access higher levels'}), 403
        
        # Get questions for the level
        quiz_level, questions = QuizService.get_random_questions_subset(level, 30)
        
        if not quiz_level or not questions:
            print(f"NO QUESTIONS: No questions found for level {level}")
            return jsonify({'error': 'No questions available for this level'}), 404
        
        print(f"SUCCESS: Returning {len(questions)} questions for level {level}")
        
        return jsonify({'level': level, 'questions': questions, 'total_questions': len(questions)})
        
    except Exception as e:
        print(f"Error in get_quiz: {e}")
        return jsonify({'error': 'Failed to fetch quiz questions'}), 500

@quiz_bp.route('/practice/<int:level>', methods=['GET'])
def get_practice_quiz(level):
    """Get a subset of questions for practice mode."""
    try:
        user_id = get_user_id()
        
        # Check access
        if user_id != 'default_user':
            try:
                user_id = int(user_id)
                if not QuizService.is_level_unlocked(user_id, level):
                    return jsonify({'error': 'Level not unlocked yet'}), 403
            except (ValueError, TypeError):
                user_id = 'default_user'
        
        if user_id == 'default_user' and level > 1:
            return jsonify({'error': 'Please login to access higher levels'}), 403
        
        # Get 20 random questions for practice
        quiz_level, questions = QuizService.get_random_questions_subset(level, 20)
        
        if not quiz_level or not questions:
            return jsonify({'error': 'No questions available for practice'}), 404
        
        return jsonify({
            'level': level,
            'mode': 'practice',
            'questions': questions,
            'total_questions': len(questions)
        })
        
    except Exception as e:
        print(f"Error in get_practice_quiz: {e}")
        return jsonify({'error': 'Failed to fetch practice quiz'}), 500

@quiz_bp.route('/stats', methods=['GET'])
def get_quiz_system_stats():
    """Get overall quiz system statistics."""
    try:
        stats = QuizService.get_quiz_summary_stats()
        if stats:
            return jsonify(stats)
        else:
            return jsonify({'error': 'Failed to get statistics'}), 500
    except Exception as e:
        print(f"Error in get_quiz_system_stats: {e}")
        return jsonify({'error': 'Failed to fetch statistics'}), 500
        
@quiz_bp.route('/submit/<int:level>', methods=['POST'])
def submit_quiz(level):
    #Submit quiz answers and get results
    try:
        user_id = get_user_id()
        
        print(f"=== SUBMIT QUIZ DEBUG ===")
        print(f"User ID: {user_id}")
        print(f"Level: {level}")
        
        if user_id != 'default_user':
            try:
                user_id = int(user_id)
                # Check if level is unlocked for authenticated users
                if not QuizService.is_level_unlocked(user_id, level):
                    return jsonify({'error': 'Level not unlocked yet'}), 403
            except (ValueError, TypeError):
                user_id = 'default_user'
        
        # For default users, only allow level 1
        if user_id == 'default_user' and level > 1:
            return jsonify({'error': 'Please login to access higher levels'}), 403
        
        # Get submitted answers
        data = request.get_json()
        if not data or 'answers' not in data:
            return jsonify({'error': 'Invalid submission'}), 400
        
        submitted_answers = data['answers']
        print(f"Submitted answers: {submitted_answers}")
        
        if user_id != 'default_user':
            user_id = int(user_id)
            # Real-time Performance Analysis
            attempt = QuizService.submit_quiz_attempt(user_id, level, submitted_answers)
            
            if not attempt:
                return jsonify({'error': 'Failed to submit quiz'}), 500
            
            # Generate Comprehensive Feedback
            personalized_feedback = QuizService.generate_personalized_feedback(user_id, attempt)
            
            # Immediate Analysis Results
            result = {
                'level': level,
                'correct': attempt.score,
                'total': attempt.total_questions,
                'percentage': float(attempt.percentage),
                'passed': attempt.passed,
                'attempt_id': attempt.id,
                'performance_analysis': QuizService.analyze_attempt_performance(attempt),
                'feedback': personalized_feedback,
                'next_recommendation': QuizService.get_next_recommendation(user_id, level, attempt.passed)
            }
            
            # Store feedback for future reference
            QuizService.store_feedback_record(user_id, attempt.id, personalized_feedback)
            
            return jsonify(result)
        else:
            # Handle default user submission
            return handle_default_user_submission(level, submitted_answers)
            
    except Exception as e:
        print(f"Error in submit_quiz: {e}")
        return jsonify({'error': 'Failed to submit quiz'}), 500

def handle_default_user_submission(level, submitted_answers):
    try:
        # Get questions for the level
        quiz_level, questions = QuizService.get_questions_for_level(level, randomize=False)
        
        if not quiz_level or not questions:
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
        passed = percentage >= quiz_level.passing_threshold
        
        result = {
            'level': level,
            'correct': correct_count,
            'total': total_questions,
            'percentage': round(percentage, 2),
            'passed': passed
        }
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error in handle_default_user_submission: {e}")
        return jsonify({'error': 'Failed to process submission'}), 500

@quiz_bp.route('/progress', methods=['GET'])
@jwt_required()
def get_progress():
    try:
        user_id = int(get_jwt_identity())
        progress = QuizService.get_user_progress(user_id)
        
        return jsonify({
            'completed_levels': progress.get_completed_levels(),
            'highest_unlocked': progress.highest_unlocked_level,
            'total_attempts': progress.total_attempts,
            'total_passed': progress.total_passed
        })
        
    except Exception as e:
        print(f"Error in get_progress: {e}")
        return jsonify({'error': 'Failed to fetch progress'}), 500

@quiz_bp.route('/statistics', methods=['GET'])
@jwt_required()
def get_statistics():
    #Get user quiz statistics
    try:
        user_id = int(get_jwt_identity())
        stats = QuizService.get_quiz_statistics(user_id)
        
        return jsonify(stats)
        
    except Exception as e:
        print(f"Error in get_statistics: {e}")
        return jsonify({'error': 'Failed to fetch statistics'}), 500

@quiz_bp.route('/attempts', methods=['GET'])
@jwt_required()
def get_attempts():
    try:
        user_id = int(get_jwt_identity())
        level = request.args.get('level', type=int)
        limit = request.args.get('limit', 10, type=int)
        
        attempts = QuizService.get_user_attempts(user_id, level, limit)
        
        return jsonify({'attempts': attempts})
        
    except Exception as e:
        print(f"Error in get_attempts: {e}")
        return jsonify({'error': 'Failed to fetch attempts'}), 500

@quiz_bp.route('/reset', methods=['POST'])
@jwt_required()
def reset_progress():
    """Reset user progress (for testing)"""
    try:
        user_id = int(get_jwt_identity())
        QuizService.reset_user_progress(user_id)
        
        return jsonify({'status': 'success', 'message': 'Progress reset successfully'})
        
    except Exception as e:
        print(f"Error in reset_progress: {e}")
        return jsonify({'error': 'Failed to reset progress'}), 500

@quiz_bp.route('/admin/levels', methods=['GET'])
@jwt_required()
def get_all_levels():
    """Get all quiz levels (admin endpoint)"""
    try:
        from models.quiz import QuizLevel
        levels = QuizLevel.query.order_by(QuizLevel.level_number).all()
        
        return jsonify({
            'levels': [level.to_dict() for level in levels]
        })
        
    except Exception as e:
        print(f"Error in get_all_levels: {e}")
        return jsonify({'error': 'Failed to fetch levels'}), 500