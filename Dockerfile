FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .

RUN apt-get update && apt-get install -y \
    build-essential gcc libffi-dev libssl-dev \
    && python -m pip install --no-cache-dir -e . \
    && rm -rf /var/lib/apt/lists/*

COPY . .

ENV PORT=9000
ENV HOST=0.0.0.0

EXPOSE 9000

CMD ["python", "server.py"]
