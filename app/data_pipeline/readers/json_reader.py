"""
Purpose:
--------
Reads JSON files.
"""

import json

from app.data_pipeline.readers.base_reader import (
    BaseReader
)


class JSONReader(BaseReader):

    def validate(self, file_path):

        return True

    def read(self, file_path):

        with open(file_path) as f:

            data = json.load(f)

        return str(data)