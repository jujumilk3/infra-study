# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MCP_SERVER_MODE=streamable-http

# Copy project files
COPY pyproject.toml ./
COPY main.py ./

# Install uv for faster Python package management
RUN pip install --no-cache-dir uv

# Install dependencies using uv
RUN uv pip install --system --no-cache .

# Expose port for HTTP mode
EXPOSE 8000

# Run the MCP server
CMD ["python", "main.py"]