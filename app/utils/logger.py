"""
Central Logger

Import this everywhere.

Example:

from app.utils.logger import get_logger

logger = get_logger("agent")
"""

from loguru import logger


def get_logger(module: str):

    return logger.bind(module=module)