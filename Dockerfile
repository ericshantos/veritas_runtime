FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY src ./src
COPY server.py .

RUN python -m spacy download pt_core_news_sm

RUN apt-get update && apt-get install -y \
    build-essential gcc libffi-dev libssl-dev \
    && python -m pip install --no-cache-dir . \
    && rm -rf /var/lib/apt/lists/*

ENV PORT=9000
ENV HOST=0.0.0.0

ENV REPO_ID="ericshantos/veritas-lstm-ptbr"
ENV MODEL_FILENAME="veritas-lstm-ptbr.keras"
ENV TOKENIZER_FILENAME="tokenizer.pkl"

EXPOSE 9000

CMD ["python", "server.py"]
