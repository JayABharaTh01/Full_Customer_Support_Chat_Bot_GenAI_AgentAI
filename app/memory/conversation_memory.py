"""
Purpose:
--------
Stores conversations in memory.

Used For:
---------
Local Development.
"""

from app.memory.base_memory import (
    BaseMemory
)


class ConversationMemory(
    BaseMemory
):

    def __init__(self):

        self.memory = {}

    def save(
        self,
        session_id,
        message
    ):

        if session_id not in self.memory:

            self.memory[session_id] = []

        self.memory[session_id].append(
            message
        )

    def load(
        self,
        session_id
    ):

        return self.memory.get(
            session_id,
            []
        )

    def clear(
        self,
        session_id
    ):

        self.memory.pop(
            session_id,
            None
        )