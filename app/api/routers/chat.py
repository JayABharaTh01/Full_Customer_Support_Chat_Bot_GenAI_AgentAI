from fastapi import APIRouter

from app.agents.orchestrator.graph import (
    compiled_graph
)

router = APIRouter()


@router.post(
    "/chat"
)
def chat(
    query: str
):

    result = compiled_graph.invoke(

        {

            "request_id": "1",

            "session_id": "session_1",

            "user_id": "1",

            "query": query,

            "intent": "",

            "intent_confidence": 0.0,

            "sentiment": "",

            "context": "",

            "response": "",

            "escalation": False,

            "history": [],

            "metadata": {},

            "tokens_used": 0,

            "latency": 0

        }

    )

    return result