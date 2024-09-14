FROM ghcr.io/astral-sh/uv:python3.12-bookworm AS builder
WORKDIR /mylib
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
COPY . /mylib/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project
RUN <<INSTALL_PROJECT
    .venv/bin/python -m ensurepip
    .venv/bin/python -m pip install --no-deps .
INSTALL_PROJECT

FROM python:3.12-slim-bookworm
COPY --from=builder /mylib/.venv/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
CMD ["python", "-m", "mylib"]
