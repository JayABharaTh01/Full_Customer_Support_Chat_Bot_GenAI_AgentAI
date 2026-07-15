"""
Purpose:
--------
Determines if human support is required.
"""

from app.agents.base.base_agent import (
    BaseAgent
)


class EscalationAgent(
    BaseAgent
):

    def execute(
        self,
        state
    ):

        state["escalation"] = (

            state["sentiment"]

            == "negative"

        )

        return state