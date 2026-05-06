from __future__ import annotations

import os

from flask import Flask
import psycopg2
from psycopg2.extensions import connection as PGConnection

CREATE_MESSAGES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS messages (
    id serial PRIMARY KEY,
    name text NOT NULL,
    text text NOT NULL,
    created_at timestamptz DEFAULT now()
)
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


def create_app() -> Flask:
    app = Flask(__name__)

    with app.app_context():
        bootstrap_schema()

    return app


app = create_app()
