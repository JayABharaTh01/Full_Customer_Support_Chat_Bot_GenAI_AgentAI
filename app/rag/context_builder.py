"""
Purpose:
--------
Builds context from retrieved documents.
"""


class ContextBuilder:

    def build(
        self,
        results
    ):

        context = []

        documents = results.get(
            "documents",
            [[]]
        )[0]

        for document in documents:

            context.append(
                document
            )

        return "\n\n".join(
            context
        )