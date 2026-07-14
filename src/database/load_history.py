import sqlite3
import pandas as pd
import os

DATABASE = "database/lovelens.db"


def load_history():

    print("=" * 50)
    print("Current Working Directory :", os.getcwd())
    print("Database Absolute Path    :", os.path.abspath(DATABASE))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Show available tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)

    # If prediction_history doesn't exist, return an empty DataFrame
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='prediction_history';
    """)

    if cursor.fetchone() is None:
        print("prediction_history table not found.")
        conn.close()

        return pd.DataFrame(
            columns=[
                "id",
                "username",
                "love_score",
                "confidence",
                "prediction",
                "explanation",
                "created_at"
            ]
        )

    query = """
    SELECT
        id,
        username,
        love_score,
        confidence,
        prediction,
        explanation,
        created_at
    FROM prediction_history
    ORDER BY created_at DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df