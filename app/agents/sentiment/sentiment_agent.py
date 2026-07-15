"""
Purpose:
--------
Detects customer sentiment.
"""

from app.agents.base.base_agent import (
    BaseAgent
)


class SentimentAgent(
    BaseAgent
):

    def execute(
        self,
        state
    ):

        query = state["query"]

        if "angry" in query:

            state["sentiment"] = "negative"

        else:

            state["sentiment"] = "neutral"

        return state