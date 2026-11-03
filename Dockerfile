FROM python:3.13-slim

WORKDIR /app

# Set environment variable so Python can find the src package
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Default values that can be overridden in docker-compose
ENV TARGET_URL="https://quotes.toscrape.com"
ENV OUTPUT_PATH="/data/output.json"
ENV LOG_LEVEL="INFO"

CMD ["python", "-m", "src.main"]