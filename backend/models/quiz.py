from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.user import db

class QuizLevel(db.Model):
    __tablename__ = 'quiz_levels'
    
    id = db.Column(db.Integer, primary_key=True)
    level_number = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    passing_threshold = db.Column(db.Integer, nullable=False, default=60)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    questions = db.relationship('QuizQuestion', backref='level', lazy=True, cascade="all, delete-orphan")
    attempts = db.relationship('QuizAttempt', backref='level', lazy=True, cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            'id': self.id,
            'level_number': self.level_number,
            'title': self.title,
            'description': self.description,
            'passing_threshold': self.passing_threshold,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class QuizQuestion(db.Model):
    #Model for quiz questions
    __tablename__ = 'quiz_questions'
    
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer, db.ForeignKey('quiz_levels.id'), nullable=False)
    question_number = db.Column(db.Integer, nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(500), nullable=False)
    option_b = db.Column(db.String(500), nullable=False)
    option_c = db.Column(db.String(500), nullable=False)
    option_d = db.Column(db.String(500), nullable=False)
    correct_answer = db.Column(db.Enum('A', 'B', 'C', 'D', name='answer_options'), nullable=False)
    explanation = db.Column(db.Text)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    answers = db.relationship('QuizAnswer', backref='question', lazy=True, cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            'id': self.id,
            'level_id': self.level_id,
            'question_number': self.question_number,
            'question': self.question_text,
            'options': [
                f"A. {self.option_a}",
                f"B. {self.option_b}",
                f"C. {self.option_c}",
                f"D. {self.option_d}"
            ],
            'correct_answer': self.correct_answer,
            'explanation': self.explanation,
            'is_active': self.is_active
        }

class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('quiz_levels.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Numeric(5, 2), nullable=False)
    passed = db.Column(db.Boolean, nullable=False, default=False)
    time_taken = db.Column(db.Integer)  # in seconds
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    answers = db.relationship('QuizAnswer', backref='attempt', lazy=True, cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'level_id': self.level_id,
            'level_number': self.level.level_number if self.level else None,
            'score': self.score,
            'total_questions': self.total_questions,
            'percentage': float(self.percentage),
            'passed': self.passed,
            'time_taken': self.time_taken,
            'started_at': self.started_at.isoformat() if self.started_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class QuizAnswer(db.Model):
    __tablename__ = 'quiz_answers'
    
    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('quiz_attempts.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz_questions.id'), nullable=False)
    selected_answer = db.Column(db.Enum('A', 'B', 'C', 'D', name='answer_options'), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'attempt_id': self.attempt_id,
            'question_id': self.question_id,
            'selected_answer': self.selected_answer,
            'is_correct': self.is_correct,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class UserQuizProgress(db.Model):
    __tablename__ = 'user_quiz_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    highest_unlocked_level = db.Column(db.Integer, nullable=False, default=1)
    total_attempts = db.Column(db.Integer, nullable=False, default=0)
    total_passed = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'highest_unlocked_level': self.highest_unlocked_level,
            'total_attempts': self.total_attempts,
            'total_passed': self.total_passed,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def get_completed_levels(self):
        #Get list of completed levels for this user
        # Get all passed attempts for this user
        passed_attempts = QuizAttempt.query.filter_by(
            user_id=self.user_id, 
            passed=True
        ).all()
        
        completed_levels = list(set([attempt.level.level_number for attempt in passed_attempts]))
        return sorted(completed_levels)