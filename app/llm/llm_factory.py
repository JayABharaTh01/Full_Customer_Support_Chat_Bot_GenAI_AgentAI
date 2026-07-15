"""
Purpose:
--------
Creates LLM providers.
"""

from app.config.settings import settings

from app.llm.openai_client import (
    OpenAIClient
)

from app.llm.ollama_client import (
    OllamaClient
)


class LLMFactory:

    @staticmethod
    def create():

        provider = settings.LLM_PROVIDER

        if provider == "openai":

            return OpenAIClient()

        elif provider == "ollama":

            return OllamaClient()

        raise ValueError(
            "LLM not supported."
        )