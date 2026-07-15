"""
Purpose:
--------
Abstract embedding interface.

Every embedding model in the project
must implement:

1. embed_query()
2. embed_documents()
"""

from abc import ABC
from abc import abstractmethod


class BaseEmbedding(ABC):

    @abstractmethod
    def embed_query(
        self,
        text: str
    ):
        pass

    @abstractmethod
    def embed_documents(
        self,
        texts: list[str]
    ):
        pass