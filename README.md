# 🎹 AI Piano Coach

A simple agent-based piano learning assistant built with **FastAPI**, **Streamlit**, and a modular **agent architecture**.

The project demonstrates how specialized agents collaborate to generate a learning plan, create practice exercises, evaluate answers, and track learning progress. The architecture is designed to be easily extendable with an LLM (OpenAI, Gemini, Groq, Ollama).

---

## Architecture

```text
                User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
              FastAPI API
                  │
                  ▼
         Orchestrator Agent
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Goal Agent  Curriculum Agent Practice Agent
                                  │
                                  ▼
                          Feedback Agent
                                  │
                                  ▼
                          Progress Agent
                                  │
                                  ▼
                                Tools
                                  │
                                  ▼
                        Curriculum (JSON)
                        Optional LLM
```

---

## Project Structure

```text
.
├── app/
│   ├── agents.py
│   ├── llm.py
│   ├── main.py
│   ├── schemas.py
│   └── tools.py
├── data/
│   └── beginner.json
├── tests/
├── ui/
│   └── streamlit_app.py
├── playground.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

- FastAPI
- Streamlit
- Pydantic
- Python
- JSON
- Pytest
- Optional: Groq / Gemini / OpenAI

---

## Setup

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
python3 -m uvicorn app.main:app --reload
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
streamlit run ui/streamlit_app.py
```

Open:

```
http://localhost:8501
```

---

## Features

- Agent-based architecture
- Learning plan generation
- Practice exercise generation
- Answer evaluation
- Progress tracking
- Modular tool layer
- Ready for LLM integration
```