"""
=========================================================
LoveLens AI
Decision Engine
=========================================================
"""

from src.scoring.weight_rules import (
    PREDICTION_RULES,
    get_score_label
)


def predict(love_score):
    """
    Returns final prediction based on Love Score.

    Parameters
    ----------
    love_score : int

    Returns
    -------
    ❤️ YES
    😊 MAYBE
    💔 NO
    """

    if (
        PREDICTION_RULES["YES"]["min_score"]
        <= love_score <=
        PREDICTION_RULES["YES"]["max_score"]
    ):

        return "❤️ YES"

    elif (
        PREDICTION_RULES["MAYBE"]["min_score"]
        <= love_score <=
        PREDICTION_RULES["MAYBE"]["max_score"]
    ):

        return "😊 MAYBE"

    else:

        return "💔 NO"


def prediction_details(love_score):
    """
    Returns detailed prediction information.
    """

    prediction = predict(love_score)

    score_label = get_score_label(love_score)

    return {

        "love_score": love_score,

        "prediction": prediction,

        "score_label": score_label

    }


def is_positive_prediction(love_score):
    """
    Returns True if prediction is YES.
    """

    return predict(love_score) == "❤️ YES"


def is_maybe_prediction(love_score):
    """
    Returns True if prediction is MAYBE.
    """

    return predict(love_score) == "😊 MAYBE"


def is_negative_prediction(love_score):
    """
    Returns True if prediction is NO.
    """

    return predict(love_score) == "💔 NO"