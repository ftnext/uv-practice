ARG python_version
FROM ghcr.io/astral-sh/uv:python${python_version}-bookworm AS builder
WORKDIR /mylib
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
COPY . /mylib/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-editable

FROM python:${python_version}-slim-bookworm
ARG python_version
COPY --from=builder /mylib/.venv/lib/python${python_version}/site-packages /usr/local/lib/python${python_version}/site-packages
CMD ["python", "-m", "mylib"]
