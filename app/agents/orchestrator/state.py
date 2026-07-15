"""
Purpose:
--------
Shared state between agents.

This object acts as the communication layer
between all agents in the system.

Every agent reads from and writes to this state.
"""

from typing import TypedDict


class AgentState(TypedDict):

    # ---------------------
    # Request Information
    # ---------------------

    request_id: str

    session_id: str

    user_id: str

    # ---------------------
    # Customer Query
    # ---------------------

    query: str

    # ---------------------
    # Intent
    # ---------------------

    intent: str

    intent_confidence: float

    # ---------------------
    # Sentiment
    # ---------------------

    sentiment: str

    # ---------------------
    # RAG
    # ---------------------

    context: str

    response: str

    # ---------------------
    # Escalation
    # ---------------------

    escalation: bool

    # ---------------------
    # Conversation
    # ---------------------

    history: list

    # ---------------------
    # Metadata
    # ---------------------

    metadata: dict

    # ---------------------
    # Performance
    # ---------------------

    tokens_used: int

    latency: float

    agent_metrics: dict