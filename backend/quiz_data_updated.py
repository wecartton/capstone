"""
Updated Quiz data with 60 questions per level (300 total questions)
Organized by difficulty: Beginner, Lower-Intermediate, Intermediate, Upper-Intermediate, Expert
"""

# LEVEL 1 - BEGINNER (60 questions)
# Focus: Basic vocabulary, simple grammar, simple present, to be, articles, sentence completion
level1_questions = [
    # Basic Vocabulary - Colors (1-10)
    {
        "id": 1,
        "question": "What color is the sun?",
        "options": ["A. Blue", "B. Yellow", "C. Green", "D. Red"],
        "correct_answer": "B"
    },
    {
        "id": 2,
        "question": "The grass is ...",
        "options": ["A. green", "B. blue", "C. red", "D. yellow"],
        "correct_answer": "A"
    },
    {
        "id": 3,
        "question": "An apple is usually ...",
        "options": ["A. blue", "B. purple", "C. red", "D. black"],
        "correct_answer": "C"
    },
    {
        "id": 4,
        "question": "The sky is ...",
        "options": ["A. green", "B. blue", "C. orange", "D. purple"],
        "correct_answer": "B"
    },
    {
        "id": 5,
        "question": "Snow is ...",
        "options": ["A. black", "B. brown", "C. white", "D. pink"],
        "correct_answer": "C"
    },
    {
        "id": 6,
        "question": "What color do you get when you mix red and yellow?",
        "options": ["A. Purple", "B. Orange", "C. Green", "D. Blue"],
        "correct_answer": "B"
    },
    {
        "id": 7,
        "question": "A banana is ...",
        "options": ["A. yellow", "B. purple", "C. blue", "D. green"],
        "correct_answer": "A"
    },
    {
        "id": 8,
        "question": "What color is chocolate?",
        "options": ["A. White", "B. Yellow", "C. Brown", "D. Pink"],
        "correct_answer": "C"
    },
    {
        "id": 9,
        "question": "Roses are often ...",
        "options": ["A. blue", "B. red", "C. black", "D. gray"],
        "correct_answer": "B"
    },
    {
        "id": 10,
        "question": "The color of night is ...",
        "options": ["A. white", "B. yellow", "C. black", "D. pink"],
        "correct_answer": "C"
    },
    
    # Jobs and Professions (11-20)
    {
        "id": 11,
        "question": "A person who teaches students is a ...",
        "options": ["A. doctor", "B. teacher", "C. driver", "D. cook"],
        "correct_answer": "B"
    },
    {
        "id": 12,
        "question": "A person who helps sick people is a ...",
        "options": ["A. teacher", "B. driver", "C. doctor", "D. student"],
        "correct_answer": "C"
    },
    {
        "id": 13,
        "question": "A person who drives a car for work is a ...",
        "options": ["A. driver", "B. teacher", "C. cook", "D. nurse"],
        "correct_answer": "A"
    },
    {
        "id": 14,
        "question": "A person who makes food is a ...",
        "options": ["A. doctor", "B. driver", "C. teacher", "D. cook"],
        "correct_answer": "D"
    },
    {
        "id": 15,
        "question": "A person who helps doctors is a ...",
        "options": ["A. student", "B. nurse", "C. driver", "D. cook"],
        "correct_answer": "B"
    },
    {
        "id": 16,
        "question": "A person who sells things in a store is a ...",
        "options": ["A. seller", "B. buyer", "C. teacher", "D. doctor"],
        "correct_answer": "A"
    },
    {
        "id": 17,
        "question": "A person who cuts hair is a ...",
        "options": ["A. teacher", "B. hairdresser", "C. cook", "D. driver"],
        "correct_answer": "B"
    },
    {
        "id": 18,
        "question": "A person who works in a hospital and helps patients is a ...",
        "options": ["A. teacher", "B. cook", "C. nurse", "D. driver"],
        "correct_answer": "C"
    },
    {
        "id": 19,
        "question": "A person who learns at school is a ...",
        "options": ["A. teacher", "B. student", "C. doctor", "D. nurse"],
        "correct_answer": "B"
    },
    {
        "id": 20,
        "question": "A person who flies airplanes is a ...",
        "options": ["A. driver", "B. sailor", "C. pilot", "D. teacher"],
        "correct_answer": "C"
    },
    
    # Daily Activities (21-30)
    {
        "id": 21,
        "question": "I ... breakfast every morning.",
        "options": ["A. eat", "B. sleep", "C. run", "D. study"],
        "correct_answer": "A"
    },
    {
        "id": 22,
        "question": "She ... to school by bus.",
        "options": ["A. go", "B. goes", "C. going", "D. gone"],
        "correct_answer": "B"
    },
    {
        "id": 23,
        "question": "We ... our teeth before bed.",
        "options": ["A. wash", "B. brush", "C. eat", "D. drink"],
        "correct_answer": "B"
    },
    {
        "id": 24,
        "question": "He ... television in the evening.",
        "options": ["A. watch", "B. watches", "C. watching", "D. watched"],
        "correct_answer": "B"
    },
    {
        "id": 25,
        "question": "They ... homework after school.",
        "options": ["A. do", "B. does", "C. doing", "D. did"],
        "correct_answer": "A"
    },
    {
        "id": 26,
        "question": "I ... up at 7 o'clock every day.",
        "options": ["A. get", "B. gets", "C. getting", "D. got"],
        "correct_answer": "A"
    },
    {
        "id": 27,
        "question": "My mother ... dinner for the family.",
        "options": ["A. cook", "B. cooks", "C. cooking", "D. cooked"],
        "correct_answer": "B"
    },
    {
        "id": 28,
        "question": "We ... to bed at 10 PM.",
        "options": ["A. go", "B. goes", "C. going", "D. gone"],
        "correct_answer": "A"
    },
    {
        "id": 29,
        "question": "She ... a shower every morning.",
        "options": ["A. take", "B. takes", "C. taking", "D. took"],
        "correct_answer": "B"
    },
    {
        "id": 30,
        "question": "I ... my hands before eating.",
        "options": ["A. wash", "B. washes", "C. washing", "D. washed"],
        "correct_answer": "A"
    },
    
    # Grammar - To Be (31-40)
    {
        "id": 31,
        "question": "I ... a student.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "A"
    },
    {
        "id": 32,
        "question": "She ... my sister.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "B"
    },
    {
        "id": 33,
        "question": "They ... happy today.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "C"
    },
    {
        "id": 34,
        "question": "The cat ... sleeping.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "B"
    },
    {
        "id": 35,
        "question": "We ... friends.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "C"
    },
    {
        "id": 36,
        "question": "You ... very kind.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "C"
    },
    {
        "id": 37,
        "question": "The book ... on the table.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "B"
    },
    {
        "id": 38,
        "question": "My parents ... at home.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "C"
    },
    {
        "id": 39,
        "question": "The weather ... nice today.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "B"
    },
    {
        "id": 40,
        "question": "These flowers ... beautiful.",
        "options": ["A. am", "B. is", "C. are", "D. be"],
        "correct_answer": "C"
    },
    
    # Articles a/an/the (41-50)
    {
        "id": 41,
        "question": "I want to buy ... apple.",
        "options": ["A. a", "B. an", "C. the", "D. -"],
        "correct_answer": "B"
    },
    {
        "id": 42,
        "question": "She has ... cat.",
        "options": ["A. a", "B. an", "C. the", "D. -"],
        "correct_answer": "A"
    },
    {
        "id": 43,
        "question": "... sun is bright today.",
        "options": ["A. A", "B. An", "C. The", "D. -"],
        "correct_answer": "C"
    },
    {
        "id": 44,
        "question": "I need ... umbrella.",
        "options": ["A. a", "B. an", "C. the", "D. -"],
        "correct_answer": "B"
    },
    {
        "id": 45,
        "question": "There is ... dog in the garden.",
        "options": ["A. a", "B. an", "C. the", "D. -"],
        "correct_answer": "A"
    },
    {
        "id": 46,
        "question": "... moon is beautiful tonight.",
        "options": ["A. A", "B. An", "C. The", "D. -"],
        "correct_answer": "C"
    },
    {
        "id": 47,
        "question": "He is ... honest person.",
        "options": ["A. a", "B. an", "C. the", "D. -"],
        "correct_answer": "B"
    },
    {
        "id": 48,
        "question": "I live in ... house with a red door.",
        "options": ["A. a", "B. an", "C. the", "D. -"],
        "correct_answer": "A"
    },
    {
        "id": 49,
        "question": "Can you pass me ... salt, please?",
        "options": ["A. a", "B. an", "C. the", "D. -"],
        "correct_answer": "C"
    },
    {
        "id": 50,
        "question": "She wants to be ... engineer.",
        "options": ["A. a", "B. an", "C. the", "D. -"],
        "correct_answer": "B"
    },
    
    # Simple Present & Sentence Completion (51-60)
    {
        "id": 51,
        "question": "My brother ... football every weekend.",
        "options": ["A. play", "B. plays", "C. playing", "D. played"],
        "correct_answer": "B"
    },
    {
        "id": 52,
        "question": "The children ... in the park.",
        "options": ["A. play", "B. plays", "C. playing", "D. played"],
        "correct_answer": "A"
    },
    {
        "id": 53,
        "question": "Water ... at 100 degrees Celsius.",
        "options": ["A. boil", "B. boils", "C. boiling", "D. boiled"],
        "correct_answer": "B"
    },
    {
        "id": 54,
        "question": "She ... English and French.",
        "options": ["A. speak", "B. speaks", "C. speaking", "D. spoke"],
        "correct_answer": "B"
    },
    {
        "id": 55,
        "question": "The train ... at 8:30 AM.",
        "options": ["A. leave", "B. leaves", "C. leaving", "D. left"],
        "correct_answer": "B"
    },
    {
        "id": 56,
        "question": "I ... coffee in the morning.",
        "options": ["A. drink", "B. drinks", "C. drinking", "D. drank"],
        "correct_answer": "A"
    },
    {
        "id": 57,
        "question": "The shop ... at 9 AM every day.",
        "options": ["A. open", "B. opens", "C. opening", "D. opened"],
        "correct_answer": "B"
    },
    {
        "id": 58,
        "question": "We ... our grandmother on Sundays.",
        "options": ["A. visit", "B. visits", "C. visiting", "D. visited"],
        "correct_answer": "A"
    },
    {
        "id": 59,
        "question": "The baby ... a lot.",
        "options": ["A. cry", "B. cries", "C. crying", "D. cried"],
        "correct_answer": "B"
    },
    {
        "id": 60,
        "question": "Birds ... in the sky.",
        "options": ["A. fly", "B. flies", "C. flying", "D. flew"],
        "correct_answer": "A"
    }
]

