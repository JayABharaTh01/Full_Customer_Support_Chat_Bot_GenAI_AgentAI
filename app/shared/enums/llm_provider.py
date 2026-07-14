from enum import Enum


class LLMProvider(str, Enum):

    OPENAI = "openai"

    BEDROCK = "bedrock"

    OLLAMA = "ollama"

    HUGGINGFACE = "huggingface"