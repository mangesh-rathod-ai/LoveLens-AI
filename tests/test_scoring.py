"""
=========================================
LoveLens AI
Test Score Engine
=========================================
"""

from src.scoring.score_engine import calculate_scores


def test_score_engine():

    answers = {}

    for i in range(1, 51):
        answers[i] = "Always"

    result = calculate_scores(answers)

    assert result["love_score"] == 100

    print("✅ Score Engine Test Passed")


if __name__ == "__main__":

    test_score_engine()