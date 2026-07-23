# """
# Application Entry Point
# """

# from app.core.app_factory import create_app

# from app.api.routers.metrics import (
#     router as metrics_router
# )

# from app.api.routers.agents import (
#     router as agents_router
# )

# from app.api.routers.memory import (
#     router as memory_router
# )

# from app.api.routers.mcp import (
#     router as mcp_router
# )
# from app.api.routers.chat import (
#     router as chat_router
# )

# app = create_app()

# app.include_router(

#     metrics_router,

#     prefix="/api/v1",

#     tags=["Metrics"]

# )

# app.include_router(

#     agents_router,

#     prefix="/api/v1",

#     tags=["Agents"]

# )

# app.include_router(

#     memory_router,

#     prefix="/api/v1",

#     tags=["Memory"]

# )

# app.include_router(

#     mcp_router,

#     prefix="/api/v1",

#     tags=["MCP"]

# )
# app.include_router(

#     chat_router,

#     prefix="/api/v1",

#     tags=["Chat"]

# )

# #temp
# for route in app.routes:
#     print(route.path)

"""
Application Entry Point
"""

from app.core.app_factory import (
    create_app
)

app = create_app()


# Debug Routes
for route in app.routes:

    print(route.path)