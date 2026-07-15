"""
Purpose:
--------
Retrieves top K documents.
"""

from app.embeddings.embedding_manager import (
    EmbeddingManager
)

from app.vector_db.vector_manager import (
    VectorManager
)


class Retriever:

    def __init__(self):

        self.embedding = (
            EmbeddingManager()
        )

        self.vector = (
            VectorManager()
        )

    def retrieve(
        self,
        query,
        top_k=5
    ):

        query_embedding = (

            self.embedding.embed_query(
                query
            )

        )

        return self.vector.search(

            query_embedding,

            top_k

        )