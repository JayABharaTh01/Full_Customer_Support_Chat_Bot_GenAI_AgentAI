"""
Purpose:
--------
Defines the interface for all memory implementations.

Future:
-------
- Conversation Memory
- Session Memory
- Redis Memory
- Long-Term Memory
"""

from abc import ABC
from abc import abstractmethod


class BaseMemory(ABC):

    @abstractmethod
    def save(self, session_id, message):
        pass

    @abstractmethod
    def load(self, session_id):
        pass

    @abstractmethod
    def clear(self, session_id):
        pass