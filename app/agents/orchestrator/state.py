"""
Purpose:
--------
Shared state between agents.
"""

from typing import TypedDict


class AgentState(TypedDict):

class AgentState(TypedDict):

    request_id: str

    session_id: str

    query: str

    intent: str

    intent_confidence: float

    sentiment: str

    context: str

    response: str

    escalation: bool

    history: list

    metadata: dict