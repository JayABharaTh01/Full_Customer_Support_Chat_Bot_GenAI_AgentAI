"""
Purpose:
--------
Reads PDF documents.

Future:
-------
- OCR Support
- Scanned PDFs
- Metadata extraction
"""

from pathlib import Path

from pypdf import PdfReader

from app.data_pipeline.readers.base_reader import (
    BaseReader
)


class PDFReader(BaseReader):

    def validate(self, file_path):

        return Path(file_path).exists()

    def read(self, file_path):

        reader = PdfReader(file_path)

        text = []

        for page in reader.pages:

            text.append(
                page.extract_text()
            )

        return "\n".join(text)