# LEVEL 2 - LOWER-INTERMEDIATE (60 questions)
# Focus: Tenses, complex daily vocabulary, reading short paragraphs, error correction, functional language
level2_questions = [
    # Present Perfect vs Past Simple (1-15)
    {
        "id": 1,
        "question": "I ... to Paris three times.",
        "options": ["A. went", "B. have been", "C. go", "D. am going"],
        "correct_answer": "B"
    },
    {
        "id": 2,
        "question": "She ... her homework yesterday.",
        "options": ["A. has finished", "B. finished", "C. finishes", "D. is finishing"],
        "correct_answer": "B"
    },
    {
        "id": 3,
        "question": "We ... this movie before.",
        "options": ["A. saw", "B. see", "C. have seen", "D. are seeing"],
        "correct_answer": "C"
    },
    {
        "id": 4,
        "question": "He ... his keys. He can't find them.",
        "options": ["A. lost", "B. has lost", "C. loses", "D. is losing"],
        "correct_answer": "B"
    },
    {
        "id": 5,
        "question": "They ... to the concert last night.",
        "options": ["A. have gone", "B. went", "C. go", "D. are going"],
        "correct_answer": "B"
    },
    {
        "id": 6,
        "question": "I ... never ... sushi before.",
        "options": ["A. did / eat", "B. have / eaten", "C. do / eat", "D. am / eating"],
        "correct_answer": "B"
    },
    {
        "id": 7,
        "question": "She ... her sister two hours ago.",
        "options": ["A. has called", "B. called", "C. calls", "D. is calling"],
        "correct_answer": "B"
    },
    {
        "id": 8,
        "question": "We ... here since 2010.",
        "options": ["A. lived", "B. live", "C. have lived", "D. are living"],
        "correct_answer": "C"
    },
    {
        "id": 9,
        "question": "The train ... just ...",
        "options": ["A. did / arrive", "B. has / arrived", "C. does / arrive", "D. is / arriving"],
        "correct_answer": "B"
    },
    {
        "id": 10,
        "question": "I ... my car last week.",
        "options": ["A. have sold", "B. sold", "C. sell", "D. am selling"],
        "correct_answer": "B"
    },
    {
        "id": 11,
        "question": "... you ever ... to Japan?",
        "options": ["A. Did / go", "B. Have / been", "C. Do / go", "D. Are / going"],
        "correct_answer": "B"
    },
    {
        "id": 12,
        "question": "My parents ... married for 25 years.",
        "options": ["A. were", "B. are", "C. have been", "D. will be"],
        "correct_answer": "C"
    },
    {
        "id": 13,
        "question": "She ... the book last month.",
        "options": ["A. has read", "B. read", "C. reads", "D. is reading"],
        "correct_answer": "B"
    },
    {
        "id": 14,
        "question": "I ... him since childhood.",
        "options": ["A. knew", "B. know", "C. have known", "D. am knowing"],
        "correct_answer": "C"
    },
    {
        "id": 15,
        "question": "They ... the meeting yesterday.",
        "options": ["A. have attended", "B. attended", "C. attend", "D. are attending"],
        "correct_answer": "B"
    },
    
    # Past Simple vs Past Continuous (16-25)
    {
        "id": 16,
        "question": "I ... TV when the phone rang.",
        "options": ["A. watched", "B. was watching", "C. watch", "D. am watching"],
        "correct_answer": "B"
    },
    {
        "id": 17,
        "question": "She ... while I ... cooking.",
        "options": ["A. studied / was", "B. was studying / was", "C. studied / cooked", "D. was studying / cooked"],
        "correct_answer": "B"
    },
    {
        "id": 18,
        "question": "What ... you ... at 8 PM yesterday?",
        "options": ["A. did / do", "B. were / doing", "C. do / do", "D. are / doing"],
        "correct_answer": "B"
    },
    {
        "id": 19,
        "question": "It ... heavily when we left the house.",
        "options": ["A. rained", "B. was raining", "C. rains", "D. is raining"],
        "correct_answer": "B"
    },
    {
        "id": 20,
        "question": "The children ... in the garden when their mother called them.",
        "options": ["A. played", "B. were playing", "C. play", "D. are playing"],
        "correct_answer": "B"
    },
    {
        "id": 21,
        "question": "I ... my homework when you arrived.",
        "options": ["A. finished", "B. was finishing", "C. finish", "D. am finishing"],
        "correct_answer": "B"
    },
    {
        "id": 22,
        "question": "We ... dinner at 7 PM last night.",
        "options": ["A. had", "B. were having", "C. have", "D. are having"],
        "correct_answer": "A"
    },
    {
        "id": 23,
        "question": "While she ..., the doorbell rang.",
        "options": ["A. slept", "B. was sleeping", "C. sleeps", "D. is sleeping"],
        "correct_answer": "B"
    },
    {
        "id": 24,
        "question": "They ... a movie when the lights went out.",
        "options": ["A. watched", "B. were watching", "C. watch", "D. are watching"],
        "correct_answer": "B"
    },
    {
        "id": 25,
        "question": "He ... to work by car yesterday.",
        "options": ["A. went", "B. was going", "C. goes", "D. is going"],
        "correct_answer": "A"
    },
    
    # Travel Vocabulary (26-35)
    {
        "id": 26,
        "question": "You need a ... to travel to another country.",
        "options": ["A. ticket", "B. passport", "C. suitcase", "D. map"],
        "correct_answer": "B"
    },
    {
        "id": 27,
        "question": "The plane will ... at gate 15.",
        "options": ["A. depart", "B. arrive", "C. land", "D. take off"],
        "correct_answer": "A"
    },
    {
        "id": 28,
        "question": "I need to ... my hotel room for tomorrow night.",
        "options": ["A. book", "B. check", "C. cancel", "D. leave"],
        "correct_answer": "A"
    },
    {
        "id": 29,
        "question": "The ... was very comfortable during the long flight.",
        "options": ["A. seat", "B. window", "C. door", "D. table"],
        "correct_answer": "A"
    },
    {
        "id": 30,
        "question": "We had to go through ... at the airport.",
        "options": ["A. security", "B. restaurant", "C. shop", "D. toilet"],
        "correct_answer": "A"
    },
    {
        "id": 31,
        "question": "The ... helped us find our way around the city.",
        "options": ["A. book", "B. map", "C. phone", "D. car"],
        "correct_answer": "B"
    },
    {
        "id": 32,
        "question": "Our flight was ... by two hours due to bad weather.",
        "options": ["A. delayed", "B. canceled", "C. early", "D. fast"],
        "correct_answer": "A"
    },
    {
        "id": 33,
        "question": "I forgot to pack my ... for the beach vacation.",
        "options": ["A. coat", "B. boots", "C. swimsuit", "D. scarf"],
        "correct_answer": "C"
    },
    {
        "id": 34,
        "question": "The hotel offers free ... to the airport.",
        "options": ["A. food", "B. shuttle", "C. room", "D. wifi"],
        "correct_answer": "B"
    },
    {
        "id": 35,
        "question": "Don't forget to ... your boarding pass.",
        "options": ["A. lose", "B. throw", "C. keep", "D. sell"],
        "correct_answer": "C"
    },
    
    # Work and Emotions Vocabulary (36-45)
    {
        "id": 36,
        "question": "My boss gave me a ... for my good work.",
        "options": ["A. punishment", "B. promotion", "C. problem", "D. pain"],
        "correct_answer": "B"
    },
    {
        "id": 37,
        "question": "I feel ... when I have too much work to do.",
        "options": ["A. relaxed", "B. happy", "C. stressed", "D. excited"],
        "correct_answer": "C"
    },
    {
        "id": 38,
        "question": "She was ... about getting the new job.",
        "options": ["A. worried", "B. excited", "C. angry", "D. sad"],
        "correct_answer": "B"
    },
    {
        "id": 39,
        "question": "The meeting has been ... to next week.",
        "options": ["A. canceled", "B. finished", "C. postponed", "D. started"],
        "correct_answer": "C"
    },
    {
        "id": 40,
        "question": "I need to ... the deadline for this project.",
        "options": ["A. meet", "B. lose", "C. forget", "D. ignore"],
        "correct_answer": "A"
    },
    {
        "id": 41,
        "question": "He feels ... because he lost his job.",
        "options": ["A. happy", "B. excited", "C. depressed", "D. proud"],
        "correct_answer": "C"
    },
    {
        "id": 42,
        "question": "I'm ... about the exam results.",
        "options": ["A. confident", "B. nervous", "C. angry", "D. sleepy"],
        "correct_answer": "B"
    },
    {
        "id": 43,
        "question": "She was ... when she heard the good news.",
        "options": ["A. disappointed", "B. worried", "C. thrilled", "D. confused"],
        "correct_answer": "C"
    },
    {
        "id": 44,
        "question": "My colleague is very ... and always helps others.",
        "options": ["A. selfish", "B. helpful", "C. rude", "D. lazy"],
        "correct_answer": "B"
    },
    {
        "id": 45,
        "question": "I'm ... that I made the right decision.",
        "options": ["A. doubtful", "B. uncertain", "C. confident", "D. worried"],
        "correct_answer": "C"
    },
    
    # Functional Language (46-55)
    {
        "id": 46,
        "question": "A: I have a headache. B: You ... take some medicine.",
        "options": ["A. must", "B. should", "C. can", "D. will"],
        "correct_answer": "B"
    },
    {
        "id": 47,
        "question": "Would you like to ... to the movies tonight?",
        "options": ["A. go", "B. going", "C. went", "D. gone"],
        "correct_answer": "A"
    },
    {
        "id": 48,
        "question": "I'm sorry, but I ... come to your party.",
        "options": ["A. can", "B. can't", "C. must", "D. should"],
        "correct_answer": "B"
    },
    {
        "id": 49,
        "question": "... you help me with this problem?",
        "options": ["A. Can", "B. Must", "C. Should", "D. Will"],
        "correct_answer": "A"
    },
    {
        "id": 50,
        "question": "I ... you should talk to your teacher about this.",
        "options": ["A. think", "B. know", "C. hope", "D. want"],
        "correct_answer": "A"
    },
    {
        "id": 51,
        "question": "... don't we go for a walk?",
        "options": ["A. What", "B. Why", "C. How", "D. When"],
        "correct_answer": "B"
    },
    {
        "id": 52,
        "question": "I'd like to ... an appointment with the doctor.",
        "options": ["A. make", "B. do", "C. take", "D. have"],
        "correct_answer": "A"
    },
    {
        "id": 53,
        "question": "Could you ... me a favor?",
        "options": ["A. make", "B. do", "C. give", "D. take"],
        "correct_answer": "B"
    },
    {
        "id": 54,
        "question": "I'm afraid I ... agree with you.",
        "options": ["A. can", "B. can't", "C. must", "D. should"],
        "correct_answer": "B"
    },
    {
        "id": 55,
        "question": "... about meeting for lunch tomorrow?",
        "options": ["A. What", "B. How", "C. Why", "D. When"],
        "correct_answer": "B"
    },
    
    # Error Correction (56-60)
    {
        "id": 56,
        "question": "Choose the correct sentence:",
        "options": ["A. She don't like coffee.", "B. She doesn't like coffee.", "C. She not like coffee.", "D. She no like coffee."],
        "correct_answer": "B"
    },
    {
        "id": 57,
        "question": "Choose the correct sentence:",
        "options": ["A. I am going to home.", "B. I am going home.", "C. I am going to the home.", "D. I going home."],
        "correct_answer": "B"
    },
    {
        "id": 58,
        "question": "Choose the correct sentence:",
        "options": ["A. He have been there before.", "B. He has been there before.", "C. He have been their before.", "D. He has been their before."],
        "correct_answer": "B"
    },
    {
        "id": 59,
        "question": "Choose the correct sentence:",
        "options": ["A. There is many people here.", "B. There are much people here.", "C. There are many people here.", "D. There is much people here."],
        "correct_answer": "C"
    },
    {
        "id": 60,
        "question": "Choose the correct sentence:",
        "options": ["A. I'm looking forward to see you.", "B. I'm looking forward to seeing you.", "C. I'm looking forward see you.", "D. I'm looking forward for see you."],
        "correct_answer": "B"
    }
]

