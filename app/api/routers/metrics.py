"""
Purpose:
--------
Expose application metrics.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/metrics")
def metrics():

    return {

        "version": "1.0.0",

        "agents": 6,

        "memory": "enabled",

        "mcp": "enabled",

        "vector_db": "chroma",

        "llm": "gpt-4o-mini"

    }