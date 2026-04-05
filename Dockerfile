FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential gcc libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir .

COPY src ./src
COPY server.py .

ENV PORT=9000
ENV HOST=0.0.0.0
ENV MODEL_REPOSITORY="ericshantos/veritas-bert-ptbr"
ENV TOKENIZER_REPOSITORY="neuralmind/bert-base-portuguese-cased"
ENV TRANSFORMERS_CACHE=/app/cache

RUN python -c "\
from transformers import AutoTokenizer, AutoModelForSequenceClassification; \
AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased'); \
AutoModelForSequenceClassification.from_pretrained('ericshantos/veritas-bert-ptbr')"

RUN rm -rf /root/.cache/pip

EXPOSE 9000

CMD ["python", "server.py"]