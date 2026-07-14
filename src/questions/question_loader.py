"""
=========================================================
LoveLens AI
Question Loader
=========================================================
"""

from src.questions.question_bank import QUESTION_BANK


def load_questions():
    """
    Returns all questions.
    """
    return QUESTION_BANK


def get_question_by_id(question_id):
    """
    Returns a single question using its ID.
    """

    for question in QUESTION_BANK:

        if question["id"] == question_id:

            return question

    return None


def get_questions_by_category(category):
    """
    Returns all questions of a category.
    """

    return [

        question

        for question in QUESTION_BANK

        if question["category"] == category

    ]


def total_questions():
    """
    Returns total number of questions.
    """

    return len(QUESTION_BANK)


def category_list():
    """
    Returns unique category names.
    """

    return sorted(

        list(

            set(

                question["category"]

                for question in QUESTION_BANK

            )

        )

    )


def total_categories():
    """
    Returns number of categories.
    """

    return len(category_list())


def validate_question_bank():
    """
    Checks whether Question IDs are unique.
    """

    ids = [question["id"] for question in QUESTION_BANK]

    return len(ids) == len(set(ids))


def print_summary():
    """
    Prints summary information.
    """

    print("===================================")
    print(" LoveLens AI Question Summary")
    print("===================================")

    print(f"Total Questions : {total_questions()}")

    print(f"Categories      : {total_categories()}")

    print("")

    for category in category_list():

        count = len(get_questions_by_category(category))

        print(f"{category:<20} {count}")

    print("===================================")