"""
Purpose:
--------
Reads plain text files.
"""

from pathlib import Path

from app.data_pipeline.readers.base_reader import (
    BaseReader
)


class TXTReader(BaseReader):

    def validate(self, file_path):

        return Path(file_path).exists()

    def read(self, file_path):

        with open(
            file_path,
            encoding="utf-8"
        ) as f:

            return f.read()