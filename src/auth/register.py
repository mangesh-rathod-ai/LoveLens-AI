import sqlite3

DATABASE = "database/lovelens.db"


def register(username, email, password):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(username,email,password)
        VALUES(?,?,?)
        """,
        (username, email, password)
    )

    conn.commit()

    conn.close()