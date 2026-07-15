import sys

from app.utils.logger import get_logger

logger = get_logger("api")


def check_environment():

    logger.info(
        f"Python Version: {sys.version}"
    )