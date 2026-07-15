"""
Purpose:
--------
Factory for document readers.

Benefits:
---------
- Centralized reader creation.
- Easy to add new formats.
"""

from app.data_pipeline.readers.pdf_reader import PDFReader
from app.data_pipeline.readers.docx_reader import DOCXReader
from app.data_pipeline.readers.txt_reader import TXTReader
from app.data_pipeline.readers.csv_reader import CSVReader
from app.data_pipeline.readers.json_reader import JSONReader


class ReaderFactory:

    READERS = {

        ".pdf": PDFReader(),

        ".docx": DOCXReader(),

        ".txt": TXTReader(),

        ".csv": CSVReader(),

        ".json": JSONReader()

    }

    @classmethod
    def get_reader(cls, extension):

        if extension not in cls.READERS:

            raise ValueError(
                f"Unsupported file: {extension}"
            )

        return cls.READERS[extension]