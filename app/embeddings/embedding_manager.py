"""
Purpose:
--------
Main embedding entry point.
"""

from app.embeddings.embedding_factory import (
    EmbeddingFactory
)


class EmbeddingManager:

    def __init__(self):

        self.embedding = (
            EmbeddingFactory.create()
        )

    def embed_query(
        self,
        text
    ):

        return self.embedding.embed_query(
            text
        )

    def embed_documents(
        self,
        texts
    ):

        return (
            self.embedding.embed_documents(
                texts
            )
        )