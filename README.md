[🇧🇷] [Lê em português](README.pt.md)

# veritas_runtime

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-3.x-09A3D5?logo=spacy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Model%20Hub-yellow?logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Description

**veritas_runtime** is a Python-based inference runtime for **fake news classification in Portuguese**, designed for production use.  
It encapsulates the complete pipeline for **text preprocessing, deep learning model loading (LSTM)**, and **service exposure via a WebSocket server**, with native Docker support.

This repository is ideal for **deploying NLP models**, integration with APIs, microservices, or distributed pipelines.

---

## 📚 Table of Contents

- [veritas\_runtime](#veritas_runtime)
  - [📌 Description](#-description)
  - [📚 Table of Contents](#-table-of-contents)
  - [🛠 Technologies and Tools](#-technologies-and-tools)
    - [Language and Runtime](#language-and-runtime)
    - [Machine Learning \& NLP](#machine-learning--nlp)
    - [Infrastructure](#infrastructure)
  - [🧱 Project Architecture](#-project-architecture)
  - [🧹 Text Preprocessing](#-text-preprocessing)
  - [🚀 Running with Docker](#-running-with-docker)
    - [1️⃣ Pull the image](#1️⃣-pull-the-image)
    - [2️⃣ Run the container](#2️⃣-run-the-container)
  - [🔌 Server Communication](#-server-communication)
  - [🌐 Docker Hub](#-docker-hub)
  - [⚙ Environment Variables](#-environment-variables)
  - [📄 License](#-license)
  - [✉️ Contact](#️-contact)

---

## 🛠 Technologies and Tools

The runtime was built using the following libraries and tools:

### Language and Runtime
- **Python 3.11**

### Machine Learning & NLP
- **PyTorch** – inference with a trained BERT model
- **Transformers** – model and tokenizer loading

### Infrastructure
- **Docker** – runtime packaging and execution
- **GitHub Actions** – CI for Docker image build and push
- **TCP Socket** – client-server communication

---

## 🧱 Project Architecture

Overview of the repository structure:

```

veritas_runtime/
├── app.py                     # Application entry point
├── Dockerfile                 # Docker image build
├── requirements.txt           # Project dependencies
├── LICENSE                    # MIT License
├── README.md                  # Documentation
├── .github/
│   └── workflows/
│       └── docker-build.yaml  # CI for build and push to Docker Hub
└── src/
├── **init**.py            # Runtime initialization
├── server/
│   ├── **init**.py
│   └── launcher.py        # WebSocket server
└── core/
    ├── **init**.py
    ├── news_classifier.py # Pipeline orchestrator
    ├── cleaner.py         # NLP preprocessing
    ├── model_loader.py    # Model loading
    └── predictor.py       # Inference
````

---

## 🧹 Text Preprocessing

Before inference, the runtime automatically performs the following NLP steps:

1. **Tokenization** with spaCy
2. **Stopword removal**
3. **Punctuation removal**
4. **Lemmatization**
5. **Accent normalization** (e.g., `"informação"` → `"informacao"`)
6. **Conversion to numeric sequences** using the trained tokenizer
7. **Sequence padding** to a fixed length

These steps ensure full compatibility with the trained LSTM model.

---

## 🚀 Running with Docker

### 1️⃣ Pull the image

```bash
docker pull eshantos/veritas_runtime:latest
````

### 2️⃣ Run the container

```bash
docker run -d \
  -p 9000:9000 \
  --name veritas_runtime \
  eshantos/veritas_runtime:latest
```

By default, the service listens on:

```
HOST: 0.0.0.0
PORT: 9000
```

---

## 🔌 Server Communication

The runtime uses a **WebSocket**.

* Send the news text (UTF-8 encoded)
* Receive a **float score between 0 and 1** as response

Example response:

```
0.873421
```

---

## 🌐 Docker Hub

The official project image is available on Docker Hub:

🔗 **[https://hub.docker.com/r/eshantos/veritas_runtime](https://hub.docker.com/r/eshantos/veritas_runtime)**

---

## ⚙ Environment Variables

The runtime supports the following environment variables:

| Variable | Description     | Default   |
| -------- | --------------- | --------- |
| HOST     | Server address  | `0.0.0.0` |
| PORT     | WebSocket server port | `9000`    |

Example:

```bash
docker run -e HOST=0.0.0.0 -e PORT=9000 eshantos/veritas_runtime
```

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software, provided that the author's credits are preserved.

📌 Copyright (c) 2025
**Eric Santos**

---

## ✉️ Contact

For questions, suggestions, or contributions:

* **Author:** Eric Santos
* **Email:** [ericshantos13@gmail.com](mailto:ericshantos13@gmail.com)