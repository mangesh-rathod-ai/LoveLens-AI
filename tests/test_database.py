"""
=========================================
LoveLens AI
Database Test
=========================================
"""

from src.database.load_history import load_history


def test_database():

    history = load_history()

    assert history is not None

    print("✅ Database Connection Successful")

    print(history.head())


if __name__ == "__main__":

    test_database()