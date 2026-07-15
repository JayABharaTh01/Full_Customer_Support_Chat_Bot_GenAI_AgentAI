import sys

from pathlib import Path

from app.data_pipeline.document_loader import (
    DocumentLoader
)

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

loader = DocumentLoader()

text = loader.load(
    "data/raw/sample.pdf"
)

print(text[:1000])