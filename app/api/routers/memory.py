"""
Purpose:
--------
Expose conversation memory.
"""

from fastapi import APIRouter

from app.memory.memory_manager import (
    MemoryManager
)

router = APIRouter()

memory = MemoryManager()


@router.get(
    "/memory/{session_id}"
)
def get_memory(
    session_id: str
):

    return {

        "session_id": session_id,

        "history":

        memory.load(
            session_id
        )

    }


@router.delete(
    "/memory/{session_id}"
)
def clear_memory(
    session_id: str
):

    memory.clear(
        session_id
    )

    return {

        "message":

        "Memory cleared."
    }