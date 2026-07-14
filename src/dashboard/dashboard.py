"""
=========================================================
LoveLens AI
Dashboard Engine
=========================================================
"""


def get_dashboard_statistics(history):
    """
    Generate dashboard statistics.
    """

    if history.empty:

        return {

            "total_predictions": 0,

            "yes_count": 0,

            "maybe_count": 0,

            "no_count": 0,

            "average_score": 0,

            "average_confidence": 0

        }

    total_predictions = len(history)

    yes_count = len(

        history[history["prediction"] == "❤️ YES"]

    )

    maybe_count = len(

        history[history["prediction"] == "😊 MAYBE"]

    )

    no_count = len(

        history[history["prediction"] == "💔 NO"]

    )

    average_score = round(

        history["love_score"].mean(),

        2

    )

    average_confidence = round(

        history["confidence"].mean(),

        2

    )

    highest_score = history["love_score"].max()

    lowest_score = history["love_score"].min()

    return {

        "total_predictions": total_predictions,

        "yes_count": yes_count,

        "maybe_count": maybe_count,

        "no_count": no_count,

        "average_score": average_score,

        "average_confidence": average_confidence,

        "highest_score": highest_score,

        "lowest_score": lowest_score

    }