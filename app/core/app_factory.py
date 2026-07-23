# """
# Purpose:
# --------
# Creates and configures the FastAPI application.
# """

# from fastapi import FastAPI

# from app.core.startup import startup
# from app.core.shutdown import shutdown

# # Existing Routers
# from app.api.routers.root import router as root_router
# from app.api.routers.health import router as health_router
# from app.api.routers.version import router as version_router

# # New Routers
# from app.api.routers.chat import router as chat_router
# from app.api.routers.metrics import router as metrics_router
# from app.api.routers.agents import router as agents_router
# from app.api.routers.memory import router as memory_router
# from app.api.routers.mcp import router as mcp_router


# def create_app():

#     app = FastAPI(

#         title="Customer Support AI",

#         version="1.0.0"

#     )

#     # ------------------------------------
#     # Startup / Shutdown Events
#     # ------------------------------------

#     @app.on_event("startup")
#     async def on_startup():

#         await startup()

#     @app.on_event("shutdown")
#     async def on_shutdown():

#         await shutdown()

#     # ------------------------------------
#     # Register Routers
#     # ------------------------------------

#     app.include_router(
#         root_router
#     )

#     app.include_router(
#         health_router,
#         prefix="/api/v1",
#         tags=["Health"]
#     )

#     app.include_router(
#         version_router,
#         prefix="/api/v1",
#         tags=["Version"]
#     )

#     app.include_router(
#         chat_router,
#         prefix="/api/v1",
#         tags=["Chat"]
#     )

#     app.include_router(
#         metrics_router,
#         prefix="/api/v1",
#         tags=["Metrics"]
#     )

#     app.include_router(
#         agents_router,
#         prefix="/api/v1",
#         tags=["Agents"]
#     )

#     app.include_router(
#         memory_router,
#         prefix="/api/v1",
#         tags=["Memory"]
#     )

#     app.include_router(
#         mcp_router,
#         prefix="/api/v1",
#         tags=["MCP"]
#     )

#     return app


"""
Purpose:
--------
Creates and configures the FastAPI application.
"""

from fastapi import FastAPI

from app.core.startup import startup
from app.core.shutdown import shutdown

# Existing Routers
from app.api.routers.root import (
    router as root_router
)

from app.api.routers.health import (
    router as health_router
)

from app.api.routers.version import (
    router as version_router
)

# New Routers
from app.api.routers.chat import (
    router as chat_router
)

from app.api.routers.metrics import (
    router as metrics_router
)

from app.api.routers.agents import (
    router as agents_router
)

from app.api.routers.memory import (
    router as memory_router
)

from app.api.routers.mcp import (
    router as mcp_router
)


def create_app():

    app = FastAPI(

        title="Customer Support AI",

        version="1.0.0"

    )

    # -----------------------------
    # Startup
    # -----------------------------

    @app.on_event(
        "startup"
    )
    async def on_startup():

        await startup()

    # -----------------------------
    # Shutdown
    # -----------------------------

    @app.on_event(
        "shutdown"
    )
    async def on_shutdown():

        await shutdown()

    # -----------------------------
    # Register Routers
    # -----------------------------

    app.include_router(
        root_router
    )

    app.include_router(
        health_router,
        prefix="/api/v1",
        tags=["Health"]
    )

    app.include_router(
        version_router,
        prefix="/api/v1",
        tags=["Version"]
    )

    app.include_router(
        chat_router,
        prefix="/api/v1",
        tags=["Chat"]
    )

    app.include_router(
        metrics_router,
        prefix="/api/v1",
        tags=["Metrics"]
    )

    app.include_router(
        agents_router,
        prefix="/api/v1",
        tags=["Agents"]
    )

    app.include_router(
        memory_router,
        prefix="/api/v1",
        tags=["Memory"]
    )

    app.include_router(
        mcp_router,
        prefix="/api/v1",
        tags=["MCP"]
    )

    return app