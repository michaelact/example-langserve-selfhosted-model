FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN --mount=target=/root/.cache,type=cache \
  --mount=target=/app/.venv,type=cache \
  pip install poetry && \
  poetry config virtualenvs.create false && \
  poetry install --no-interaction --no-ansi --only main

CMD exec poetry run uvicorn langserve_launch_example.server:app --host 0.0.0.0 --port 8001
