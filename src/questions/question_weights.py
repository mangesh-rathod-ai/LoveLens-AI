"""
=========================================================
LoveLens AI
Question Weights
=========================================================
"""

WEIGHTS = {

    # --------------------------------------------------
    # Frequency
    # --------------------------------------------------

    "Never": 0,
    "Rarely": 2,
    "Sometimes": 5,
    "Often": 8,
    "Always": 10,

    # --------------------------------------------------
    # Communication
    # --------------------------------------------------

    "Daily": 10,
    "Weekly": 8,
    "Monthly": 4,

    # --------------------------------------------------
    # Conversation Starter
    # --------------------------------------------------

    "You": 4,
    "Them": 8,
    "Both": 10,

    # --------------------------------------------------
    # Reply Speed
    # --------------------------------------------------

    "Very Slow": 2,
    "Slow": 4,
    "Average": 6,
    "Fast": 8,
    "Very Fast": 10,

    # --------------------------------------------------
    # Interest
    # --------------------------------------------------

    "Not Interested": 2,
    "Slightly": 4,
    "Neutral": 6,
    "Interested": 8,
    "Very Interested": 10,

    # --------------------------------------------------
    # Comfort
    # --------------------------------------------------

    "Very Uncomfortable": 2,
    "Uncomfortable": 4,
    "Comfortable": 8,
    "Very Comfortable": 10,

    # --------------------------------------------------
    # Trust
    # --------------------------------------------------

    "Not at all": 0,
    "A little": 2,
    "Somewhat": 5,
    "Mostly": 8,
    "Completely": 10,

    # --------------------------------------------------
    # Future Intent
    # --------------------------------------------------

    "Definitely No": 0,
    "Probably No": 2,
    "Maybe": 5,
    "Probably Yes": 8,
    "Definitely Yes": 10
}


def get_weight(answer):
    """
    Returns the numerical score for an answer.
    """

    return WEIGHTS.get(answer, 0)


def get_max_weight():
    """
    Returns maximum possible score for one question.
    """

    return 10


def get_min_weight():
    """
    Returns minimum possible score.
    """

    return 0


def is_valid_answer(answer):
    """
    Checks whether an answer exists in the weight dictionary.
    """

    return answer in WEIGHTS


def total_weight_options():
    """
    Returns total answer options available.
    """

    return len(WEIGHTS)