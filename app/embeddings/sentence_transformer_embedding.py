"""
Purpose:
--------
Local embedding implementation.

Model:
------
all-MiniLM-L6-v2

Dimension:
----------
384
"""

from sentence_transformers import (
    SentenceTransformer
)

from app.embeddings.base_embedding import (
    BaseEmbedding
)


class SentenceTransformerEmbedding(
    BaseEmbedding
):

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed_query(
        self,
        text: str
    ):

        return self.model.encode(
            text
        ).tolist()

    def embed_documents(
        self,
        texts: list[str]
    ):

        return self.model.encode(
            texts,
            batch_size=64,
            show_progress_bar=True
        ).tolist()