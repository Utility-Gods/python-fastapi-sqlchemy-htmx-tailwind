# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install the project into `/app`
WORKDIR /app

# Set environment variables
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PORT=8000

# Copy requirements first for better caching
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Copy application code
COPY . .

# Install the application
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Set up the path
ENV PATH="/app/.venv/bin:$PATH"

# Build CSS
COPY scripts/setup-tailwind.sh .
RUN ./scripts/setup-tailwind.sh
RUN ./bin/tailwindcss -i ./app/static/css/input.css -o ./app/static/css/output.css --minify

# Expose port 8000
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]