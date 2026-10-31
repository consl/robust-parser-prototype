FROM python:3.13-slim

WORKDIR /app

# Устанавливаем переменную окружения, чтобы Python видел пакет src
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Значения по умолчанию, которые можно переопределить в docker-compose
ENV TARGET_URL="https://quotes.toscrape.com"
ENV OUTPUT_PATH="/data/output.json"
ENV LOG_LEVEL="INFO"

CMD ["python", "-m", "src.main"]