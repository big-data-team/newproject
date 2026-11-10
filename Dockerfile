FROM debian:bookworm-slim
COPY --from=ghcr.io/astral-sh/uv:0.11.8 /uv /uvx /usr/local/bin/

WORKDIR /app

COPY README.md pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project
COPY ./src ./src
RUN uv sync --locked

CMD ["uv", "run", "python3", "-m", "newproject_eadishchev"]
