from fastapi import FastAPI
from app.engine import run_high_speed_analysis
from app.schemas import AnalyticsResponse
from loguru import logger

app = FastAPI(title="AI-Infra Analytics Engine")

@app.get("/")
async def root():
    return {"message": "AI-Infra Engine is Online", "version": "0.1.0"}

@app.get("/analytics", response_model=AnalyticsResponse)
async def get_analytics():
    logger.info("📥 API Request: GET /analytics")
    data, latency = run_high_speed_analysis()
    return {
        "data": data,
        "latency_ms": latency
    }
