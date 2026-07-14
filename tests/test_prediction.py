"""
=========================================
LoveLens AI
Prediction Test
=========================================
"""

from src.prediction.decision_engine import predict


def test_prediction():

    assert predict(90) == "❤️ YES"

    assert predict(70) == "😊 MAYBE"

    assert predict(40) == "💔 NO"

    print("✅ Prediction Engine Test Passed")


if __name__ == "__main__":

    test_prediction()