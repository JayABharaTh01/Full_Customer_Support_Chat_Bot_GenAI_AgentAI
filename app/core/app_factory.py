"""
Application Factory

Responsible for creating and configuring
the FastAPI application.
"""

from fastapi import FastAPI

from app.config.api_config import api_config

from app.core.lifespan import lifespan

from app.api.middleware.cors import configure_cors

from app.api.exceptions.exception_handler import (
    customer_support_exception_handler,
    generic_exception_handler,
)

from app.api.exceptions.custom_exceptions import (
    CustomerSupportException,
)

from app.api.routers.health import router as health_router

from app.api.routers.root import router as root_router
from app.api.routers.version import router as version_router


def create_app() -> FastAPI:

    app = FastAPI(

        title=api_config.TITLE,

        version=api_config.VERSION,

        description=api_config.DESCRIPTION,

        docs_url=api_config.DOCS_URL,

        redoc_url=api_config.REDOC_URL,

        openapi_url=api_config.OPENAPI_URL,

        lifespan=lifespan,

        openapi_tags=api_config.TAGS,

        contact=api_config.CONTACT,

        license_info=api_config.LICENSE,

    )

    # ------------------------
    # Middleware
    # ------------------------

    configure_cors(app)

    # ------------------------
    # Exception Handlers
    # ------------------------

    app.add_exception_handler(

        CustomerSupportException,

        customer_support_exception_handler

    )

    app.add_exception_handler(

        Exception,

        generic_exception_handler

    )

    # ------------------------
    # Routers
    # ------------------------
    app.include_router(root_router)

    app.include_router(

        health_router,

        prefix=api_config.API_PREFIX

    )

    app.include_router(
    version_router,
    prefix=api_config.API_PREFIX
    )

    
    return app