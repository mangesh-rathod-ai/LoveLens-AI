"""
=========================================================
LoveLens AI
Categories Configuration
=========================================================
"""

CATEGORIES = {

    "Communication": {
        "weight": 25,
        "total_questions": 10,
        "start_id": 1,
        "end_id": 10
    },

    "Trust": {
        "weight": 20,
        "total_questions": 8,
        "start_id": 11,
        "end_id": 18
    },

    "Care & Support": {
        "weight": 20,
        "total_questions": 8,
        "start_id": 19,
        "end_id": 26
    },

    "Social Behaviour": {
        "weight": 15,
        "total_questions": 8,
        "start_id": 27,
        "end_id": 34
    },

    "Compatibility": {
        "weight": 15,
        "total_questions": 8,
        "start_id": 35,
        "end_id": 42
    },

    "Future Intent": {
        "weight": 5,
        "total_questions": 8,
        "start_id": 43,
        "end_id": 50
    }

}


TOTAL_QUESTIONS = 50

TOTAL_CATEGORIES = len(CATEGORIES)

MAX_SCORE_PER_QUESTION = 10

TOTAL_MAX_SCORE = TOTAL_QUESTIONS * MAX_SCORE_PER_QUESTION

