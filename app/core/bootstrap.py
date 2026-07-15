from pathlib import Path

from app.utils.logger import get_logger

logger = get_logger("api")


DIRECTORIES = [

    "logs",

    "data/raw",

    "data/processed",

    "data/embeddings",

    "database"

]


def bootstrap():

    logger.info("Bootstrapping application...")

    for directory in DIRECTORIES:

        Path(directory).mkdir(
            parents=True,
            exist_ok=True
        )

        logger.info(
            f"Created: {directory}"
        )