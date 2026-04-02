#  High-Performance AI Analytics Engine

[![FastAPI](https://shields.io)](https://tiangolo.com)
[![Polars](https://shields.io)](https://pola.rs)
[![Docker](https://shields.io)](https://docker.com)
[![Poetry](https://shields.io)](https://python-poetry.org)

An enterprise-grade, high-throughput analytics backend built for **AI Infrastructure** workloads. This engine is optimized to process millions of data points with sub-100ms latency using **Polars** and **DuckDB**.

---

## ⚡ Performance Benchmarks
*Tested on Victus Gaming Laptop (12th Gen Intel i5, 16GB RAM)*

- **Dataset Size:** 1,000,000+ Rows (Generated via Polars)
- **Engine:** Polars (Rust-based) + DuckDB (Zero-copy SQL integration)
- **Average Latency:** **< 50ms** 
- **Memory Efficiency:** Optimized via Polars Lazy Evaluation

---

##  Tech Stack & Architecture

- **FastAPI**: Asynchronous Python framework for high-concurrency API requests.
- **Polars**: A lightning-fast DataFrame library written in **Rust**. The modern alternative to Pandas.
- **DuckDB**: In-process analytical SQL engine for complex aggregations without data copying.
- **Docker**: Containerized environment for deterministic and scalable deployments.
- **Poetry**: Professional dependency management (Determinism via `poetry.lock`).
- **Loguru**: Structured logging for infrastructure observability.

---

##  Project Structure

```text
dock-project/
├── app/                  # Core Application Logic
│   ├── main.py           # FastAPI Entry Point
│   ├── engine.py         # Polars + DuckDB Processing Logic
│   ├── schemas.py        # Pydantic Data Models (Strict Typing)
│   └── __init__.py
├── tests/                # Automated Testing Suite (Pytest)
├── Dockerfile            # Multi-stage Docker Image Build
├── pyproject.toml        # Poetry Dependency Configuration
└── README.md             # Project Documentation


 Getting Started
🐳 Using Docker (The Infra Way)
Build and run the containerized engine:
bash
# Build the image
docker build -t ai-infra-engine .

# Run the container
docker run -p 8000:8000 ai-infra-engine

access the analytics at: http://localhost:8000/analytics


# Using Poetry (Local Development)

# Install dependencies
poetry install

# Run the server
export PYTHONPATH=$PYTHONPATH:.
poetry run uvicorn app.main:app --reload# dock-project