# LEVEL 3 - INTERMEDIATE (60 questions)
# Focus: Conditionals, relative clauses, passive voice, academic vocabulary, idioms, paraphrasing
level3_questions = [
    # Conditionals (1-15)
    {
        "id": 1,
        "question": "If it rains tomorrow, we ... stay at home.",
        "options": ["A. will", "B. would", "C. could", "D. should"],
        "correct_answer": "A"
    },
    {
        "id": 2,
        "question": "If I ... you, I would apply for that job.",
        "options": ["A. am", "B. was", "C. were", "D. be"],
        "correct_answer": "C"
    },
    {
        "id": 3,
        "question": "She would have passed the exam if she ... harder.",
        "options": ["A. studied", "B. had studied", "C. studies", "D. would study"],
        "correct_answer": "B"
    },
    {
        "id": 4,
        "question": "If you heat water to 100°C, it ...",
        "options": ["A. will boil", "B. would boil", "C. boils", "D. boiled"],
        "correct_answer": "C"
    },
    {
        "id": 5,
        "question": "If I had known about the party, I ... come.",
        "options": ["A. will", "B. would", "C. would have", "D. had"],
        "correct_answer": "C"
    },
    {
        "id": 6,
        "question": "Unless you hurry, you ... miss the train.",
        "options": ["A. will", "B. would", "C. could", "D. might"],
        "correct_answer": "A"
    },
    {
        "id": 7,
        "question": "If she ... more time, she could finish the project.",
        "options": ["A. has", "B. had", "C. have", "D. would have"],
        "correct_answer": "B"
    },
    {
        "id": 8,
        "question": "What would you do if you ... a million dollars?",
        "options": ["A. win", "B. won", "C. would win", "D. will win"],
        "correct_answer": "B"
    },
    {
        "id": 9,
        "question": "If you don't study, you ... fail the test.",
        "options": ["A. will", "B. would", "C. could", "D. should"],
        "correct_answer": "A"
    },
    {
        "id": 10,
        "question": "I ... help you if I wasn't so busy.",
        "options": ["A. will", "B. would", "C. can", "D. could"],
        "correct_answer": "B"
    },
    {
        "id": 11,
        "question": "If it ... sunny, we would go to the beach.",
        "options": ["A. is", "B. was", "C. were", "D. will be"],
        "correct_answer": "C"
    },
    {
        "id": 12,
        "question": "She wouldn't have been late if she ... earlier.",
        "options": ["A. left", "B. had left", "C. leaves", "D. would leave"],
        "correct_answer": "B"
    },
    {
        "id": 13,
        "question": "If you mix red and blue, you ... purple.",
        "options": ["A. will get", "B. would get", "C. get", "D. got"],
        "correct_answer": "C"
    },
    {
        "id": 14,
        "question": "I would buy a new car if I ... enough money.",
        "options": ["A. have", "B. had", "C. will have", "D. would have"],
        "correct_answer": "B"
    },
    {
        "id": 15,
        "question": "If they had invited me, I ... to their wedding.",
        "options": ["A. will go", "B. would go", "C. would have gone", "D. had gone"],
        "correct_answer": "C"
    },
    
    # Relative Clauses (16-25)
    {
        "id": 16,
        "question": "The book ... I read yesterday was fascinating.",
        "options": ["A. who", "B. which", "C. where", "D. when"],
        "correct_answer": "B"
    },
    {
        "id": 17,
        "question": "The woman ... lives next door is a teacher.",
        "options": ["A. who", "B. which", "C. where", "D. whose"],
        "correct_answer": "A"
    },
    {
        "id": 18,
        "question": "This is the house ... I was born.",
        "options": ["A. which", "B. where", "C. who", "D. when"],
        "correct_answer": "B"
    },
    {
        "id": 19,
        "question": "The man ... car was stolen called the police.",
        "options": ["A. who", "B. which", "C. whose", "D. where"],
        "correct_answer": "C"
    },
    {
        "id": 20,
        "question": "I remember the day ... we first met.",
        "options": ["A. who", "B. which", "C. where", "D. when"],
        "correct_answer": "D"
    },
    {
        "id": 21,
        "question": "The students ... passed the exam will graduate.",
        "options": ["A. who", "B. which", "C. where", "D. whose"],
        "correct_answer": "A"
    },
    {
        "id": 22,
        "question": "The city ... we visited was beautiful.",
        "options": ["A. who", "B. which", "C. where", "D. when"],
        "correct_answer": "B"
    },
    {
        "id": 23,
        "question": "The restaurant ... we had dinner serves excellent food.",
        "options": ["A. which", "B. where", "C. who", "D. when"],
        "correct_answer": "B"
    },
    {
        "id": 24,
        "question": "The girl ... bag was stolen reported it to security.",
        "options": ["A. who", "B. which", "C. whose", "D. where"],
        "correct_answer": "C"
    },
    {
        "id": 25,
        "question": "The movie ... we watched last night was boring.",
        "options": ["A. who", "B. which", "C. where", "D. when"],
        "correct_answer": "B"
    },
    
    # Passive Voice (26-35)
    {
        "id": 26,
        "question": "The letter ... by John yesterday.",
        "options": ["A. was written", "B. wrote", "C. is written", "D. writes"],
        "correct_answer": "A"
    },
    {
        "id": 27,
        "question": "English ... all over the world.",
        "options": ["A. speaks", "B. is spoken", "C. spoke", "D. was spoken"],
        "correct_answer": "B"
    },
    {
        "id": 28,
        "question": "The house ... last year.",
        "options": ["A. built", "B. builds", "C. was built", "D. is built"],
        "correct_answer": "C"
    },
    {
        "id": 29,
        "question": "The problem ... by the experts tomorrow.",
        "options": ["A. will solve", "B. will be solved", "C. solves", "D. is solved"],
        "correct_answer": "B"
    },
    {
        "id": 30,
        "question": "The car ... by a professional mechanic.",
        "options": ["A. repaired", "B. repairs", "C. was repaired", "D. is repairing"],
        "correct_answer": "C"
    },
    {
        "id": 31,
        "question": "The cake ... by my grandmother.",
        "options": ["A. made", "B. makes", "C. was made", "D. is making"],
        "correct_answer": "C"
    },
    {
        "id": 32,
        "question": "The windows ... every week.",
        "options": ["A. clean", "B. are cleaned", "C. cleaned", "D. were cleaned"],
        "correct_answer": "B"
    },
    {
        "id": 33,
        "question": "The report ... by the deadline.",
        "options": ["A. will finish", "B. will be finished", "C. finishes", "D. finished"],
        "correct_answer": "B"
    },
    {
        "id": 34,
        "question": "The documents ... to the manager.",
        "options": ["A. sent", "B. send", "C. were sent", "D. are sending"],
        "correct_answer": "C"
    },
    {
        "id": 35,
        "question": "The meeting ... due to bad weather.",
        "options": ["A. canceled", "B. cancels", "C. was canceled", "D. is canceling"],
        "correct_answer": "C"
    },
    
    # Academic Vocabulary (36-45)
    {
        "id": 36,
        "question": "The research ... important findings about climate change.",
        "options": ["A. revealed", "B. hid", "C. ignored", "D. forgot"],
        "correct_answer": "A"
    },
    {
        "id": 37,
        "question": "Scientists need to ... their theories with evidence.",
        "options": ["A. ignore", "B. support", "C. hide", "D. forget"],
        "correct_answer": "B"
    },
    {
        "id": 38,
        "question": "The study ... the relationship between diet and health.",
        "options": ["A. examined", "B. ignored", "C. avoided", "D. forgot"],
        "correct_answer": "A"
    },
    {
        "id": 39,
        "question": "The professor ... the complex theory to the students.",
        "options": ["A. confused", "B. explained", "C. hid", "D. forgot"],
        "correct_answer": "B"
    },
    {
        "id": 40,
        "question": "The data ... a clear pattern in student performance.",
        "options": ["A. hid", "B. confused", "C. indicated", "D. ignored"],
        "correct_answer": "C"
    },
    {
        "id": 41,
        "question": "Researchers ... various methods to collect information.",
        "options": ["A. avoided", "B. employed", "C. ignored", "D. forgot"],
        "correct_answer": "B"
    },
    {
        "id": 42,
        "question": "The experiment ... the hypothesis proposed by the team.",
        "options": ["A. ignored", "B. confused", "C. confirmed", "D. forgot"],
        "correct_answer": "C"
    },
    {
        "id": 43,
        "question": "The article ... several important points about education.",
        "options": ["A. ignored", "B. highlighted", "C. hid", "D. confused"],
        "correct_answer": "B"
    },
    {
        "id": 44,
        "question": "Students must ... critical thinking skills.",
        "options": ["A. avoid", "B. ignore", "C. develop", "D. forget"],
        "correct_answer": "C"
    },
    {
        "id": 45,
        "question": "The conclusion ... from the research findings.",
        "options": ["A. derived", "B. avoided", "C. ignored", "D. confused"],
        "correct_answer": "A"
    },
    
    # Idioms and Collocations (46-55)
    {
        "id": 46,
        "question": "It's raining cats and dogs means it's raining ...",
        "options": ["A. lightly", "B. heavily", "C. slowly", "D. quietly"],
        "correct_answer": "B"
    },
    {
        "id": 47,
        "question": "I need to ... a decision about my future career.",
        "options": ["A. do", "B. make", "C. take", "D. have"],
        "correct_answer": "B"
    },
    {
        "id": 48,
        "question": "She has a ... for languages and speaks five fluently.",
        "options": ["A. gift", "B. problem", "C. fear", "D. hate"],
        "correct_answer": "A"
    },
    {
        "id": 49,
        "question": "Don't worry, it's a piece of cake means it's ...",
        "options": ["A. difficult", "B. easy", "C. expensive", "D. dangerous"],
        "correct_answer": "B"
    },
    {
        "id": 50,
        "question": "Let's ... time and go by train instead of driving.",
        "options": ["A. waste", "B. lose", "C. save", "D. spend"],
        "correct_answer": "C"
    },
    {
        "id": 51,
        "question": "Break a leg! means ...",
        "options": ["A. Be careful", "B. Good luck", "C. Hurry up", "D. Sit down"],
        "correct_answer": "B"
    },
    {
        "id": 52,
        "question": "I want to ... my English skills this year.",
        "options": ["A. worsen", "B. ignore", "C. improve", "D. forget"],
        "correct_answer": "C"
    },
    {
        "id": 53,
        "question": "He's feeling under the weather means he's ...",
        "options": ["A. happy", "B. excited", "C. sick", "D. angry"],
        "correct_answer": "C"
    },
    {
        "id": 54,
        "question": "Please ... attention to the instructions.",
        "options": ["A. give", "B. pay", "C. take", "D. make"],
        "correct_answer": "B"
    },
    {
        "id": 55,
        "question": "Time flies means time ...",
        "options": ["A. stops", "B. passes slowly", "C. passes quickly", "D. goes backwards"],
        "correct_answer": "C"
    },
    
    # Paraphrasing (56-60)
    {
        "id": 56,
        "question": "\"The meeting was postponed.\" Another way to say this is:",
        "options": ["A. The meeting was canceled forever.", "B. The meeting was moved to a later time.", "C. The meeting was moved to an earlier time.", "D. The meeting was successful."],
        "correct_answer": "B"
    },
    {
        "id": 57,
        "question": "\"She's very intelligent.\" A similar meaning is:",
        "options": ["A. She's very stupid.", "B. She's very lazy.", "C. She's very smart.", "D. She's very slow."],
        "correct_answer": "C"
    },
    {
        "id": 58,
        "question": "\"The task is challenging.\" This means the task is:",
        "options": ["A. easy", "B. boring", "C. difficult", "D. quick"],
        "correct_answer": "C"
    },
    {
        "id": 59,
        "question": "\"He arrived promptly.\" This means he arrived:",
        "options": ["A. late", "B. on time", "C. early", "D. never"],
        "correct_answer": "B"
    },
    {
        "id": 60,
        "question": "\"The project was completed successfully.\" Another way to say this is:",
        "options": ["A. The project failed.", "B. The project was abandoned.", "C. The project was finished well.", "D. The project was started."],
        "correct_answer": "C"
    }
]

