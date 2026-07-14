"""
=========================================================
LoveLens AI
Score Engine
=========================================================
"""

from src.questions.question_bank import QUESTION_BANK
from src.questions.question_weights import get_weight
from src.questions.categories import CATEGORIES


def calculate_scores(user_answers):
    """
    Calculates category scores and overall love score.

    Parameters
    ----------
    user_answers : dict

    Example
    -------
    {
        1: "Daily",
        2: "Both",
        3: "Fast"
    }

    Returns
    -------
    Dictionary containing

    Communication Score
    Trust Score
    Care & Support Score
    Social Behaviour Score
    Compatibility Score
    Future Intent Score

    Overall Love Score
    """

    category_scores = {}

    category_max_scores = {}

    # Initialize categories
    for category in CATEGORIES.keys():

        category_scores[category] = 0

        category_max_scores[category] = 0

    # --------------------------------------------
    # Calculate Scores
    # --------------------------------------------

    for question in QUESTION_BANK:

        question_id = question["id"]

        category = question["category"]

        answer = user_answers.get(question_id, None)

        score = get_weight(answer)

        category_scores[category] += score

        category_max_scores[category] += 10

    # --------------------------------------------
    # Convert to Percentage
    # --------------------------------------------

    category_percentages = {}

    weighted_total = 0

    total_weight = 0

    for category in CATEGORIES.keys():

        maximum = category_max_scores[category]

        obtained = category_scores[category]

        if maximum == 0:

            percentage = 0

        else:

            percentage = round((obtained / maximum) * 100)

        category_percentages[category] = percentage

        weight = CATEGORIES[category]["weight"]

        weighted_total += percentage * weight

        total_weight += weight

    # --------------------------------------------
    # Overall Love Score
    # --------------------------------------------

    love_score = round(weighted_total / total_weight)

    return {

        "category_scores": category_percentages,

        "love_score": love_score

    }


def get_category_score(scores, category):

    return scores["category_scores"].get(category, 0)


def get_love_score(scores):

    return scores["love_score"]