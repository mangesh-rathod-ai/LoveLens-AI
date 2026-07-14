import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE = BASE_DIR / "database" / "lovelens.db"

SCHEMA = BASE_DIR / "database" / "schema.sql"


def initialize_database():

    conn = sqlite3.connect(DATABASE)

    with open(SCHEMA, "r", encoding="utf-8") as f:

        conn.executescript(f.read())

    conn.commit()

    conn.close()

    print("✅ Database created successfully")


if __name__ == "__main__":

    initialize_database()