# LEVEL 4 - UPPER-INTERMEDIATE (60 questions)
# Focus: Reading comprehension, mixed conditionals, reported speech, advanced collocations, phrasal verbs, discourse markers
level4_questions = [
    # Mixed Conditionals (1-10)
    {
        "id": 1,
        "question": "If I had studied medicine, I ... a doctor now.",
        "options": ["A. would be", "B. will be", "C. am", "D. was"],
        "correct_answer": "A"
    },
    {
        "id": 2,
        "question": "If she were more organized, she ... her keys yesterday.",
        "options": ["A. wouldn't lose", "B. wouldn't have lost", "C. won't lose", "D. didn't lose"],
        "correct_answer": "B"
    },
    {
        "id": 3,
        "question": "If he ... harder in school, he would have a better job now.",
        "options": ["A. studied", "B. had studied", "C. studies", "D. would study"],
        "correct_answer": "B"
    },
    {
        "id": 4,
        "question": "If I were you, I ... taken that opportunity.",
        "options": ["A. would", "B. will have", "C. would have", "D. had"],
        "correct_answer": "C"
    },
    {
        "id": 5,
        "question": "If they had more time now, they ... finished the project yesterday.",
        "options": ["A. would finish", "B. would have finished", "C. will finish", "D. finished"],
        "correct_answer": "B"
    },
    {
        "id": 6,
        "question": "If she hadn't moved abroad, she ... still be living here.",
        "options": ["A. would", "B. will", "C. could", "D. should"],
        "correct_answer": "A"
    },
    {
        "id": 7,
        "question": "If I ... rich, I wouldn't have borrowed money last week.",
        "options": ["A. am", "B. was", "C. were", "D. had been"],
        "correct_answer": "C"
    },
    {
        "id": 8,
        "question": "If you had told me the truth, I ... trust you now.",
        "options": ["A. would", "B. will", "C. could", "D. should"],
        "correct_answer": "A"
    },
    {
        "id": 9,
        "question": "If he ... more confident, he would have applied for the promotion.",
        "options": ["A. is", "B. was", "C. were", "D. had been"],
        "correct_answer": "C"
    },
    {
        "id": 10,
        "question": "If I had his phone number now, I ... called him yesterday.",
        "options": ["A. would call", "B. would have called", "C. will call", "D. called"],
        "correct_answer": "B"
    },
    
    # Reported Speech (11-20)
    {
        "id": 11,
        "question": "She said, \"I am tired.\" → She said that she ... tired.",
        "options": ["A. is", "B. was", "C. were", "D. will be"],
        "correct_answer": "B"
    },
    {
        "id": 12,
        "question": "He asked, \"Where do you live?\" → He asked me where I ...",
        "options": ["A. live", "B. lived", "C. living", "D. will live"],
        "correct_answer": "B"
    },
    {
        "id": 13,
        "question": "They said, \"We will come tomorrow.\" → They said they ... the next day.",
        "options": ["A. will come", "B. come", "C. would come", "D. came"],
        "correct_answer": "C"
    },
    {
        "id": 14,
        "question": "She asked, \"Can you help me?\" → She asked if I ... help her.",
        "options": ["A. can", "B. could", "C. will", "D. would"],
        "correct_answer": "B"
    },
    {
        "id": 15,
        "question": "He said, \"I have finished my work.\" → He said he ... his work.",
        "options": ["A. has finished", "B. finished", "C. had finished", "D. will finish"],
        "correct_answer": "C"
    },
    {
        "id": 16,
        "question": "She told me, \"Don't be late.\" → She told me ... late.",
        "options": ["A. don't be", "B. not to be", "C. not being", "D. to not be"],
        "correct_answer": "B"
    },
    {
        "id": 17,
        "question": "They asked, \"Did you see the movie?\" → They asked if I ... the movie.",
        "options": ["A. saw", "B. see", "C. had seen", "D. have seen"],
        "correct_answer": "C"
    },
    {
        "id": 18,
        "question": "He said, \"I was working yesterday.\" → He said he ... the day before.",
        "options": ["A. was working", "B. worked", "C. had been working", "D. is working"],
        "correct_answer": "C"
    },
    {
        "id": 19,
        "question": "She asked, \"What time is it?\" → She asked what time ...",
        "options": ["A. is it", "B. it is", "C. was it", "D. it was"],
        "correct_answer": "D"
    },
    {
        "id": 20,
        "question": "He said, \"I must go now.\" → He said he ... go then.",
        "options": ["A. must", "B. had to", "C. has to", "D. should"],
        "correct_answer": "B"
    },
    
    # Advanced Collocations (21-30)
    {
        "id": 21,
        "question": "The company decided to ... a new marketing strategy.",
        "options": ["A. make", "B. do", "C. implement", "D. create"],
        "correct_answer": "C"
    },
    {
        "id": 22,
        "question": "The evidence strongly ... that he is innocent.",
        "options": ["A. suggests", "B. tells", "C. says", "D. speaks"],
        "correct_answer": "A"
    },
    {
        "id": 23,
        "question": "She has a ... understanding of quantum physics.",
        "options": ["A. deep", "B. high", "C. strong", "D. big"],
        "correct_answer": "A"
    },
    {
        "id": 24,
        "question": "The negotiations ... a successful conclusion.",
        "options": ["A. arrived", "B. reached", "C. got", "D. came"],
        "correct_answer": "B"
    },
    {
        "id": 25,
        "question": "The report ... serious concerns about safety.",
        "options": ["A. lifts", "B. raises", "C. grows", "D. increases"],
        "correct_answer": "B"
    },
    {
        "id": 26,
        "question": "The government plans to ... strict measures against pollution.",
        "options": ["A. take", "B. make", "C. do", "D. create"],
        "correct_answer": "A"
    },
    {
        "id": 27,
        "question": "The new policy will ... into effect next month.",
        "options": ["A. go", "B. come", "C. enter", "D. put"],
        "correct_answer": "B"
    },
    {
        "id": 28,
        "question": "Scientists are working to ... a cure for the disease.",
        "options": ["A. find", "B. discover", "C. develop", "D. create"],
        "correct_answer": "C"
    },
    {
        "id": 29,
        "question": "The committee will ... the proposals carefully.",
        "options": ["A. think", "B. consider", "C. look", "D. see"],
        "correct_answer": "B"
    },
    {
        "id": 30,
        "question": "The team managed to ... the deadline despite difficulties.",
        "options": ["A. meet", "B. reach", "C. achieve", "D. get"],
        "correct_answer": "A"
    },
    
    # Phrasal Verbs (31-40)
    {
        "id": 31,
        "question": "The meeting was ... until next week due to scheduling conflicts.",
        "options": ["A. put off", "B. put on", "C. put up", "D. put down"],
        "correct_answer": "A"
    },
    {
        "id": 32,
        "question": "I need to ... this information before making a decision.",
        "options": ["A. look into", "B. look after", "C. look up", "D. look down"],
        "correct_answer": "A"
    },
    {
        "id": 33,
        "question": "She ... her coat and left the room quickly.",
        "options": ["A. put on", "B. put off", "C. put up", "D. put down"],
        "correct_answer": "A"
    },
    {
        "id": 34,
        "question": "The fire was ... by the emergency services.",
        "options": ["A. put on", "B. put out", "C. put up", "D. put off"],
        "correct_answer": "B"
    },
    {
        "id": 35,
        "question": "I can't ... with his constant complaining anymore.",
        "options": ["A. put up", "B. put down", "C. put off", "D. put on"],
        "correct_answer": "A"
    },
    {
        "id": 36,
        "question": "The company had to ... 50 employees due to budget cuts.",
        "options": ["A. lay off", "B. lay down", "C. lay up", "D. lay out"],
        "correct_answer": "A"
    },
    {
        "id": 37,
        "question": "I ... my old friend at the shopping mall yesterday.",
        "options": ["A. ran into", "B. ran out", "C. ran up", "D. ran down"],
        "correct_answer": "A"
    },
    {
        "id": 38,
        "question": "We need to ... the problem before it gets worse.",
        "options": ["A. sort in", "B. sort out", "C. sort up", "D. sort down"],
        "correct_answer": "B"
    },
    {
        "id": 39,
        "question": "Please ... the volume on the television.",
        "options": ["A. turn up", "B. turn in", "C. turn out", "D. turn over"],
        "correct_answer": "A"
    },
    {
        "id": 40,
        "question": "The project ... to be more successful than expected.",
        "options": ["A. turned in", "B. turned out", "C. turned up", "D. turned over"],
        "correct_answer": "B"
    },
    
    # Discourse Markers and Transition Signals (41-50)
    {
        "id": 41,
        "question": "The weather was terrible. ..., we decided to cancel the picnic.",
        "options": ["A. However", "B. Therefore", "C. Moreover", "D. Nevertheless"],
        "correct_answer": "B"
    },
    {
        "id": 42,
        "question": "She studied hard for the exam. ..., she was nervous about the results.",
        "options": ["A. Therefore", "B. However", "C. Moreover", "D. Furthermore"],
        "correct_answer": "B"
    },
    {
        "id": 43,
        "question": "The project is expensive. ..., it will take a long time to complete.",
        "options": ["A. However", "B. Nevertheless", "C. Furthermore", "D. Therefore"],
        "correct_answer": "C"
    },
    {
        "id": 44,
        "question": "He didn't have much experience. ..., he got the job.",
        "options": ["A. Therefore", "B. Nevertheless", "C. Furthermore", "D. Moreover"],
        "correct_answer": "B"
    },
    {
        "id": 45,
        "question": "... the heavy rain, the concert continued as planned.",
        "options": ["A. Although", "B. Because", "C. Despite", "D. Due to"],
        "correct_answer": "C"
    },
    {
        "id": 46,
        "question": "The team worked hard. ..., they achieved their goals.",
        "options": ["A. In contrast", "B. As a result", "C. However", "D. On the other hand"],
        "correct_answer": "B"
    },
    {
        "id": 47,
        "question": "..., I would like to thank everyone for their support.",
        "options": ["A. In conclusion", "B. However", "C. Therefore", "D. Moreover"],
        "correct_answer": "A"
    },
    {
        "id": 48,
        "question": "The first option is cheaper. ..., the second option offers better quality.",
        "options": ["A. Therefore", "B. Furthermore", "C. On the other hand", "D. As a result"],
        "correct_answer": "C"
    },
    {
        "id": 49,
        "question": "... his young age, he showed remarkable maturity.",
        "options": ["A. Because of", "B. Despite", "C. Due to", "D. Thanks to"],
        "correct_answer": "B"
    },
    {
        "id": 50,
        "question": "The company faced financial difficulties. ..., they managed to survive.",
        "options": ["A. Therefore", "B. As a result", "C. Nonetheless", "D. Furthermore"],
        "correct_answer": "C"
    },
    
    # Inference and Context (51-60)
    {
        "id": 51,
        "question": "\"Sarah's office light is still on at 11 PM.\" This suggests that Sarah is probably:",
        "options": ["A. sleeping", "B. working late", "C. on vacation", "D. at home"],
        "correct_answer": "B"
    },
    {
        "id": 52,
        "question": "\"The restaurant was packed and there was a long queue outside.\" This implies the restaurant is:",
        "options": ["A. unpopular", "B. closed", "C. very popular", "D. expensive"],
        "correct_answer": "C"
    },
    {
        "id": 53,
        "question": "\"He kept checking his watch during the presentation.\" This suggests he was:",
        "options": ["A. interested", "B. bored or anxious", "C. confused", "D. happy"],
        "correct_answer": "B"
    },
    {
        "id": 54,
        "question": "\"The store has 'Everything Must Go' signs everywhere.\" This indicates the store is having a:",
        "options": ["A. grand opening", "B. closing down sale", "C. regular sale", "D. new product launch"],
        "correct_answer": "B"
    },
    {
        "id": 55,
        "question": "\"She spoke in a barely audible whisper.\" This means she spoke:",
        "options": ["A. very loudly", "B. very quietly", "C. very quickly", "D. very slowly"],
        "correct_answer": "B"
    },
    {
        "id": 56,
        "question": "\"The proposal was met with thunderous applause.\" This suggests the audience:",
        "options": ["A. disliked it", "B. was confused", "C. loved it", "D. was indifferent"],
        "correct_answer": "C"
    },
    {
        "id": 57,
        "question": "\"His face turned red when she mentioned his mistake.\" This indicates he felt:",
        "options": ["A. proud", "B. embarrassed", "C. angry", "D. excited"],
        "correct_answer": "B"
    },
    {
        "id": 58,
        "question": "\"The company's profits have been declining for three consecutive quarters.\" This suggests the company is:",
        "options": ["A. doing very well", "B. expanding rapidly", "C. facing difficulties", "D. stable"],
        "correct_answer": "C"
    },
    {
        "id": 59,
        "question": "\"She packed her belongings hastily and left without saying goodbye.\" This implies she was:",
        "options": ["A. happy", "B. excited", "C. upset or angry", "D. confused"],
        "correct_answer": "C"
    },
    {
        "id": 60,
        "question": "\"The candidate avoided making eye contact during the interview.\" This might suggest the candidate was:",
        "options": ["A. confident", "B. nervous or dishonest", "C. experienced", "D. qualified"],
        "correct_answer": "B"
    }
]

