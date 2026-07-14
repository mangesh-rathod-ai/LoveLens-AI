"""
=========================================================
LoveLens AI
Weight Rules
=========================================================
"""

# -------------------------------------------------------
# Category Weights (%)
# Total = 100
# -------------------------------------------------------

CATEGORY_WEIGHTS = {

    "Communication": 25,

    "Trust": 20,

    "Care & Support": 20,

    "Social Behaviour": 15,

    "Compatibility": 15,

    "Future Intent": 5

}


# -------------------------------------------------------
# Prediction Rules
# -------------------------------------------------------

PREDICTION_RULES = {

    "YES": {
        "min_score": 80,
        "max_score": 100
    },

    "MAYBE": {
        "min_score": 60,
        "max_score": 79
    },

    "NO": {
        "min_score": 0,
        "max_score": 59
    }

}


# -------------------------------------------------------
# Confidence Rules
# -------------------------------------------------------

CONFIDENCE_RULES = {

    95: (95, 100),

    90: (90, 94),

    85: (85, 89),

    80: (80, 84),

    75: (75, 79),

    70: (70, 74),

    65: (65, 69),

    60: (60, 64),

    50: (0, 59)

}


# -------------------------------------------------------
# Score Labels
# -------------------------------------------------------

SCORE_LABELS = {

    "Excellent": (90, 100),

    "Very Good": (80, 89),

    "Good": (70, 79),

    "Average": (60, 69),

    "Low": (40, 59),

    "Very Low": (0, 39)

}


# -------------------------------------------------------
# Utility Functions
# -------------------------------------------------------

def get_category_weight(category):

    return CATEGORY_WEIGHTS.get(category, 0)


def get_prediction(score):

    for label, rule in PREDICTION_RULES.items():

        if rule["min_score"] <= score <= rule["max_score"]:

            return label

    return "NO"


def get_confidence(score):

    for confidence, value in CONFIDENCE_RULES.items():

        minimum = value[0]

        maximum = value[1]

        if minimum <= score <= maximum:

            return confidence

    return 50


def get_score_label(score):

    for label, value in SCORE_LABELS.items():

        minimum = value[0]

        maximum = value[1]

        if minimum <= score <= maximum:

            return label

    return "Unknown"