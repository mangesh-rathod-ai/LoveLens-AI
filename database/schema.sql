CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL,

    email TEXT UNIQUE,

    password TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS prediction_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    love_score INTEGER,

    confidence INTEGER,

    prediction TEXT,

    explanation TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);