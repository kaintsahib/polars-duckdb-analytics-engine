# Step 1: Base image
FROM python:3.12-slim

# Step 2: System dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Step 3: Install Poetry
# Step 3: Install Poetry (Updated Official URL)
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# Step 4: Set working directory
WORKDIR /app

# Step 5: Copy dependency files
COPY pyproject.toml poetry.lock ./

# Step 6: Install dependencies (No dev tools)
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

# Step 7: Copy application code
COPY . .

# Step 8: Start the engine
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