# LEVEL 5 - EXPERT (60 questions)
# Focus: Academic reading, summarizing, critical thinking, abstract vocabulary, error identification, style analysis
level5_questions = [
    # Critical Thinking and Analysis (1-15)
    {
        "id": 1,
        "question": "The author's tone in the passage can best be described as:",
        "options": ["A. optimistic and encouraging", "B. skeptical and cautious", "C. neutral and objective", "D. pessimistic and discouraging"],
        "correct_answer": "B"
    },
    {
        "id": 2,
        "question": "Which statement best reflects the author's implicit bias?",
        "options": ["A. Technology always improves education", "B. Traditional methods are outdated", "C. Change should be gradual and measured", "D. Innovation is inherently dangerous"],
        "correct_answer": "C"
    },
    {
        "id": 3,
        "question": "The primary purpose of the third paragraph is to:",
        "options": ["A. introduce new evidence", "B. refute opposing arguments", "C. provide historical context", "D. summarize previous points"],
        "correct_answer": "B"
    },
    {
        "id": 4,
        "question": "The author's use of rhetorical questions serves to:",
        "options": ["A. confuse the reader", "B. engage the reader in reflection", "C. avoid taking a stance", "D. demonstrate uncertainty"],
        "correct_answer": "B"
    },
    {
        "id": 5,
        "question": "Which logical fallacy is present in the argument 'Everyone believes X, therefore X must be true'?",
        "options": ["A. Ad hominem", "B. False dichotomy", "C. Bandwagon fallacy", "D. Circular reasoning"],
        "correct_answer": "C"
    },
    {
        "id": 6,
        "question": "The author's credibility is primarily established through:",
        "options": ["A. emotional appeals", "B. statistical evidence", "C. personal anecdotes", "D. authoritative citations"],
        "correct_answer": "D"
    },
    {
        "id": 7,
        "question": "The underlying assumption in the argument is that:",
        "options": ["A. correlation implies causation", "B. the past predicts the future", "C. all stakeholders share common goals", "D. expertise guarantees correct conclusions"],
        "correct_answer": "C"
    },
    {
        "id": 8,
        "question": "The author's methodology could be criticized for:",
        "options": ["A. being too comprehensive", "B. lack of peer review", "C. insufficient sample size", "D. excessive objectivity"],
        "correct_answer": "C"
    },
    {
        "id": 9,
        "question": "Which interpretation of the data is most supported by the evidence?",
        "options": ["A. The trend is irreversible", "B. Multiple factors contribute to the outcome", "C. The correlation is coincidental", "D. The methodology is flawed"],
        "correct_answer": "B"
    },
    {
        "id": 10,
        "question": "The author's conclusion would be stronger if it included:",
        "options": ["A. more emotional language", "B. acknowledgment of limitations", "C. additional personal opinions", "D. simplified explanations"],
        "correct_answer": "B"
    },
    {
        "id": 11,
        "question": "The juxtaposition of contrasting viewpoints serves to:",
        "options": ["A. create confusion", "B. highlight complexity", "C. favor one perspective", "D. avoid responsibility"],
        "correct_answer": "B"
    },
    {
        "id": 12,
        "question": "The author's use of conditional language ('might', 'could', 'possibly') indicates:",
        "options": ["A. uncertainty about the facts", "B. academic caution and precision", "C. lack of confidence", "D. intentional ambiguity"],
        "correct_answer": "B"
    },
    {
        "id": 13,
        "question": "Which aspect of the argument requires further substantiation?",
        "options": ["A. The statistical significance", "B. The theoretical framework", "C. The causal relationships claimed", "D. The methodology described"],
        "correct_answer": "C"
    },
    {
        "id": 14,
        "question": "The author's perspective can be characterized as:",
        "options": ["A. reductionist", "B. holistic", "C. deterministic", "D. relativistic"],
        "correct_answer": "B"
    },
    {
        "id": 15,
        "question": "The implicit message of the conclusion is that:",
        "options": ["A. immediate action is required", "B. further research is necessary", "C. the issue is resolved", "D. previous studies were incorrect"],
        "correct_answer": "B"
    },
    
    # Abstract and Academic Vocabulary (16-30)
    {
        "id": 16,
        "question": "The philosopher's arguments demonstrate remarkable intellectual ...",
        "options": ["A. rigidity", "B. acuity", "C. superficiality", "D. inconsistency"],
        "correct_answer": "B"
    },
    {
        "id": 17,
        "question": "The committee's recommendations lack the ... necessary for implementation.",
        "options": ["A. ambiguity", "B. complexity", "C. specificity", "D. generality"],
        "correct_answer": "C"
    },
    {
        "id": 18,
        "question": "Her research methodology demonstrates ... attention to detail.",
        "options": ["A. meticulous", "B. cursory", "C. reluctant", "D. intermittent"],
        "correct_answer": "A"
    },
    {
        "id": 19,
        "question": "The theory's ... makes it difficult to test empirically.",
        "options": ["A. simplicity", "B. popularity", "C. abstraction", "D. antiquity"],
        "correct_answer": "C"
    },
    {
        "id": 20,
        "question": "The study's findings ... conventional wisdom about learning.",
        "options": ["A. corroborate", "B. challenge", "C. ignore", "D. simplify"],
        "correct_answer": "B"
    },
    {
        "id": 21,
        "question": "The researcher's approach is characterized by methodological ...",
        "options": ["A. chaos", "B. simplicity", "C. rigor", "D. flexibility"],
        "correct_answer": "C"
    },
    {
        "id": 22,
        "question": "The ethical implications of the study are ...",
        "options": ["A. inconsequential", "B. paramount", "C. obvious", "D. irrelevant"],
        "correct_answer": "B"
    },
    {
        "id": 23,
        "question": "The data reveals a ... pattern that warrants further investigation.",
        "options": ["A. ubiquitous", "B. anomalous", "C. predictable", "D. trivial"],
        "correct_answer": "B"
    },
    {
        "id": 24,
        "question": "The author's thesis is both ... and thought-provoking.",
        "options": ["A. conventional", "B. simplistic", "C. contentious", "D. obsolete"],
        "correct_answer": "C"
    },
    {
        "id": 25,
        "question": "The study's conclusions are ... by the limited sample size.",
        "options": ["A. enhanced", "B. confirmed", "C. undermined", "D. clarified"],
        "correct_answer": "C"
    },
    {
        "id": 26,
        "question": "The researcher's claims require ... verification.",
        "options": ["A. immediate", "B. empirical", "C. theoretical", "D. subjective"],
        "correct_answer": "B"
    },
    {
        "id": 27,
        "question": "The study's ... lies in its innovative methodology.",
        "options": ["A. weakness", "B. significance", "C. limitation", "D. confusion"],
        "correct_answer": "B"
    },
    {
        "id": 28,
        "question": "The findings are ... with previous research in the field.",
        "options": ["A. incompatible", "B. identical", "C. consistent", "D. unrelated"],
        "correct_answer": "C"
    },
    {
        "id": 29,
        "question": "The theoretical framework demonstrates conceptual ...",
        "options": ["A. confusion", "B. coherence", "C. simplicity", "D. redundancy"],
        "correct_answer": "B"
    },
    {
        "id": 30,
        "question": "The research contributes to the ... understanding of the phenomenon.",
        "options": ["A. superficial", "B. comprehensive", "C. limited", "D. biased"],
        "correct_answer": "B"
    },
    
    # Style and Register Analysis (31-45)
    {
        "id": 31,
        "question": "Which sentence maintains appropriate academic register?",
        "options": ["A. The results were totally awesome and blew our minds.", "B. The findings demonstrate significant implications for practice.", "C. We were like, really surprised by what we found.", "D. The outcome was way better than we thought it would be."],
        "correct_answer": "B"
    },
    {
        "id": 32,
        "question": "Identify the sentence with inappropriate tone for a research paper:",
        "options": ["A. The data suggests a correlation between variables.", "B. Further investigation is warranted.", "C. Obviously, anyone can see this is wrong.", "D. The methodology follows established protocols."],
        "correct_answer": "C"
    },
    {
        "id": 33,
        "question": "Which sentence demonstrates hedging appropriate for academic writing?",
        "options": ["A. This proves conclusively that the theory is correct.", "B. The evidence suggests that there may be a relationship.", "C. Everyone knows this is the only possible explanation.", "D. This definitely shows the hypothesis is wrong."],
        "correct_answer": "B"
    },
    {
        "id": 34,
        "question": "Select the most concise version without losing meaning:",
        "options": ["A. Due to the fact that the experiment was successful, we proceeded.", "B. Because the experiment succeeded, we continued.", "C. In light of the experimental success, progression was initiated.", "D. The successful nature of the experiment led to our continuation."],
        "correct_answer": "B"
    },
    {
        "id": 35,
        "question": "Which sentence avoids unnecessary jargon while maintaining precision?",
        "options": ["A. The pedagogical intervention facilitated cognitive enhancement.", "B. The teaching method helped students learn better.", "C. The instructional modality optimized learning outcomes.", "D. The educational paradigm enhanced intellectual development."],
        "correct_answer": "B"
    },
    {
        "id": 36,
        "question": "Identify the sentence with appropriate emphasis for academic writing:",
        "options": ["A. The results are ABSOLUTELY INCREDIBLE!", "B. The findings represent a significant contribution.", "C. These results are the most amazing ever discovered.", "D. The outcomes are totally mind-blowing."],
        "correct_answer": "B"
    },
    {
        "id": 37,
        "question": "Which sentence demonstrates appropriate caution in claiming causation?",
        "options": ["A. X causes Y in all cases.", "B. X appears to influence Y under certain conditions.", "C. X definitely makes Y happen.", "D. X always results in Y."],
        "correct_answer": "B"
    },
    {
        "id": 38,
        "question": "Select the sentence that avoids anthropomorphism:",
        "options": ["A. The data argues for a new interpretation.", "B. The study believes that intervention is necessary.", "C. The results suggest alternative explanations.", "D. The research thinks the hypothesis is flawed."],
        "correct_answer": "C"
    },
    {
        "id": 39,
        "question": "Which transition maintains logical flow between contrasting ideas?",
        "options": ["A. Also, the results contradict expectations.", "B. Furthermore, the findings oppose predictions.", "C. However, the outcomes differ from predictions.", "D. Additionally, the data contradicts hypotheses."],
        "correct_answer": "C"
    },
    {
        "id": 40,
        "question": "Identify the sentence with appropriate specificity for academic writing:",
        "options": ["A. Some people think this method works.", "B. Researchers (Smith et al., 2023) report effectiveness.", "C. Everybody knows this approach is good.", "D. Many experts believe in this technique."],
        "correct_answer": "B"
    },
    {
        "id": 41,
        "question": "Which sentence appropriately acknowledges limitations?",
        "options": ["A. This study has no weaknesses whatsoever.", "B. While comprehensive, the sample size limits generalizability.", "C. The methodology is perfect and beyond criticism.", "D. These findings apply to everyone, everywhere."],
        "correct_answer": "B"
    },
    {
        "id": 42,
        "question": "Select the sentence that avoids absolute statements:",
        "options": ["A. This method never fails to produce results.", "B. The approach consistently demonstrates effectiveness.", "C. This technique always works perfectly.", "D. The intervention invariably succeeds completely."],
        "correct_answer": "B"
    },
    {
        "id": 43,
        "question": "Which sentence demonstrates appropriate objectivity?",
        "options": ["A. I personally believe this theory is wonderful.", "B. The evidence supports the theoretical framework.", "C. In my opinion, this approach is the best.", "D. I think everyone should use this method."],
        "correct_answer": "B"
    },
    {
        "id": 44,
        "question": "Identify the sentence with appropriate qualification of claims:",
        "options": ["A. The intervention eliminates all learning difficulties.", "B. The method may reduce certain learning challenges.", "C. The approach cures every educational problem.", "D. The technique solves all academic issues."],
        "correct_answer": "B"
    },
    {
        "id": 45,
        "question": "Which sentence maintains appropriate formality for academic discourse?",
        "options": ["A. The results were pretty cool and stuff.", "B. The findings constitute a noteworthy contribution.", "C. The outcomes were awesome, no kidding.", "D. The data was like, really interesting."],
        "correct_answer": "B"
    },
    
    # Error Identification and Redundancy (46-60)
    {
        "id": 46,
        "question": "Identify the redundant phrase: \"The research study investigates the phenomenon.\"",
        "options": ["A. research study", "B. investigates the", "C. the phenomenon", "D. No redundancy present"],
        "correct_answer": "A"
    },
    {
        "id": 47,
        "question": "Which sentence contains unnecessary wordiness?",
        "options": ["A. The study examined student performance.", "B. In this study, we examined how students performed.", "C. At this point in time, we conducted an examination of the manner in which students performed academically.", "D. We examined student academic performance."],
        "correct_answer": "C"
    },
    {
        "id": 48,
        "question": "Identify the logical inconsistency: \"The universal solution addresses specific problems.\"",
        "options": ["A. universal/specific contradiction", "B. solution/problems mismatch", "C. addresses/problems incompatibility", "D. No inconsistency present"],
        "correct_answer": "A"
    },
    {
        "id": 49,
        "question": "Which sentence contains a dangling modifier?",
        "options": ["A. After completing the experiment, the results were analyzed.", "B. After completing the experiment, researchers analyzed the results.", "C. The results were analyzed after the experiment was completed.", "D. Researchers completed the experiment and analyzed results."],
        "correct_answer": "A"
    },
    {
        "id": 50,
        "question": "Identify the misplaced emphasis: \"Only the researchers studied the participants.\"",
        "options": ["A. Suggests researchers did nothing else", "B. Suggests no one else studied participants", "C. Suggests limited participant study", "D. No misplaced emphasis"],
        "correct_answer": "B"
    },
    {
        "id": 51,
        "question": "Which sentence demonstrates faulty parallelism?",
        "options": ["A. The study was comprehensive, systematic, and thorough.", "B. Participants were selected, trained, and tested.", "C. The method is reliable, valid, and has accuracy.", "D. Results were analyzed, interpreted, and reported."],
        "correct_answer": "C"
    },
    {
        "id": 52,
        "question": "Identify the inappropriate anthropomorphism: \"The study feels that more research is needed.\"",
        "options": ["A. study feels", "B. more research", "C. is needed", "D. No anthropomorphism present"],
        "correct_answer": "A"
    },
    {
        "id": 53,
        "question": "Which sentence contains unnecessary passive construction?",
        "options": ["A. The experiment was conducted by researchers.", "B. Researchers conducted the experiment.", "C. The data was analyzed systematically.", "D. Participants were randomly selected."],
        "correct_answer": "A"
    },
    {
        "id": 54,
        "question": "Identify the problematic nominalization: \"The occurrence of learning happened.\"",
        "options": ["A. occurrence of learning", "B. learning happened", "C. Both A and B", "D. No problematic nominalization"],
        "correct_answer": "C"
    },
    {
        "id": 55,
        "question": "Which sentence shows inappropriate hedging?",
        "options": ["A. The data suggests a possible potential maybe-relationship.", "B. The findings indicate a probable correlation.", "C. Results suggest a potential relationship.", "D. Evidence indicates possible associations."],
        "correct_answer": "A"
    },
    {
        "id": 56,
        "question": "Identify the circular reasoning: \"The method is effective because it works well.\"",
        "options": ["A. effective/works well redundancy", "B. method/effective mismatch", "C. because/well incompatibility", "D. No circular reasoning"],
        "correct_answer": "A"
    },
    {
        "id": 57,
        "question": "Which sentence contains an inappropriate absolute statement?",
        "options": ["A. All participants demonstrated improvement.", "B. Most participants showed improvement.", "C. Many participants demonstrated gains.", "D. Participants generally improved."],
        "correct_answer": "A"
    },
    {
        "id": 58,
        "question": "Identify the mixed metaphor: \"We need to tackle this issue and plant the seeds for success.\"",
        "options": ["A. tackle/plant inconsistency", "B. issue/seeds mismatch", "C. seeds/success incompatibility", "D. No mixed metaphor"],
        "correct_answer": "A"
    },
    {
        "id": 59,
        "question": "Which sentence demonstrates poor cohesion?",
        "options": ["A. The study examined learning. However, participants were selected randomly.", "B. The study examined learning. Therefore, participants were selected randomly.", "C. The study examined learning. Subsequently, participants were selected randomly.", "D. The study examined learning. First, participants were selected randomly."],
        "correct_answer": "A"
    },
    {
        "id": 60,
        "question": "Identify the inappropriate register shift: \"The research methodology was totally awesome and demonstrated significant validity.\"",
        "options": ["A. totally awesome", "B. demonstrated significant", "C. significant validity", "D. No register shift"],
        "correct_answer": "A"
    }
]

