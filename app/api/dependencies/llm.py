"""
LLM Dependency

Provides the configured LLM client.
"""

from app.config.settings import settings


def get_llm():

    provider = settings.LLM_PROVIDER.lower()

    if provider == "openai":

        return "OpenAI Client"

    elif provider == "bedrock":

        return "Bedrock Client"

    elif provider == "ollama":

        return "Ollama Client"

    raise ValueError(
        f"Unsupported LLM Provider: {provider}"
    )