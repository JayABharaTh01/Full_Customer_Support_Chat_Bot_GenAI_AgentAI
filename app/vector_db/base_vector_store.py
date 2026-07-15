"""
Purpose:
--------
Abstract vector store interface.

Every vector database must implement:

1. add_documents()
2. search()
3. delete()
4. count()
"""

from abc import ABC
from abc import abstractmethod


class BaseVectorStore(ABC):

    @abstractmethod
    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas
    ):
        pass

    @abstractmethod
    def search(
        self,
        query_embedding,
        top_k=5
    ):
        pass

    @abstractmethod
    def delete(
        self,
        ids
    ):
        pass

    @abstractmethod
    def count(self):
        pass