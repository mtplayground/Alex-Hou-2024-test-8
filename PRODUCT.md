# Product Snapshot

## What This Project Is
`Alex-Hou-2024-test-8` is a small Python guestbook web app that will use Flask for HTTP handling, PostgreSQL for persistence, and gunicorn for production serving.

## Current State
The repository currently contains bootstrap, containerization, and database initialization setup from issues `#1` through `#3`.
- Python runtime dependencies are declared in `requirements.txt`.
- Local environment configuration is documented in `.env.example`.
- Repository ignore rules are in place for Python artifacts, virtualenvs, and local secret/state files.
- A production-oriented Dockerfile is present for running the app with gunicorn on port `8080`.
- `app.py` now creates the Flask app, opens PostgreSQL connections from `DATABASE_URL`, and bootstraps the `messages` table at startup.

## What It Does Today
The repository now has a real Flask entrypoint and database bootstrap, but it still does not expose any guestbook routes or HTML rendering yet.

## Key Decisions
- Use Flask as the web framework.
- Use `psycopg2-binary` for PostgreSQL connectivity.
- Use gunicorn as the production app server.
- Configure the database through `DATABASE_URL` in the environment instead of hardcoding connection details.
- Standardize container execution around `gunicorn app:app` bound to `0.0.0.0:8080`.
- Initialize the `messages` table during app startup with idempotent `CREATE TABLE IF NOT EXISTS` SQL.

## Conventions
- Keep environment-specific values out of version control.
- Keep the container image based on `python:3.11-slim` unless there is a clear reason to change it.
- Keep `PRODUCT.md` aligned with merged `main` only, not planned or in-progress work.
