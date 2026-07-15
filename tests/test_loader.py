from app.data_pipeline.document_loader import (
    DocumentLoader
)


loader = DocumentLoader()

text = loader.load(
    "data/raw/sample.pdf"
)

print(text[:1000])