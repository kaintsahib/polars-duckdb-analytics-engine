import time
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analytics_endpoint_status_and_latency():
    # Warm-up DuckDB in-memory engine
    client.get("/analytics")

    start_time = time.perf_counter()
    response = client.get("/analytics")
    elapsed_ms = (time.perf_counter() - start_time) * 1000.0

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert len(data["data"]) > 0
    assert elapsed_ms < 200.0, f"Latency SLA breached: {elapsed_ms:.2f}ms"
