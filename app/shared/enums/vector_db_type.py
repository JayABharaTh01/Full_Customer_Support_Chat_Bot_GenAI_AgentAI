from enum import Enum


class VectorDBType(str, Enum):

    CHROMA = "chroma"

    PINECONE = "pinecone"