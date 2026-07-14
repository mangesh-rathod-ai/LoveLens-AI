import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE = BASE_DIR / "database" / "lovelens.db"
SCHEMA = BASE_DIR / "database" / "schema.sql"


def initialize_database():
    print(f"BASE_DIR : {BASE_DIR}")
    print(f"DATABASE : {DATABASE}")
    print(f"SCHEMA   : {SCHEMA}")
    print(f"Schema exists: {SCHEMA.exists()}")

    conn = sqlite3.connect(DATABASE)

    with open(SCHEMA, "r", encoding="utf-8") as f:
        schema = f.read()
        print(schema)   # prints SQL to logs
        conn.executescript(schema)

    conn.commit()

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Tables after initialization:", cursor.fetchall())

    conn.close()

    print("✅ Database initialized successfully")