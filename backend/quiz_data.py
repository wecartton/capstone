"""
Quiz data and levels for the web application
"""

# Level 1 questions (easy)
level1_questions = [
    {
        "id": 1,
        "question": "My friend ... a good bicycle",
        "options": ["A. Have", "B. Has", "C. Having", "D. Had"],
        "correct_answer": "B"
    },
    {
        "id": 2,
        "question": "The lesson ... interesting",
        "options": ["A. Look", "B. Looks", "C. Looking", "D. Looked"],
        "correct_answer": "B"
    },
    {
        "id": 3,
        "question": "They always ... ice cream together",
        "options": ["A. Buy", "B. Buys", "C. Buying", "D. Bought"],
        "correct_answer": "A"
    },
    {
        "id": 4,
        "question": "My brother usually ... to school by bicycle",
        "options": ["A. Go", "B. Goes", "C. Going", "D. Gone"],
        "correct_answer": "B"
    },
    {
        "id": 5,
        "question": "This program ... very well",
        "options": ["A. Work", "B. Works", "C. Working", "D. Worked"],
        "correct_answer": "B"
    },
    {
        "id": 6,
        "question": "My friends ... this movie",
        "options": ["A. Like", "B. Likes", "C. Liking", "D. Liked"],
        "correct_answer": "A"
    }
]

# Level 2 questions
level2_questions = [
    {
        "id": 1,
        "question": "Our teacher ... a lot",
        "options": ["A. Know", "B. Knows", "C. Knowing", "D. Known"],
        "correct_answer": "B"
    },
    {
        "id": 2,
        "question": "Your friend always ... very interesting things",
        "options": ["A. Say", "B. Says", "C. Saying", "D. Said"],
        "correct_answer": "B"
    },
    {
        "id": 3,
        "question": "The teachers always ... early",
        "options": ["A. Come", "B. Comes", "C. Coming", "D. Came"],
        "correct_answer": "A"
    },
    {
        "id": 4,
        "question": "It ... interesting",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    },
    {
        "id": 5,
        "question": "She ... very beautiful",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    },
    {
        "id": 6,
        "question": "He ... a student",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    }
]

# Level 3 questions
level3_questions = [
    {
        "id": 1,
        "question": "I ... so happy",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "B"
    },
    {
        "id": 2,
        "question": "They ... our partner",
        "options": ["A. is", "B. am", "C. are", "D. was"],
        "correct_answer": "C"
    },
    {
        "id": 3,
        "question": "We ... at Home yesterday",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "D"
    },
    {
        "id": 4,
        "question": "You ... so talented",
        "options": ["A. is", "B. am", "C. are", "D. was"],
        "correct_answer": "C"
    },
    {
        "id": 5,
        "question": "The news ... surprising",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    },
    {
        "id": 6,
        "question": "This knowledge ... good enough",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    }
]

# Level 4 questions
level4_questions = [
    {
        "id": 1,
        "question": "They say money ... power",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    },
    {
        "id": 2,
        "question": "Your lessons ... so useful last week",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "D"
    },
    {
        "id": 3,
        "question": "The lesson ... really boring yesterday",
        "options": ["A. is", "B. am", "C. are", "D. was"],
        "correct_answer": "D"
    },
    {
        "id": 4,
        "question": "Some people say money ... only paper",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    },
    {
        "id": 5,
        "question": "The computer ... 2000 dollars",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    },
    {
        "id": 6,
        "question": "The news ... really bad last month",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "D"
    }
]

# Level 5 questions (difficult)
level5_questions = [
    {
        "id": 1,
        "question": "The shoes ... new",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "C"
    },
    {
        "id": 2,
        "question": "His progress ... slow",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    },
    {
        "id": 3,
        "question": "Your results ... fantastic",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "C"
    },
    {
        "id": 4,
        "question": "This knowledge ... more than enough",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    },
    {
        "id": 5,
        "question": "The weather ... awful",
        "options": ["A. is", "B. am", "C. are", "D. were"],
        "correct_answer": "A"
    }
]

# Dictionary to access questions by level
quiz_levels = {
    1: level1_questions,
    2: level2_questions,
    3: level3_questions,
    4: level4_questions,
    5: level5_questions
}

# Passing threshold (percentage) for each level
passing_threshold = {
    1: 60,  # 60% to pass level 1
    2: 65,  # 65% to pass level 2
    3: 70,  # 70% to pass level 3
    4: 75,  # 75% to pass level 4
    5: 80   # 80% to pass level 5
}

def get_questions_for_level(level):
    """Get questions for a specific level"""
    if level in quiz_levels:
        return quiz_levels[level]
    return []

def is_passing_score(level, score, total):
    """Check if score meets the passing threshold for a given level"""
    if level in passing_threshold:
        percentage = (score / total) * 100
        return percentage >= passing_threshold[level]
    return False