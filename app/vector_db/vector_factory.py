"""
Purpose:
--------
Creates vector DB.
"""

from app.config.settings import (
    settings
)

from app.vector_db.chroma_store import (
    ChromaStore
)

from app.vector_db.pinecone_store import (
    PineconeStore
)


class VectorFactory:

    @staticmethod
    def create():

        if settings.VECTOR_DB == "chroma":

            return ChromaStore()

        elif settings.VECTOR_DB == "pinecone":

            return PineconeStore()

        raise ValueError(
            "Vector DB not supported."
        )