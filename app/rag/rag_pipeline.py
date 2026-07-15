"""
Purpose:
--------
Executes the complete RAG workflow.
"""

# from app.rag.query_rewriter import (
#     QueryRewriter
# )

# from app.rag.context_builder import (
#     ContextBuilder
# )

# from app.rag.prompt_builder import (
#     PromptBuilder
# )

# from app.rag.response_validator import (
#     ResponseValidator
# )

# from app.vector_db.retriever import (
#     Retriever
# )
from app.rag.query_rewriter import QueryRewriter

from app.rag.context_builder import ContextBuilder

from app.rag.prompt_builder import PromptBuilder

from app.rag.response_validator import ResponseValidator

from app.vector_db.retriever import Retriever

from app.llm.llm_manager import LLMManager


class RAGPipeline:

    def __init__(self):

        # self.rewriter = (
        #     QueryRewriter()
        # )

        # self.retriever = (
        #     Retriever()
        # )

        # self.context = (
        #     ContextBuilder()
        # )

        # self.prompt = (
        #     PromptBuilder()
        # )

        # self.validator = (
        #     ResponseValidator()
        # )
        self.rewriter = QueryRewriter()

        self.retriever = Retriever()

        self.context = ContextBuilder()

        self.prompt = PromptBuilder()

        self.validator = ResponseValidator()

        self.llm = LLMManager()

    def run(
        self,
        query
    ):

        query = self.rewriter.rewrite(
            query
        )

        results = self.retriever.retrieve(
            query
        )

        context = self.context.build(
            results
        )

        prompt = self.prompt.build(

            context,

            query

        )

        #return prompt
        response = self.llm.generate(
            prompt
        )
        return response