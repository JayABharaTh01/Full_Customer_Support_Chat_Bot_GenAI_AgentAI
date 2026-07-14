from datetime import datetime

from fastapi import APIRouter

from app.config.settings import settings


router = APIRouter(

    prefix="/health",

    tags=["Health"]

)


@router.get("/")

def health_check():

    return {

        "success": True,

        "status": "healthy",

        "project": settings.PROJECT_NAME,

        "version": settings.VERSION,

        "environment": settings.ENVIRONMENT,

        "timestamp": datetime.utcnow().isoformat()

    }