# Product Snapshot

## What This Project Is
`Alex-Hou-2024-test-8` is a small Python guestbook web app that will use Flask for HTTP handling, PostgreSQL for persistence, and gunicorn for production serving.

## Current State
The repository currently contains bootstrap and containerization setup from issues `#1` and `#2`.
- Python runtime dependencies are declared in `requirements.txt`.
- Local environment configuration is documented in `.env.example`.
- Repository ignore rules are in place for Python artifacts, virtualenvs, and local secret/state files.
- A production-oriented Dockerfile is present for running the app with gunicorn on port `8080`.

## What It Does Today
The repository is still pre-application setup. It defines the Python dependencies and container runtime shape, but there is still no merged Flask app code, database bootstrap, or HTTP route implementation.

## Key Decisions
- Use Flask as the web framework.
- Use `psycopg2-binary` for PostgreSQL connectivity.
- Use gunicorn as the production app server.
- Configure the database through `DATABASE_URL` in the environment instead of hardcoding connection details.
- Standardize container execution around `gunicorn app:app` bound to `0.0.0.0:8080`.

## Conventions
- Keep environment-specific values out of version control.
- Keep the container image based on `python:3.11-slim` unless there is a clear reason to change it.
- Keep `PRODUCT.md` aligned with merged `main` only, not planned or in-progress work.
