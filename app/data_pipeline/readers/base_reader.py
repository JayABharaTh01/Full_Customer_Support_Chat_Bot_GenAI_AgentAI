"""
Purpose:
--------
This is the abstract base class for all document readers.

Every reader in the system must implement:

1. read()
2. validate()

Examples:
---------
PDFReader
DOCXReader
CSVReader
JSONReader

Benefits:
---------
- Standard interface
- Easy extensibility
- Supports Factory Pattern
"""

from abc import ABC, abstractmethod


class BaseReader(ABC):

    @abstractmethod
    def validate(self, file_path: str) -> bool:
        """
        Validate whether the file exists and
        is supported.
        """
        pass

    @abstractmethod
    def read(self, file_path: str) -> str:
        """
        Reads file and returns text.
        """
        pass