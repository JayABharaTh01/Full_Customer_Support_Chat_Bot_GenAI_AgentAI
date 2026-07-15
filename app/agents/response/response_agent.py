"""
Purpose:
--------
Generates final response.
"""

from app.agents.base.base_agent import (
    BaseAgent
)


class ResponseAgent(
    BaseAgent
):

    def execute(
        self,
        state
    ):

        state["response"] = (

            state["context"]

        )

        return state