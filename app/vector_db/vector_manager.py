"""
Purpose:
--------
Main entry point.
"""

from app.vector_db.vector_factory import (
    VectorFactory
)


class VectorManager:

    def __init__(self):

        self.store = (
            VectorFactory.create()
        )

    def add_documents(
        self,
        *args
    ):

        return (
            self.store.add_documents(
                *args
            )
        )

    def search(
        self,
        *args
    ):

        return (
            self.store.search(
                *args
            )
        )

    def delete(
        self,
        *args
    ):

        return (
            self.store.delete(
                *args
            )
        )

    def count(self):

        return self.store.count()