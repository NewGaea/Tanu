# syntax=docker/dockerfile:1
FROM python:3.12-slim-bookworm AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_PYTHON_DOWNLOADS=never

COPY --from=ghcr.io/astral-sh/uv:0.12.3 /uv /uvx /bin/
WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-install-project

FROM python:3.12-slim-bookworm AS runtime

ENV DJANGO_DEBUG=false \
    PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN addgroup --system tanu && adduser --system --ingroup tanu tanu

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:0.12.3 /uv /uvx /bin/
COPY --from=builder /opt/venv /opt/venv
COPY --chown=tanu:tanu . .

RUN DJANGO_SECRET_KEY=build-only-secret python manage.py collectstatic --noinput

USER tanu
EXPOSE 8000

CMD ["gunicorn", "tanu.wsgi:application", "--bind", "0.0.0.0:8000", "--access-logfile", "-"]
