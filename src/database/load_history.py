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

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Tables:", cursor.fetchall())

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