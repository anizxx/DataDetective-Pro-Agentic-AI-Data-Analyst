import sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

from .config import STORAGE_DIR

DB_PATH = STORAGE_DIR / "datadetective.db"


def init_db() -> None:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                reference_id TEXT,
                detail TEXT,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


@contextmanager
def get_connection():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def record_event(event_type: str, reference_id: str = "", detail: str = "") -> None:
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO events(event_type, reference_id, detail, created_at) VALUES (?, ?, ?, ?)",
            (event_type, reference_id, detail, datetime.utcnow().isoformat()),
        )
        conn.commit()
