"""
Global application settings.

This is the single source of truth for configuration.
Every other config module imports `settings` from here.
"""

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ==========================
    # Project
    # ==========================
    PROJECT_NAME: str = "Full Customer Support Chat Bot GenAI AgentAI"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # ==========================
    # API
    # ==========================
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_PREFIX: str = "/api/v1"

    # ==========================
    # Logging
    # ==========================
    LOG_LEVEL: str = "INFO"
    LOG_DIR: str = "logs"

    # ==========================
    # LLM
    # ==========================
    LLM_PROVIDER: str = "openai"

    OPENAI_API_KEY: str = Field(default="")
    OPENAI_MODEL: str = "gpt-4o-mini"

    # Future
    BEDROCK_MODEL: str = ""
    BEDROCK_REGION: str = ""

    # ==========================
    # Embeddings
    # ==========================
    EMBEDDING_PROVIDER: str = "sentence_transformers"

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    EMBEDDING_DIMENSION: int = 384

    EMBEDDING_BATCH_SIZE: int = 64

    # ==========================
    # Vector DB
    # ==========================
    VECTOR_DB: str = "chroma"

    CHROMA_COLLECTION: str = "customer_support"

    CHROMA_DB_PATH: str = "./data/chroma_db"

    PINECONE_API_KEY: str = ""
    PINECONE_INDEX_NAME: str = ""
    PINECONE_ENVIRONMENT: str = ""

    # ==========================
    # Database
    # ==========================
    DATABASE_TYPE: str = "sqlite"

    SQLITE_DB: str = "./database/customer_support.db"

    POSTGRES_HOST: str = ""
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""

    # ==========================
    # Memory
    # ==========================
    MEMORY_WINDOW: int = 10

    SESSION_TIMEOUT: int = 30

    # ==========================
    # Retrieval
    # ==========================
    TOP_K: int = 5

    SIMILARITY_THRESHOLD: float = 0.75

    # ==========================
    # Prompt
    # ==========================
    MAX_TOKENS: int = 512

    TEMPERATURE: float = 0.2

    # ==========================
    # Security
    # ==========================
    SECRET_KEY: str = "change_me"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()