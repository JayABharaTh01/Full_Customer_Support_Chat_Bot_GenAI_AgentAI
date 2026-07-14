"""
FastAPI Application Configuration

This module centralizes all API-related settings.

Responsibilities:
- API metadata
- Versioning
- Swagger
- OpenAPI
- CORS
- Middleware registration
"""

from app.config.settings import settings


class APIConfig:
    """Application API configuration."""

    TITLE = settings.PROJECT_NAME

    VERSION = settings.VERSION

    DESCRIPTION = """
    Enterprise Multi-Agent Customer Support Platform

    Features
    --------
    • Multi-Agent AI
    • RAG Pipeline
    • Conversation Memory
    • Sentiment Analysis
    • Escalation
    • FastAPI Backend
    """

    API_PREFIX = settings.API_PREFIX

    DOCS_URL = "/docs"

    REDOC_URL = "/redoc"

    OPENAPI_URL = "/openapi.json"

    CONTACT = {
        "name": "Development Team",
        "email": "support@example.com",
    }

    LICENSE = {
        "name": "MIT"
    }

    TAGS = [

        {
            "name": "Health",
            "description": "Application Health APIs"
        },

        {
            "name": "Chat",
            "description": "Customer Chat APIs"
        },

        {
            "name": "Authentication",
            "description": "Login APIs"
        },

        {
            "name": "Knowledge Base",
            "description": "RAG APIs"
        }

    ]


api_config = APIConfig()