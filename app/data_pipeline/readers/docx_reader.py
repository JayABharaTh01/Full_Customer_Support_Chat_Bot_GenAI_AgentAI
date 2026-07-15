"""
Purpose:
--------
Reads Microsoft Word documents.
"""

from pathlib import Path

import docx

from app.data_pipeline.readers.base_reader import (
    BaseReader
)


class DOCXReader(BaseReader):

    def validate(self, file_path):

        return Path(file_path).exists()

    def read(self, file_path):

        document = docx.Document(file_path)

        return "\n".join(

            paragraph.text

            for paragraph in document.paragraphs
        )