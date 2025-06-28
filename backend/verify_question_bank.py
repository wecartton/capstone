import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from models.quiz import QuizLevel, QuizQuestion
from models.user import db

def verify_question_bank():
    """Verify each level has enough questions in the bank"""
    app = create_app()
    
    with app.app_context():
        print("=== VERIFYING QUESTION BANK ===")
        print("-" * 40)
        
        levels = QuizLevel.query.filter_by(is_active=True).order_by(QuizLevel.level_number).all()
        
        all_good = True
        
        for level in levels:
            # Count active questions for this level
            question_count = QuizQuestion.query.filter_by(
                level_id=level.id,
                is_active=True
            ).count()
            
            print(f"Level {level.level_number} - {level.title}:")
            print(f"  Total questions: {question_count}")
            
            if question_count < 30:
                print(f"  ⚠️  WARNING: Not enough questions! Need at least 30, have {question_count}")
                all_good = False
            elif question_count < 60:
                print(f"  ⚠️  NOTICE: Less than full bank (60). Random selection limited.")
            else:
                print(f"  ✓ Question bank OK")
            
            print()
        
        print("-" * 40)
        if all_good:
            print("✓ All levels have sufficient questions for quiz mode (30 questions)")
        else:
            print("✗ Some levels need more questions added to the bank")
        
        # Test random selection
        print("\n=== TESTING RANDOM SELECTION ===")
        test_level = 1
        
        from services.quiz_service import QuizService
        
        # Get 3 random sets to verify randomness
        sets = []
        for i in range(3):
            _, questions = QuizService.get_random_questions_subset(test_level, 30)
            if questions:
                question_ids = [q['id'] for q in questions]
                sets.append(set(question_ids))
                print(f"Set {i+1}: {len(questions)} questions selected")
        
        # Check if sets are different
        if len(sets) == 3:
            common_questions = sets[0] & sets[1] & sets[2]
            print(f"\nCommon questions in all 3 sets: {len(common_questions)}")
            print(f"This shows randomization is working!" if len(common_questions) < 30 else "Check randomization!")

if __name__ == "__main__":
    verify_question_bank()