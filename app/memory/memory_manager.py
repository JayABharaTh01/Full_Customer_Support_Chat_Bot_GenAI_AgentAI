"""
Purpose:
--------
Main entry point for memory.
"""

from app.memory.conversation_memory import (
    ConversationMemory
)


class MemoryManager:

    def __init__(self):

        self.memory = (
            ConversationMemory()
        )

    def save(
        self,
        session_id,
        message
    ):

        self.memory.save(
            session_id,
            message
        )

    def load(
        self,
        session_id
    ):

        return self.memory.load(
            session_id
        )

    def clear(
        self,
        session_id
    ):

        self.memory.clear(
            session_id
        )