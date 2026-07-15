"""
Purpose:
--------
Production Vector DB.

Used for:
---------
AWS Deployment
Large Scale Retrieval
"""

from pinecone import Pinecone

from app.config.settings import (
    settings
)

from app.vector_db.base_vector_store import (
    BaseVectorStore
)


class PineconeStore(
    BaseVectorStore
):

    def __init__(self):

        self.client = Pinecone(

            api_key=settings.PINECONE_API_KEY
        )

        self.index = self.client.Index(

            settings.PINECONE_INDEX_NAME
        )

    def add_documents(

        self,

        ids,

        documents,

        embeddings,

        metadatas

    ):

        vectors = []

        for i in range(
            len(ids)
        ):

            vectors.append(

                {

                    "id": ids[i],

                    "values": embeddings[i],

                    "metadata": {

                        "text": documents[i],

                        **metadatas[i]

                    }

                }

            )

        self.index.upsert(
            vectors
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        return self.index.query(

            vector=query_embedding,

            top_k=top_k,

            include_metadata=True

        )

    def delete(
        self,
        ids
    ):

        self.index.delete(
            ids=ids
        )

    def count(self):

        stats = (
            self.index.describe_index_stats()
        )

        return stats["total_vector_count"]