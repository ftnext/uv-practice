FROM ghcr.io/astral-sh/uv:python3.12-bookworm AS builder
WORKDIR /app
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-dev

FROM python:3.12-slim-bookworm
COPY --from=builder /app/.venv/bin/uvicorn /usr/local/bin/uvicorn
COPY --from=builder /app/.venv/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
WORKDIR /app
COPY main.py .
EXPOSE 8000
CMD ["uvicorn", "main:app"]
