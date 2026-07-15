from uuid import uuid4

from app.vector_db.vector_manager import (
    VectorManager
)

vector = VectorManager()

vector.add_documents(

    ids=[str(uuid4())],

    documents=[
        "Refund takes 5 days."
    ],

    embeddings=[
        [0.1] * 384
    ],

    metadatas=[
        {

            "source": "policy.pdf"

        }
    ]

)

print(

    vector.count()

)

from app.vector_db.retriever import (
    Retriever
)

retriever = Retriever()

print(

    retriever.retrieve(

        "How long does refund take?"

    )

)