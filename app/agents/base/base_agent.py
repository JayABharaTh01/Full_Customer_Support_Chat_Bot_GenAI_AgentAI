"""
Purpose:
--------
Every agent must implement execute().

Benefits:
---------
- Standard interface
- Supports LangGraph
- Easy testing
"""

from abc import ABC
from abc import abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    def execute(
        self,
        state
    ):
        pass