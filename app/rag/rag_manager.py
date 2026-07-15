"""
Purpose:
--------
Main RAG entry point.
"""

from app.rag.rag_pipeline import (
    RAGPipeline
)


class RAGManager:

    def __init__(self):

        self.pipeline = (
            RAGPipeline()
        )

    def ask(
        self,
        query
    ):

        return self.pipeline.run(
            query
        )