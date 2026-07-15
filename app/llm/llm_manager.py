"""
Purpose:
--------
Main LLM entry point.
"""

from app.llm.llm_factory import (
    LLMFactory
)


class LLMManager:

    def __init__(self):

        self.llm = (

            LLMFactory.create()

        )

    def generate(
        self,
        prompt
    ):

        return self.llm.generate(
            prompt
        )