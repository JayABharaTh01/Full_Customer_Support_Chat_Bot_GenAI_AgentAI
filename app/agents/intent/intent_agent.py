"""
Purpose:
--------
Determines customer intent.
"""

from app.agents.base.base_agent import (
    BaseAgent
)


class IntentAgent(
    BaseAgent
):

    def execute(
        self,
        state
    ):

        query = state["query"]

        if "refund" in query:

            state["intent"] = "refund"

            state["intent_confidence"] = 0.95

        elif "order" in query:

            state["intent"] = "order"

            state["intent_confidence"] = 0.90

        else:

            state["intent"] = "unknown"

            state["intent_confidence"] = 0.50

        return state