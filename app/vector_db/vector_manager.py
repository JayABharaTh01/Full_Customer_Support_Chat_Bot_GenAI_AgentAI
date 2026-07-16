"""
Purpose:
--------
Main entry point.
"""

from app.vector_db.vector_factory import (
    VectorFactory
)


# class VectorManager:

#     def __init__(self):

#         self.store = (
#             VectorFactory.create()
#         )

#     # def add_documents(
#     #     self,
#     #     *args
#     # ):

#     #     return (
#     #         self.store.add_documents(
#     #             *args
#     #         )
#     #     )
#     def add_documents(
#         self,
#         ids,
#         documents,
#         embeddings,
#         metadatas
#     ):
#         return self.store.add_documents(
#             ids=ids,
#             documents=documents,
#             embeddings=embeddings,
#             metadatas=metadatas
#         )


#     def search(
#         self,
#         *args
#     ):

#         return (
#             self.store.search(
#                 *args
#             )
#         )

#     def delete(
#         self,
#         *args
#     ):

#         return (
#             self.store.delete(
#                 *args
#             )
#         )

#     def count(self):

#         return self.store.count()


class VectorManager:

    def __init__(self):

        self.store = VectorFactory.create()

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas
    ):

        return self.store.add_documents(

            ids=ids,

            documents=documents,

            embeddings=embeddings,

            metadatas=metadatas

        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        return self.store.search(

            query_embedding=query_embedding,

            top_k=top_k

        )

    def delete(
        self,
        ids
    ):

        return self.store.delete(ids)

    def count(self):

        return self.store.count()