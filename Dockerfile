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
ENV REPOSITORY="ericshantos/veritas-bert-ptbr"
ENV TRANSFORMERS_CACHE=/app/cache
ENV HF_HUB_DISABLE_PROGRESS_BARS=1
ENV HF_HUB_DISABLE_TELEMETRY=1

RUN pip install transformers sentencepiece tokenizers accelerate

RUN python -c "\
from transformers import AutoTokenizer, AutoModelForSequenceClassification; \
AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased'); \
AutoModelForSequenceClassification.from_pretrained('ericshantos/veritas-bert-ptbr', trust_remote_code=True)"

RUN rm -rf /root/.cache/pip

EXPOSE 9000

CMD ["python", "server.py"]