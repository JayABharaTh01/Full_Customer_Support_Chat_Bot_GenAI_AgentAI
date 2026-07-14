from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
def root():
    return {
        "application": "Enterprise Multi-Agent AI Customer Support Platform",
        "version": "1.0.0",
        "status": "Running"
    }