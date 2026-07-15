"""
Purpose:
--------
Abstract LLM interface.

All LLM providers must implement:

1. generate()
2. stream()
"""

from abc import ABC
from abc import abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str
    ):
        pass

    @abstractmethod
    def stream(
        self,
        prompt: str
    ):
        pass