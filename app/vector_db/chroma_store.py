"""
Purpose:
--------
Local Vector DB.

Used for:
---------
Development
Testing
Local RAG
"""

import chromadb

from app.config.settings import (
    settings
)

from app.vector_db.base_vector_store import (
    BaseVectorStore
)


class ChromaStore(
    BaseVectorStore
):

    def __init__(self):

        self.client = (
            chromadb.PersistentClient(
                path=settings.CHROMA_DB_PATH
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=settings.CHROMA_COLLECTION
            )
        )

    def add_documents(

        self,

        ids,

        documents,

        embeddings,

        metadatas

    ):

        self.collection.add(

            ids=ids,

            documents=documents,

            embeddings=embeddings,

            metadatas=metadatas

        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        return self.collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=top_k

        )

    def delete(
        self,
        ids
    ):

        self.collection.delete(
            ids=ids
        )

    def count(self):

        return self.collection.count()