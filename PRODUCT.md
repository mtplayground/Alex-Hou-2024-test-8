# Product Snapshot

## What This Project Is
`Alex-Hou-2024-test-8` is a small Python guestbook web app that will use Flask for HTTP handling, PostgreSQL for persistence, and gunicorn for production serving.

## Current State
Only the project bootstrap from issue `#1` is merged.
- Python runtime dependencies are declared in `requirements.txt`.
- Local environment configuration is documented in `.env.example`.
- Repository ignore rules are in place for Python artifacts, virtualenvs, and local secret/state files.

## What It Does Today
The repository is currently setup-only. There is no application code, Docker image, database bootstrap, or HTTP route implementation merged yet.

## Key Decisions
- Use Flask as the web framework.
- Use `psycopg2-binary` for PostgreSQL connectivity.
- Use gunicorn as the production app server.
- Configure the database through `DATABASE_URL` in the environment instead of hardcoding connection details.

## Conventions
- Keep environment-specific values out of version control.
- Keep `PRODUCT.md` aligned with merged `main` only, not planned or in-progress work.
