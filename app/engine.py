import time
import polars as pl
import duckdb
from loguru import logger

_NUM_ROWS = 1_000_000
_TELEMETRY_DF = pl.DataFrame({
    "node_id": [f"gpu-node-{i % 8}" for i in range(_NUM_ROWS)],
    "model": ["deepseek-v3" if i % 2 == 0 else "qwen-72b" for i in range(_NUM_ROWS)],
    "tokens_generated": [(i % 512) + 64 for i in range(_NUM_ROWS)],
    "latency_ms": [12.5 + (i % 40) * 0.75 for i in range(_NUM_ROWS)],
})

# Persistent in-memory DuckDB connection with zero-copy Arrow registration
_CON = duckdb.connect(database=":memory:")
_CON.register("telemetry", _TELEMETRY_DF)

def run_high_speed_analysis():
    start_time = time.perf_counter()
    query = """
        SELECT
            node_id,
            model,
            COUNT(*) AS total_requests,
            SUM(tokens_generated) AS total_tokens,
            ROUND(AVG(latency_ms), 2) AS avg_latency_ms
        FROM telemetry
        GROUP BY node_id, model
        ORDER BY total_tokens DESC
    """
    result_df = _CON.execute(query).pl()
    execution_time = round((time.perf_counter() - start_time) * 1000.0, 2)
    logger.info(f"Processed {_NUM_ROWS:,} rows in {execution_time} ms")
    return result_df.to_dicts(), execution_time
