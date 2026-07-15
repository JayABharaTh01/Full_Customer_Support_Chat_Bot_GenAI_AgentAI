"""
Purpose:
--------
Creates embedding providers.
"""

from app.config.settings import settings

from app.embeddings.openai_embedding import (
    OpenAIEmbedding
)

from app.embeddings.sentence_transformer_embedding import (
    SentenceTransformerEmbedding
)


class EmbeddingFactory:

    @staticmethod
    def create():

        provider = settings.EMBEDDING_PROVIDER

        if provider == "openai":

            return OpenAIEmbedding()

        elif provider == "sentence_transformers":

            return (
                SentenceTransformerEmbedding()
            )

        raise ValueError(
            "Embedding Provider Not Supported"
        )