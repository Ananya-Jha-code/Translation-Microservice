# utils/db.py

import sqlite3


def get_db_connection():
    conn = sqlite3.connect("logs.db", check_same_thread=False)
    return conn


def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            original TEXT,
            language TEXT,
            translated TEXT
        )
    """)
    conn.commit()
    conn.close()
