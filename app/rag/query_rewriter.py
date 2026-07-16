"""
Purpose:
--------
Improves customer queries before retrieval.

Examples:
---------
Can I return it?

↓

Can I return my recently purchased order?
"""


class QueryRewriter:

    def rewrite(
        self,
        query: str
    ):return query