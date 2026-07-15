from app.embeddings.embedding_manager import (
    EmbeddingManager
)


manager = EmbeddingManager()

vector = manager.embed_query(

    "Where is my refund?"

)

texts = [

    "refund",

    "order tracking",

    "payment failed"
]

vectors = manager.embed_documents(
    texts
)

print(len(vector))