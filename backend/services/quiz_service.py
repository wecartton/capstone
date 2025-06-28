from datetime import datetime, timedelta
from sqlalchemy import func
from models.user import db
from flask import jsonify
from models.quiz import QuizLevel, QuizQuestion, QuizAttempt, QuizAnswer, UserQuizProgress
import random
import time
from functools import wraps

def monitor_performance(func):
    """Decorator to monitor function performance."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        
        if execution_time > 1.0:  # Log slow queries (>1 second)
            print(f"⚠️  Slow query detected: {func.__name__} took {execution_time:.2f} seconds")
        elif execution_time > 0.5:  # Log moderately slow queries
            print(f"📊 Performance: {func.__name__} took {execution_time:.2f} seconds")
        
        return result
    return wrapper

def handle_default_user_submission(level, submitted_answers):
    try:
        # Get the SAME 30 random questions that were shown to the user
        # Since we can't track which specific questions were shown to default users,
        # we need to calculate based on submitted answers only
        
        # Get the level info for passing threshold
        quiz_level = QuizLevel.query.filter_by(level_number=level, is_active=True).first()
        
        if not quiz_level:
            return jsonify({'error': 'Level not found'}), 404
        
        # Calculate score based on submitted answers only
        correct_count = 0
        total_questions = len(submitted_answers)  # Use actual submitted answers count
        
        # Get ALL questions for this level to check correct answers
        all_questions = QuizQuestion.query.filter_by(level_id=quiz_level.id, is_active=True).all()
        correct_answers = {q.id: q.correct_answer for q in all_questions}
        
        # Check each submitted answer
        for answer in submitted_answers:
            question_id = answer.get('question_id')
            selected_option = answer.get('selected_option')
            
            if question_id in correct_answers and selected_option == correct_answers[question_id]:
                correct_count += 1
        
        # Calculate percentage based on actual questions answered
        percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
        
        # Determine if user passed the level
        passed = percentage >= quiz_level.passing_threshold
        
        result = {
            'level': level,
            'correct': correct_count,
            'total': total_questions,  # This will be 30 now
            'percentage': round(percentage, 2),
            'passed': passed
        }
        
        print(f"Default user result: {correct_count}/{total_questions} = {percentage}%")
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error in handle_default_user_submission: {e}")
        return jsonify({'error': 'Failed to process submission'}), 500
        
class QuizService:
    """Service class for managing quiz operations."""
    
    @staticmethod
    def get_user_progress(user_id):
        progress = UserQuizProgress.query.filter_by(user_id=user_id).first()
        
        if not progress:
            # Create new progress for user
            progress = UserQuizProgress(user_id=user_id)
            db.session.add(progress)
            db.session.commit()
        
        return progress
    
    @staticmethod
    def get_available_levels(user_id):
        #Get all available levels and their status for a user
        progress = QuizService.get_user_progress(user_id)
        completed_levels = progress.get_completed_levels()
        
        levels = QuizLevel.query.filter_by(is_active=True).order_by(QuizLevel.level_number).all()
        
        level_status = []
        for level in levels:
            status = {
                'level': level.level_number,
                'title': level.title,
                'description': level.description,
                'unlocked': level.level_number <= progress.highest_unlocked_level,
                'completed': level.level_number in completed_levels,
                'passing_threshold': level.passing_threshold
            }
            level_status.append(status)
        
        return level_status
    
    @staticmethod
    @monitor_performance
    def get_questions_for_level(level_number, randomize=True):
        #Get questions for a specific level
        level = QuizLevel.query.filter_by(level_number=level_number, is_active=True).first()
        
        if not level:
            return None, None
        
        questions = QuizQuestion.query.filter_by(
            level_id=level.id, 
            is_active=True
        ).order_by(QuizQuestion.question_number).all()
        
        if randomize:
            random.shuffle(questions)
        
        questions_dict = [q.to_dict() for q in questions]
        
        return level, questions_dict
    
    @staticmethod
    def is_level_unlocked(user_id, level_number):
        #Check if a level is unlocked for a user
        progress = QuizService.get_user_progress(user_id)
        return level_number <= progress.highest_unlocked_level
    
    @staticmethod
    def start_quiz_attempt(user_id, level_number):
        """Start a new quiz attempt."""
        level = QuizLevel.query.filter_by(level_number=level_number, is_active=True).first()
        
        if not level:
            return None
        
        if not QuizService.is_level_unlocked(user_id, level_number):
            return None
        
        # Create new attempt
        attempt = QuizAttempt(
            user_id=user_id,
            level_id=level.id,
            score=0,
            total_questions=0,
            percentage=0.0,
            passed=False,
            started_at=datetime.utcnow()
        )
        
        db.session.add(attempt)
        db.session.commit()
        
        return attempt
    
    @staticmethod
    @monitor_performance
    def submit_quiz_attempt(user_id, level_number, answers):
        #Submit quiz attempt and calculate results
        level = QuizLevel.query.filter_by(level_number=level_number, is_active=True).first()
        
        if not level:
            return None
        
        # Get the most recent incomplete attempt
        attempt = QuizAttempt.query.filter_by(
            user_id=user_id,
            level_id=level.id,
            completed_at=None
        ).order_by(QuizAttempt.started_at.desc()).first()
        
        if not attempt:
            # Create new attempt if none exists
            attempt = QuizService.start_quiz_attempt(user_id, level_number)
        
        # Get all questions for this level
        questions = QuizQuestion.query.filter_by(level_id=level.id, is_active=True).all()
        question_dict = {q.id: q for q in questions}
        
        # Process answers
        correct_count = 0
        total_questions = len(answers)
        
        # Clear existing answers for this attempt
        QuizAnswer.query.filter_by(attempt_id=attempt.id).delete()
        
        # Process submitted answers
        for answer_data in answers:
            question_id = answer_data.get('question_id')
            selected_option = answer_data.get('selected_option')
            
            if question_id in question_dict:
                question = question_dict[question_id]
                is_correct = selected_option == question.correct_answer
                
                if is_correct:
                    correct_count += 1
                
                # Save answer
                quiz_answer = QuizAnswer(
                    attempt_id=attempt.id,
                    question_id=question_id,
                    selected_answer=selected_option,
                    is_correct=is_correct
                )
                db.session.add(quiz_answer)
        
        # Calculate results
        percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
        passed = percentage >= level.passing_threshold
        
        # Update attempt
        attempt.score = correct_count
        attempt.total_questions = total_questions
        attempt.percentage = percentage
        attempt.passed = passed
        attempt.completed_at = datetime.utcnow()
        
        if attempt.started_at:
            time_taken = (attempt.completed_at - attempt.started_at).total_seconds()
            attempt.time_taken = int(time_taken)
        
        print(f"Authenticated user result: {correct_count}/{total_questions} = {percentage}%")
        
        db.session.commit()
        
        # Update user progress if passed
        if passed:
            QuizService.update_user_progress(user_id, level_number)
        
        return attempt

    @staticmethod
    def update_user_progress(user_id, completed_level):
        #Update user progress after completing a level
        progress = QuizService.get_user_progress(user_id)
        
        # progress analysis
        progress.total_attempts += 1
        
        # Check if a new level completion
        completed_levels = progress.get_completed_levels()
        if completed_level not in completed_levels:
            progress.total_passed += 1
        
        # Adaptive Level Unlocking Analysis
        if completed_level == progress.highest_unlocked_level and completed_level < 5:
            # Analyze if student is ready for next level
            recent_attempts = QuizAttempt.query.filter_by(
                user_id=user_id
            ).order_by(QuizAttempt.created_at.desc()).limit(3).all()
            
            # Performance consistency check
            if len(recent_attempts) >= 2:
                recent_scores = [a.percentage for a in recent_attempts if a.passed]
                if len(recent_scores) >= 2 and min(recent_scores) > 70:
                    # Student shows consistent good performance
                    progress.highest_unlocked_level = completed_level + 1
            else:
                # Standard unlock for first completion
                progress.highest_unlocked_level = completed_level + 1
        
        progress.updated_at = datetime.utcnow()
        db.session.commit()
        
        return progress
    
    @staticmethod
    def get_user_attempts(user_id, level_number=None, limit=10):
        #Get user's quiz attempts history
        query = QuizAttempt.query.filter_by(user_id=user_id)
        
        if level_number:
            level = QuizLevel.query.filter_by(level_number=level_number).first()
            if level:
                query = query.filter_by(level_id=level.id)
        
        attempts = query.order_by(QuizAttempt.created_at.desc()).limit(limit).all()
        return [attempt.to_dict() for attempt in attempts]
    
    @staticmethod
    def get_quiz_statistics(user_id):
        progress = QuizService.get_user_progress(user_id)
        
        # Get all attempts
        attempts = QuizAttempt.query.filter_by(user_id=user_id).all()
        
        # performance analysis calculations
        total_attempts = len(attempts)
        passed_attempts = len([a for a in attempts if a.passed])
        
        if total_attempts > 0:
            # Statistical Analysis
            average_score = sum([a.percentage for a in attempts]) / total_attempts
            best_score = max([a.percentage for a in attempts])
            worst_score = min([a.percentage for a in attempts])
            
            # Performance Trend Analysis
            recent_attempts = sorted(attempts, key=lambda x: x.created_at)[-5:]
            if len(recent_attempts) >= 2:
                recent_average = sum([a.percentage for a in recent_attempts]) / len(recent_attempts)
                improvement_rate = recent_average - average_score
            else:
                improvement_rate = 0
        else:
            average_score = 0
            best_score = 0
            worst_score = 0
            improvement_rate = 0
        
        # Level-by-Level Performance Analysis
        level_stats = {}
        for attempt in attempts:
            level_num = attempt.level.level_number
            if level_num not in level_stats:
                level_stats[level_num] = {
                    'attempts': 0,
                    'passed': 0,
                    'best_score': 0,
                    'average_score': 0,
                    'scores': [],
                    'last_attempt': None,
                    'success_rate': 0
                }
            
            level_stats[level_num]['attempts'] += 1
            level_stats[level_num]['scores'].append(attempt.percentage)
            
            if attempt.passed:
                level_stats[level_num]['passed'] += 1
            
            if attempt.percentage > level_stats[level_num]['best_score']:
                level_stats[level_num]['best_score'] = attempt.percentage
            
            if not level_stats[level_num]['last_attempt'] or attempt.created_at > level_stats[level_num]['last_attempt']:
                level_stats[level_num]['last_attempt'] = attempt.created_at
        
        # Calculate success rates and averages per level
        for level_num in level_stats:
            stats = level_stats[level_num]
            stats['success_rate'] = (stats['passed'] / stats['attempts']) * 100 if stats['attempts'] > 0 else 0
            stats['average_score'] = sum(stats['scores']) / len(stats['scores']) if stats['scores'] else 0
            stats['average_score'] = round(stats['average_score'], 2)
        
        # Analyzed Performance Output
        return {
            'total_attempts': total_attempts,
            'passed_attempts': passed_attempts,
            'success_rate': round((passed_attempts / total_attempts) * 100, 2) if total_attempts > 0 else 0,
            'total_passed_levels': progress.total_passed,
            'highest_unlocked_level': progress.highest_unlocked_level,
            'average_score': round(average_score, 2),
            'best_score': round(best_score, 2),
            'worst_score': round(worst_score, 2),
            'improvement_rate': round(improvement_rate, 2),
            'level_statistics': level_stats,
            'learning_progress': QuizService.analyze_learning_progress(user_id)
        }
    
    @staticmethod
    def analyze_attempt_performance(attempt):
        """Analyze performance for a specific attempt."""
        percentage = float(attempt.percentage)
        time_taken = attempt.time_taken if attempt.time_taken else 0
        
        # Performance Analysis
        performance = {
            'score_category': 'excellent' if percentage >= 90 else 'good' if percentage >= 80 else 'satisfactory' if percentage >= 70 else 'needs_improvement',
            'time_efficiency': 'fast' if time_taken < 300 else 'normal' if time_taken < 600 else 'slow',
            'accuracy_rate': percentage,
            'questions_correct': attempt.score,
            'questions_total': attempt.total_questions
        }
        
        # Strength and weakness analysis
        if percentage >= 80:
            performance['strengths'] = ['Good understanding of grammar concepts', 'Consistent performance']
            performance['weaknesses'] = ['Minor areas for improvement'] if percentage < 100 else []
        else:
            performance['strengths'] = ['Showing effort and progress']
            performance['weaknesses'] = ['Need more practice with grammar rules', 'Review basic concepts']
        
        return performance
    
    @staticmethod
    def analyze_learning_progress(user_id):
        #Analyze learning patterns and progress
        attempts = QuizAttempt.query.filter_by(user_id=user_id).order_by(QuizAttempt.created_at).all()
        
        if len(attempts) < 2:
            return {'trend': 'insufficient_data', 'pattern': 'new_learner'}
        
        # Time-based Analysis
        recent_month = [a for a in attempts if (datetime.utcnow() - a.created_at).days <= 30]
        previous_month = [a for a in attempts if 30 < (datetime.utcnow() - a.created_at).days <= 60]
        
        # Progress Pattern Analysis
        if len(recent_month) > len(previous_month):
            activity_trend = 'increasing'
        elif len(recent_month) < len(previous_month):
            activity_trend = 'decreasing'
        else:
            activity_trend = 'stable'
        
        # Performance Trend Analysis
        if len(recent_month) > 0 and len(previous_month) > 0:
            recent_avg = sum([a.percentage for a in recent_month]) / len(recent_month)
            previous_avg = sum([a.percentage for a in previous_month]) / len(previous_month)
            
            if recent_avg > previous_avg + 5:
                performance_trend = 'improving'
            elif recent_avg < previous_avg - 5:
                performance_trend = 'declining'
            else:
                performance_trend = 'stable'
        else:
            performance_trend = 'unknown'
        
        return {
            'activity_trend': activity_trend,
            'performance_trend': performance_trend,
            'recent_activity': len(recent_month),
            'consistency': 'high' if len(attempts) > 10 else 'medium' if len(attempts) > 5 else 'low'
        }
        
    @staticmethod
    def reset_user_progress(user_id):
        """Reset user progress (for testing purposes)."""
        # Delete all attempts and answers
        attempts = QuizAttempt.query.filter_by(user_id=user_id).all()
        for attempt in attempts:
            QuizAnswer.query.filter_by(attempt_id=attempt.id).delete()
        
        QuizAttempt.query.filter_by(user_id=user_id).delete()
        
        # Reset progress
        progress = UserQuizProgress.query.filter_by(user_id=user_id).first()
        if progress:
            progress.highest_unlocked_level = 1
            progress.total_attempts = 0
            progress.total_passed = 0
            progress.updated_at = datetime.utcnow()
        
        db.session.commit()
        return True
    
    @staticmethod
    def generate_personalized_feedback(user_id, attempt):
        #Generate personalized feedback based on performance analysis
        # Get user's learning history for context
        user_attempts = QuizAttempt.query.filter_by(user_id=user_id).order_by(QuizAttempt.created_at.desc()).limit(10).all()
        progress = QuizService.get_user_progress(user_id)
        
        feedback = {
            'performance_feedback': QuizService.get_performance_feedback(attempt),
            'improvement_suggestions': QuizService.get_improvement_suggestions(user_id, attempt),
            'learning_path_recommendation': QuizService.get_learning_path_recommendation(user_id, attempt),
            'motivation_message': QuizService.get_motivation_message(user_id, attempt),
            'study_recommendations': QuizService.get_study_recommendations(attempt)
        }
        
        return feedback

    @staticmethod
    def get_performance_feedback(attempt):
        """Generate specific performance feedback."""
        percentage = float(attempt.percentage)
        level_num = attempt.level.level_number
        
        if percentage >= 90:
            return {
                'level': 'excellent',
                'message': f"Outstanding performance on Level {level_num}! You've mastered these grammar concepts.",
                'confidence': 'high'
            }
        elif percentage >= 80:
            return {
                'level': 'good',
                'message': f"Great work on Level {level_num}! You have a strong understanding of the material.",
                'confidence': 'high'
            }
        elif percentage >= 70:
            return {
                'level': 'satisfactory',
                'message': f"Good effort on Level {level_num}! You're on the right track with some room for improvement.",
                'confidence': 'medium'
            }
        elif percentage >= 60:
            return {
                'level': 'needs_work',
                'message': f"You're making progress on Level {level_num}, but need more practice with these concepts.",
                'confidence': 'low'
            }
        else:
            return {
                'level': 'needs_significant_work',
                'message': f"Level {level_num} requires more study. Don't give up - practice makes perfect!",
                'confidence': 'low'
            }

    @staticmethod
    def get_improvement_suggestions(user_id, attempt):
        suggestions = []
        percentage = float(attempt.percentage)
        level_num = attempt.level.level_number
        
        # Analyze wrong answers for targeted suggestions
        wrong_answers = QuizAnswer.query.filter_by(
            attempt_id=attempt.id,
            is_correct=False
        ).all()
        
        if len(wrong_answers) > 0:
            # Grammar-specific suggestions based on level
            if level_num <= 2:
                suggestions.append("Focus on basic verb forms and subject-verb agreement")
                suggestions.append("Practice with simple present tense rules")
            elif level_num <= 4:
                suggestions.append("Review advanced grammar structures and verb tenses")
                suggestions.append("Practice with complex sentence formation")
            else:
                suggestions.append("Study expert-level grammar rules and exceptions")
                suggestions.append("Focus on nuanced grammar usage and context")
        
        # Performance-based suggestions
        if percentage < 70:
            suggestions.append("Take more time to read each question carefully")
            suggestions.append("Review grammar basics before attempting higher levels")
        
        if attempt.time_taken and attempt.time_taken < 300:  # Less than 5 minutes
            suggestions.append("Take more time to think through each answer")
        
        return suggestions

    @staticmethod
    def get_next_recommendation(user_id, current_level, passed):
        """Get recommendation for next action."""
        if passed:
            if current_level < 5:
                return {
                    'action': 'advance',
                    'message': f'Great job! You can now proceed to Level {current_level + 1}',
                    'next_level': current_level + 1,
                    'ready': True
                }
            else:
                return {
                    'action': 'complete',
                    'message': 'Congratulations! You have completed all levels!',
                    'next_level': None,
                    'ready': False
                }
        else:
            return {
                'action': 'retry',
                'message': f'Keep practicing! Try Level {current_level} again when ready.',
                'next_level': current_level,
                'ready': True
            }
    
    @staticmethod
    def get_next_level_difficulty(level_number):
        """Get difficulty estimate for next level."""
        difficulties = {
            1: 'beginner',
            2: 'elementary', 
            3: 'intermediate',
            4: 'advanced',
            5: 'expert'
        }
        return difficulties.get(level_number, 'unknown')
    
    @staticmethod
    def get_quiz_summary_stats():
        """Get comprehensive quiz statistics for dashboard."""
        try:
            total_levels = QuizLevel.query.count()
            total_questions = QuizQuestion.query.count()
            total_attempts = QuizAttempt.query.count()
            
            # Question distribution per level
            level_stats = db.session.query(
                QuizLevel.level_number,
                QuizLevel.title,
                func.count(QuizQuestion.id).label('question_count'),
                QuizLevel.passing_threshold
            ).outerjoin(QuizQuestion).group_by(QuizLevel.id).order_by(QuizLevel.level_number).all()
            
            return {
                'total_levels': total_levels,
                'total_questions': total_questions,
                'total_attempts': total_attempts,
                'questions_per_level': 30,  # New standard
                'level_breakdown': [
                    {
                        'level': stat.level_number,
                        'title': stat.title,
                        'question_count': stat.question_count,
                        'threshold': stat.passing_threshold
                    }
                    for stat in level_stats
                ]
            }
        except Exception as e:
            print(f"Error getting quiz stats: {e}")
            return None
    
    @staticmethod
    def get_random_questions_subset(level_number, count=20):
        """Get a random subset of questions for practice mode."""
        try:
            level = QuizLevel.query.filter_by(level_number=level_number, is_active=True).first()
            if not level:
                return None, None
                
            # Get random subset of questions
            questions = QuizQuestion.query.filter_by(
                level_id=level.id, 
                is_active=True
            ).order_by(func.random()).limit(count).all()
            
            questions_dict = [q.to_dict() for q in questions]
            return level, questions_dict
            
        except Exception as e:
            print(f"Error getting random questions: {e}")
            return None, None
        
    @staticmethod
    def get_learning_path_recommendation(user_id, attempt):
        percentage = float(attempt.percentage)
        level_num = attempt.level.level_number
        progress = QuizService.get_user_progress(user_id)
        
        if attempt.passed:
            if level_num < 5:
                return {
                    'next_action': 'advance',
                    'recommendation': f"Ready for Level {level_num + 1}",
                    'confidence_level': 'high' if percentage > 80 else 'medium',
                    'estimated_difficulty': QuizService.get_next_level_difficulty(level_num + 1)
                }
            else:
                return {
                    'next_action': 'complete',
                    'recommendation': "Congratulations! Consider advanced grammar exercises",
                    'confidence_level': 'high',
                    'estimated_difficulty': 'expert'
                }
        else:
            # Determine if student should retry or review previous levels
            recent_attempts = QuizAttempt.query.filter_by(
                user_id=user_id,
                level_id=attempt.level_id
            ).order_by(QuizAttempt.created_at.desc()).limit(3).all()
            
            if len(recent_attempts) >= 3 and all(not a.passed for a in recent_attempts):
                return {
                    'next_action': 'review_previous',
                    'recommendation': f"Review Level {max(1, level_num - 1)} before retrying",
                    'confidence_level': 'low',
                    'estimated_difficulty': 'challenging'
                }
            else:
                return {
                    'next_action': 'retry',
                    'recommendation': f"Practice more and retry Level {level_num}",
                    'confidence_level': 'medium',
                    'estimated_difficulty': 'manageable'
                }

    @staticmethod
    def get_motivation_message(user_id, attempt):
        """Generate personalized motivation messages."""
        user_stats = QuizService.get_quiz_statistics(user_id)
        total_attempts = user_stats['total_attempts']
        
        if attempt.passed:
            messages = [
                "Great job! You're making excellent progress in your English learning journey!",
                "Well done! Your hard work is paying off!",
                "Fantastic! You're building strong grammar skills!",
                "Excellent work! Keep up this great momentum!"
            ]
        else:
            if total_attempts <= 3:
                messages = [
                    "Don't worry! Learning takes time, and you're just getting started!",
                    "Keep going! Every attempt helps you learn something new!",
                    "You're on the right path! Practice makes perfect!"
                ]
            else:
                messages = [
                    "Persistence is key! You're building valuable skills with each attempt!",
                    "Don't give up! Your dedication will lead to success!",
                    "Keep practicing! You're closer to mastery than you think!"
                ]
        
        import random
        return random.choice(messages)

    @staticmethod
    def get_study_recommendations(attempt):
        """Generate specific study material recommendations."""
        level_num = attempt.level.level_number
        percentage = float(attempt.percentage)
        
        recommendations = {
            'focus_areas': [],
            'practice_exercises': [],
            'study_time': '15-20 minutes daily'
        }
        
        if level_num <= 2:
            recommendations['focus_areas'] = [
                'Subject-verb agreement',
                'Basic verb forms (have/has, is/are)',
                'Simple present tense'
            ]
            recommendations['practice_exercises'] = [
                'Fill-in-the-blank exercises with basic verbs',
                'Simple sentence completion tasks',
                'Basic grammar pattern recognition'
            ]
        elif level_num <= 4:
            recommendations['focus_areas'] = [
                'Past and present tense usage',
                'Proper verb form selection',
                'Context-based grammar application'
            ]
            recommendations['practice_exercises'] = [
                'Mixed tense exercises',
                'Context-based verb selection',
                'Sentence transformation practice'
            ]
        else:
            recommendations['focus_areas'] = [
                'Advanced grammar structures',
                'Complex sentence patterns',
                'Nuanced grammar usage'
            ]
            recommendations['practice_exercises'] = [
                'Advanced grammar challenges',
                'Complex sentence analysis',
                'Professional writing practice'
            ]
        
        if percentage < 60:
            recommendations['study_time'] = '25-30 minutes daily'
        
        return recommendations
    
    @staticmethod
    def get_immediate_recommendations(attempt):
        """Generate immediate post-quiz recommendations."""
        if attempt.passed:
            return {
                'action': 'celebrate',
                'message': 'Take a moment to celebrate your success!',
                'next_step': 'Ready for the next challenge when you are!'
            }
        else:
            return {
                'action': 'review',
                'message': 'Review the questions you missed and try again',
                'next_step': 'Practice makes perfect - you can do this!'
            }

    @staticmethod
    def generate_learning_goals(user_id, stats):
        """Generate personalized learning goals based on performance."""
        goals = []
        
        if stats['success_rate'] < 70:
            goals.append({
                'type': 'improvement',
                'target': 'Achieve 70% success rate',
                'timeframe': '2 weeks',
                'action': 'Focus on fundamental concepts'
            })
        
        if stats['highest_unlocked_level'] < 3:
            goals.append({
                'type': 'progression',
                'target': f"Unlock Level {stats['highest_unlocked_level'] + 1}",
                'timeframe': '1 week',
                'action': 'Master current level with consistent high scores'
            })
        
        if stats['total_attempts'] < 10:
            goals.append({
                'type': 'consistency',
                'target': 'Complete 10 total quiz attempts',
                'timeframe': '1 month',
                'action': 'Practice regularly, aim for 2-3 attempts per week'
            })
        
        return goals
    
    @staticmethod
    def get_long_term_recommendations(user_id, attempt):
        """Generate long-term learning recommendations."""
        stats = QuizService.get_quiz_statistics(user_id)
        
        recommendations = []
        
        if stats['average_score'] < 70:
            recommendations.append("Consider spending more time on fundamentals")
            recommendations.append("Set a goal to practice 15 minutes daily")
        
        if stats['total_attempts'] > 10 and stats['success_rate'] < 60:
            recommendations.append("Try different learning strategies")
            recommendations.append("Focus on understanding concepts rather than memorizing")
        
        return {
            'study_plan': recommendations,
            'goals': QuizService.generate_learning_goals(user_id, stats),
            'timeline': '2-4 weeks for significant improvement'
        }

    @staticmethod
    def store_feedback_record(user_id, attempt_id, feedback):
        """Store feedback for historical tracking (placeholder)."""
        # This would store feedback in a dedicated table for future analysis
        # For now, we can extend the QuizAttempt model or create a new Feedback model
        print(f"Storing feedback for user {user_id}, attempt {attempt_id}")
        return True