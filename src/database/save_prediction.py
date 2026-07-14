import sqlite3

DATABASE = "database/lovelens.db"

def save_prediction(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        love_score INTEGER,
        confidence INTEGER,
        prediction TEXT,
        explanation TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    INSERT INTO prediction_history
    (
        username,
        love_score,
        confidence,
        prediction,
        explanation
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        data["username"],
        data["love_score"],
        data["confidence"],
        data["prediction"],
        data["explanation"]
    ))

    conn.commit()
    conn.close()