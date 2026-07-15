"""
Purpose:
--------
Runs RAG retrieval.
"""

from app.agents.base.base_agent import (
    BaseAgent
)

from app.rag.rag_manager import (
    RAGManager
)


class RetrievalAgent(
    BaseAgent
):

    def __init__(self):

        self.rag = RAGManager()

    def execute(
        self,
        state
    ):

        state["context"] = self.rag.ask(
            state["query"]
        )

        return state