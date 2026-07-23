"""
Purpose:
--------
Base interface for all MCP tools.
"""

from abc import ABC
from abc import abstractmethod


class BaseTool(ABC):

    @abstractmethod
    def execute(
        self,
        **kwargs
    ):
        pass