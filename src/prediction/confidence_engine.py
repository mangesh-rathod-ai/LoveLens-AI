"""
=========================================================
LoveLens AI
Confidence Engine
=========================================================
"""

from src.scoring.weight_rules import CONFIDENCE_RULES


def calculate_confidence(love_score):
    """
    Calculates confidence percentage based on Love Score.

    Parameters
    ----------
    love_score : int

    Returns
    -------
    Confidence Percentage
    """

    for confidence, score_range in CONFIDENCE_RULES.items():

        minimum = score_range[0]
        maximum = score_range[1]

        if minimum <= love_score <= maximum:

            return confidence

    return 50


def confidence_level(confidence):
    """
    Returns confidence label.
    """

    if confidence >= 95:

        return "Excellent"

    elif confidence >= 90:

        return "Very High"

    elif confidence >= 80:

        return "High"

    elif confidence >= 70:

        return "Medium"

    elif confidence >= 60:

        return "Low"

    else:

        return "Very Low"


def confidence_details(love_score):
    """
    Returns complete confidence information.
    """

    confidence = calculate_confidence(love_score)

    return {

        "confidence": confidence,

        "level": confidence_level(confidence)

    }