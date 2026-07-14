import sqlite3

DATABASE = "database/lovelens.db"


def save_prediction(data):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history
        (
            username,
            love_score,
            confidence,
            prediction,
            explanation
        )

        VALUES
        (
            ?,?,?,?,?
        )
        """,
        (
            data["username"],
            data["love_score"],
            data["confidence"],
            data["prediction"],
            data["explanation"]
        )
    )

    conn.commit()

    conn.close()