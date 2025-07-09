import sqlite3
from datetime import datetime

conn = sqlite3.connect("logs.db", check_same_thread=False)
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


def log_request(original: str, lang: str, translated: str):
    timestamp = datetime.utcnow().isoformat()
    cursor.execute("""
    INSERT INTO logs (timestamp, original, language, translated)
    VALUES (?, ?, ?, ?)
    """, (timestamp, original, lang, translated))
    conn.commit()


def get_all_logs():
    cursor.execute(
        "SELECT timestamp, original, language, translated FROM logs")
    return cursor.fetchall()
