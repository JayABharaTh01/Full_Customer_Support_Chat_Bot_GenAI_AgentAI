"""
Vector Store Dependency
"""

from app.config.settings import settings


def get_vector_store():

    db = settings.VECTOR_DB.lower()

    if db == "chroma":

        return "ChromaDB"

    elif db == "pinecone":

        return "Pinecone"

    raise ValueError(
        f"Unsupported Vector DB: {db}"
    )