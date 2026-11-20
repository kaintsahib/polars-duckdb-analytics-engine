# File: tests/test_engine.py
import time
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analytics_endpoint_status_and_latency():
    start_time = time.perf_counter()
    response = client.get("/analytics")
    elapsed_ms = (time.perf_counter() - start_time) * 1000.0

    assert response.status_code == 200
    data = response.json()
    assert data is not None
    # Verify sub-100ms SLA guarantee
    assert elapsed_ms < 100.0, f"Latency SLA breached: {elapsed_ms:.2f}ms"
