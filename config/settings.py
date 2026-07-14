"""
=========================================================
LoveLens AI
Application Settings
=========================================================
"""

# -------------------------------------------------
# Application
# -------------------------------------------------

APP_NAME = "LoveLens AI"

APP_VERSION = "1.0.0"

APP_AUTHOR = "Mangesh Rathod"

APP_DESCRIPTION = "AI-Based Love Prediction System"

# -------------------------------------------------
# Database
# -------------------------------------------------

DATABASE_NAME = "lovelens.db"

DATABASE_PATH = "database/lovelens.db"

# -------------------------------------------------
# Questions
# -------------------------------------------------

TOTAL_QUESTIONS = 50

TOTAL_CATEGORIES = 6

# -------------------------------------------------
# Score
# -------------------------------------------------

MAX_SCORE_PER_QUESTION = 10

MAX_TOTAL_SCORE = TOTAL_QUESTIONS * MAX_SCORE_PER_QUESTION

# -------------------------------------------------
# Prediction Thresholds
# -------------------------------------------------

YES_SCORE = 80

MAYBE_SCORE = 60

NO_SCORE = 0

# -------------------------------------------------
# Streamlit
# -------------------------------------------------

PAGE_TITLE = "LoveLens AI"

PAGE_ICON = "❤️"

LAYOUT = "wide"