[🇬🇧] [Read in English](README.md)

# veritas_runtime

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-3.x-09A3D5?logo=spacy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Model%20Hub-yellow?logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Descrição

O **veritas_runtime** é um runtime de inferência em Python para **classificação de fake news em português**, projetado para uso em produção.  
Ele encapsula todo o pipeline de **pré-processamento de texto, carregamento de modelo deep learning (LSTM)** e **exposição de serviço via servidor WebSocket**, com suporte nativo a Docker.

Este repositório é ideal para **deploy de modelos NLP**, integração com APIs, microsserviços ou pipelines distribuídos.

---

## 📚 Sumário

- [veritas\_runtime](#veritas_runtime)
  - [📌 Descrição](#-descrição)
  - [📚 Sumário](#-sumário)
  - [🛠 Tecnologias e Ferramentas](#-tecnologias-e-ferramentas)
    - [Linguagem e Runtime](#linguagem-e-runtime)
    - [Machine Learning \& NLP](#machine-learning--nlp)
    - [Infraestrutura](#infraestrutura)
  - [🧱 Arquitetura do Projeto](#-arquitetura-do-projeto)
  - [🧹 Pré-processamento de Texto](#-pré-processamento-de-texto)
  - [🚀 Execução via Docker](#-execução-via-docker)
    - [1️⃣ Pull da imagem](#1️⃣-pull-da-imagem)
    - [2️⃣ Executar o container](#2️⃣-executar-o-container)
  - [🔌 Comunicação com o Servidor](#-comunicação-com-o-servidor)
  - [🌐 Docker Hub](#-docker-hub)
  - [⚙ Variáveis de Ambiente](#-variáveis-de-ambiente)
  - [📄 Licença](#-licença)
  - [✉️ Contato](#️-contato)

---

## 🛠 Tecnologias e Ferramentas

O runtime foi construído utilizando as seguintes bibliotecas e ferramentas:

### Linguagem e Runtime
- **Python 3.11**

### Machine Learning & NLP
- **TensorFlow / Keras** – inferência com modelo LSTM treinado
- **spaCy (pt_core_news_sm)** – tokenização, stopwords e lematização
- **Unidecode** – normalização de acentos
- **Hugging Face Hub** – download do modelo e tokenizer

### Infraestrutura
- **Docker** – empacotamento e execução do runtime
- **GitHub Actions** – CI para build e push da imagem Docker
- **Socket TCP** – comunicação cliente-servidor

---

## 🧱 Arquitetura do Projeto

Visão geral da estrutura do repositório:

```

veritas_runtime/
├── server.py                     # Entry point da aplicação
├── Dockerfile                 # Build da imagem Docker
├── requirements.txt           # Dependências do projeto
├── LICENSE                    # Licença MIT
├── README.md                  # Documentação
├── .github/
│   └── workflows/
│       └── docker-build.yaml  # CI para build e push no Docker Hub
└── src/
├── init.py            # Inicialização do runtime
├── server/
│   ├── init.py
│   └── launcher.py        # Servidor WebSocket
└── core/
    ├── init.py
    ├── news_classifier.py # Orquestrador do pipeline
    ├── cleaner.py         # Pré-processamento NLP
    ├── model_loader.py    # Carregamento do modelo
    └── predictor.py       # Inferência
```

---

## 🧹 Pré-processamento de Texto

Antes da inferência, o runtime executa automaticamente os seguintes passos de NLP:

1. **Tokenização** com spaCy
2. **Remoção de stopwords**
3. **Remoção de pontuação**
4. **Lematização**
5. **Normalização de acentos** (ex: "informação" → "informacao")
6. **Conversão para sequência numérica** via tokenizer treinado
7. **Padding de sequência** para tamanho fixo

Esses passos garantem compatibilidade total com o modelo LSTM treinado.

---

## 🚀 Execução via Docker

### 1️⃣ Pull da imagem

```bash
docker pull eshantos/veritas_runtime:latest
````

### 2️⃣ Executar o container

```bash
docker run -d \
  -p 9000:9000 \
  --name veritas_runtime \
  eshantos/veritas_runtime:latest
```

O serviço ficará escutando por padrão em:

```
HOST: 0.0.0.0
PORT: 9000
```

---

## 🔌 Comunicação com o Servidor

O runtime utiliza **WebSocket**.

* Envie o texto da notícia (UTF-8)
* Receba como resposta um **score float entre 0 e 1**

Exemplo de resposta:

```
0.873421
```

---

## 🌐 Docker Hub

A imagem oficial do projeto está disponível no Docker Hub:

🔗 **[https://hub.docker.com/r/eshantos/veritas_runtime](https://hub.docker.com/r/eshantos/veritas_runtime)**

---

## ⚙ Variáveis de Ambiente

O runtime suporta as seguintes variáveis:

| Variável | Descrição             | Padrão    |
| -------- | --------------------- | --------- |
| HOST     | Endereço do servidor  | `0.0.0.0` |
| PORT     | Porta do servidor WebSocket | `9000`    |

Exemplo:

```bash
docker run -e HOST=0.0.0.0 -e PORT=9000 eshantos/veritas_runtime
```

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.

Você é livre para usar, modificar e distribuir este software, desde que mantenha os créditos do autor.

📌 Copyright (c) 2025
**Eric Santos**

---

## ✉️ Contato

Em caso de dúvidas, sugestões ou contribuições:

* **Autor:** Eric Santos
* **Email:** [ericshantos13@gmail.com](mailto:ericshantos13@gmail.com)
