"""
=========================================================
LoveLens AI
Validation Engine
=========================================================
"""


def validate_personal_info(data):
    """
    Validate Personal Information
    """

    errors = []

    # -------------------------
    # Name
    # -------------------------

    name = data.get("name", "").strip()

    if not name:

        errors.append("Name is required.")

    elif len(name) < 2:

        errors.append("Name must contain at least 2 characters.")

    # -------------------------
    # Age
    # -------------------------

    age = data.get("age", 0)

    if age < 13:

        errors.append("Age must be at least 13 years.")

    elif age > 100:

        errors.append("Please enter a valid age.")

    # -------------------------
    # Gender
    # -------------------------

    gender = data.get("gender", "")

    if gender == "":

        errors.append("Please select your gender.")

    # -------------------------
    # Relationship Status
    # -------------------------

    relationship = data.get("relationship_status", "")

    if relationship == "":

        errors.append("Please select relationship status.")

    return errors


def validate_answers(answers, total_questions=50):
    """
    Validate Question Answers
    """

    errors = []

    if len(answers) != total_questions:

        errors.append(
            f"Please answer all {total_questions} questions."
        )

    for question_id in range(1, total_questions + 1):

        if question_id not in answers:

            errors.append(
                f"Question {question_id} is unanswered."
            )

    return errors


def validate_prediction_ready(personal_info, answers):
    """
    Check if project is ready for prediction
    """

    errors = []

    errors.extend(validate_personal_info(personal_info))

    errors.extend(validate_answers(answers))

    return errors


def is_valid(personal_info, answers):
    """
    Returns True if validation passes
    """

    errors = validate_prediction_ready(
        personal_info,
        answers
    )

    return len(errors) == 0