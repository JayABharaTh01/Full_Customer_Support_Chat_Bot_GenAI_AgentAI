"""
Purpose:
--------
Reads CSV files.

Future:
-------
- DataFrame support
- Column filtering
"""

import pandas as pd

from app.data_pipeline.readers.base_reader import (
    BaseReader
)


class CSVReader(BaseReader):

    def validate(self, file_path):

        return True

    def read(self, file_path):

        df = pd.read_csv(file_path)

        return df.to_string()