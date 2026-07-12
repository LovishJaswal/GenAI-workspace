# 🚀 Gen AI Core

A structured collection of notes, examples, and mini-projects built while learning **Generative AI** from the ground up.

The goal of this repository is to understand how modern LLM applications are built—from making API calls and scraping web content to processing text and creating complete GenAI applications.

---

## 📂 Repository Structure

```
Gen AI Core/
│
├── 01_api_basics/
├── 02_web_scraping/
├── 03_text_processing/
├── 04_projects/
│
├── config.py
├── pyproject.toml
├── README.md
└── .env
```

---

## 📘 01. API Basics

Learn different ways to interact with Large Language Models (LLMs).

### Topics Covered

- Google GenAI Native SDK
- OpenAI SDK
- OpenRouter API
- Raw HTTP Requests
- Local inference using Ollama
- Reasoning models
- OpenRouter free models

### Example Files

- `using_native_sdk.py`
- `using_openai.py`
- `using_openrouter.py`
- `using_requests.py`
- `ollama_chat.py`
- `reasoning_continuation.py`
- `google-gemma-4-31b.py`
- `laguna-m.1.py`
- `openai-gpt-oss-120b.py`

---

## 🌐 02. Web Scraping

Collect and clean webpage data before sending it to an LLM.

### Topics Covered

- Requests
- BeautifulSoup
- HTML Parsing
- User-Agent Spoofing
- Cleaning webpage content

### Example Files

- `clean_webpage.py`
- `html_parsing_demo.py`
- `user_agent.py`

---

## ✂️ 03. Text Processing

Prepare text for Large Language Models.

### Topics Covered

- Fixed-size chunking
- Text preprocessing
- Preparing data for prompts

### Example Files

- `fixed_size_chunking.py`

---

## 💡 04. Projects

Complete end-to-end GenAI applications.

### Projects

### Webpage Summarizer (OpenRouter)

- Accepts a webpage URL
- Scrapes the webpage
- Cleans the HTML
- Sends the content to an LLM
- Saves the generated summary

### Webpage Summarizer (Ollama)

- Works completely offline
- Uses a local Ollama model
- Produces webpage summaries without cloud APIs

---

## ⚙️ Configuration

Secrets are stored inside a `.env` file.

Example:

```env
OPEN_ROUTER_API_KEY=your_api_key
OPEN_ROUTER_BASE_URL=https://openrouter.ai/api/v1

GEMINI_API_KEY=your_api_key
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
```

Environment variables are loaded through `config.py`.

---

## 🛠️ Tech Stack

- Python 3.12
- uv
- Requests
- BeautifulSoup4
- html5lib
- fake-useragent
- OpenAI SDK
- Google GenAI SDK
- Ollama
- OpenRouter

---

## 📦 Installation

Clone the repository.

```bash
git clone <repository-url>
```

Move into the project.

```bash
cd "Gen AI Core"
```

Create the virtual environment (if needed).

```bash
uv venv
```

Install all dependencies.

```bash
uv sync
```

---

## 🎯 Learning Roadmap

This repository will continue expanding with:

- Embeddings
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- AI Agents
- Model Context Protocol (MCP)
- Fine-Tuning
- Production GenAI Applications

---

## 📌 Purpose

This repository serves as a personal learning journey and reference while exploring the GenAI ecosystem. Every script focuses on a specific concept, while the projects combine multiple concepts into practical applications.