def get_questions_for_level(level):
    """Get questions for a specific level"""
    if level in quiz_levels:
        return quiz_levels[level]
    return []

# Quiz Levels
quiz_levels = {
    1: level1_questions,
    2: level2_questions,
    3: level3_questions,
    4: level4_questions,
    5: level5_questions
}

def is_passing_score(level, score, total):
    """Check if score meets the passing threshold for a given level"""
    if level in passing_threshold:
        percentage = (score / total) * 100
        return percentage >= passing_threshold[level]
    return False

# Updated passing threshold (percentage) for each level - slightly increased for higher difficulty
passing_threshold = {
    1: 60,  # 60% to pass level 1 (Beginner)
    2: 65,  # 65% to pass level 2 (Lower-Intermediate)
    3: 70,  # 70% to pass level 3 (Intermediate)
    4: 75,  # 75% to pass level 4 (Upper-Intermediate)
    5: 80   # 80% to pass level 5 (Expert)
}

# Level titles updated to reflect new categorization
level_titles = {
    1: "Level 1 - Beginner",
    2: "Level 2 - Lower-Intermediate", 
    3: "Level 3 - Intermediate",
    4: "Level 4 - Upper-Intermediate",
    5: "Level 5 - Expert"
}

# Level descriptions updated to reflect content focus
level_descriptions = {
    1: "Basic vocabulary (colors, jobs, daily activities), simple grammar (to be, articles, simple present), sentence completion",
    2: "Tenses (present perfect, past continuous), complex daily vocabulary (travel, work, emotions), error correction, functional language",
    3: "Advanced grammar (conditionals, relative clauses, passive voice), academic vocabulary, idioms & collocations, paraphrasing",
    4: "Reading comprehension, mixed conditionals, reported speech, advanced collocations, phrasal verbs, discourse markers, inference",
    5: "Academic reading, critical thinking, abstract vocabulary, style analysis, error identification, summarizing"
}