"""
=========================================================
LoveLens AI
Explanation Engine
=========================================================
"""


def generate_explanation(love_score, category_scores):
    """
    Generate AI explanation based on
    Love Score and Category Scores.
    """

    explanation = []

    # ----------------------------------------
    # Overall Prediction
    # ----------------------------------------

    if love_score >= 80:

        explanation.append(
            "Your responses indicate a strong possibility of a positive relationship."
        )

    elif love_score >= 60:

        explanation.append(
            "Your responses show some positive signs, but the relationship may need better communication and understanding."
        )

    else:

        explanation.append(
            "The current responses indicate a low compatibility level. Building trust and communication may improve the relationship."
        )

    explanation.append("")

    # ----------------------------------------
    # Category Analysis
    # ----------------------------------------

    for category, score in category_scores.items():

        if score >= 90:

            explanation.append(
                f"✅ {category}: Excellent ({score}%)"
            )

        elif score >= 80:

            explanation.append(
                f"🟢 {category}: Very Good ({score}%)"
            )

        elif score >= 70:

            explanation.append(
                f"🟡 {category}: Good ({score}%)"
            )

        elif score >= 60:

            explanation.append(
                f"🟠 {category}: Average ({score}%)"
            )

        else:

            explanation.append(
                f"🔴 {category}: Needs Improvement ({score}%)"
            )

    explanation.append("")

    # ----------------------------------------
    # Suggestions
    # ----------------------------------------

    if category_scores.get("Communication", 0) < 70:

        explanation.append(
            "• Try communicating more openly and honestly."
        )

    if category_scores.get("Trust", 0) < 70:

        explanation.append(
            "• Building trust can strengthen the relationship."
        )

    if category_scores.get("Care & Support", 0) < 70:

        explanation.append(
            "• Showing more care and emotional support may help."
        )

    if category_scores.get("Compatibility", 0) < 70:

        explanation.append(
            "• Spend more quality time together and discover shared interests."
        )

    if category_scores.get("Future Intent", 0) < 70:

        explanation.append(
            "• Discuss future goals and expectations together."
        )

    explanation.append("")

    explanation.append(
        "⚠️ This prediction is generated using a rule-based AI system and is intended for entertainment purposes only."
    )

    return "\n".join(explanation)