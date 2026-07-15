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

        elif "order" in query:

            state["intent"] = "order"

        else:

            state["intent"] = "unknown"

        return state