from __future__ import annotations

import os

from flask import Flask, render_template
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection as PGConnection

CREATE_MESSAGES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS messages (
    id serial PRIMARY KEY,
    name text NOT NULL,
    text text NOT NULL,
    created_at timestamptz DEFAULT now()
)
"""

SELECT_MESSAGES_SQL = """
SELECT id, name, text, created_at
FROM messages
ORDER BY created_at DESC
"""


def get_database_url() -> str:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        raise RuntimeError("DATABASE_URL environment variable is required")
    return database_url


def get_db_connection() -> PGConnection:
    try:
        return psycopg2.connect(get_database_url())
    except psycopg2.Error as exc:
        raise RuntimeError("Unable to connect to the database") from exc


def bootstrap_schema() -> None:
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_MESSAGES_TABLE_SQL)
    except psycopg2.Error as exc:
        raise RuntimeError("Unable to initialize database schema") from exc


def fetch_messages() -> list[dict[str, object]]:
    try:
        with get_db_connection() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(SELECT_MESSAGES_SQL)
                return [dict(row) for row in cursor.fetchall()]
    except psycopg2.Error as exc:
        raise RuntimeError("Unable to load messages") from exc


def create_app() -> Flask:
    app = Flask(__name__)

    with app.app_context():
        bootstrap_schema()

    @app.get("/")
    def guestbook() -> str:
        return render_template("guestbook.html", messages=fetch_messages())

    return app


app = create_app()
