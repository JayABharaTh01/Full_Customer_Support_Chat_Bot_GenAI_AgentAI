"""
Purpose:
--------
Local LLM support.

Examples:
---------
Llama3
Mistral
Phi
"""

from app.llm.base_llm import BaseLLM


class OllamaClient(BaseLLM):

    def generate(
        self,
        prompt
    ):

        return "Ollama Response"

    def stream(
        self,
        prompt
    ):

        pass