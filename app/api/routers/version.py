"""
Version Router
"""

from fastapi import APIRouter

from app.config.settings import settings

router = APIRouter(
    prefix="/version",
    tags=["System"],
)


@router.get("/")
async def get_version():
    return {
        "success": True,
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
    }