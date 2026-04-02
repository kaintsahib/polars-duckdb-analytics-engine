from pydantic import BaseModel
from typing import List, Dict

class AnalyticsResponse(BaseModel):
    data: List[Dict]
    latency_ms: float
    status: str = "success"
