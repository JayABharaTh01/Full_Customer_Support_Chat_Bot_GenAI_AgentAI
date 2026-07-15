"""
Purpose:
--------
Entry point for all documents.

Responsibilities:
-----------------
1. Determine extension.
2. Get reader.
3. Validate.
4. Return text.
"""

from pathlib import Path

from app.data_pipeline.factory import ReaderFactory


class DocumentLoader:

    def load(self, file_path):

        extension = Path(
            file_path
        ).suffix.lower()

        reader = ReaderFactory.get_reader(
            extension
        )

        if not reader.validate(file_path):

            raise ValueError(
                "Invalid file."
            )

        return reader.read(file_path)