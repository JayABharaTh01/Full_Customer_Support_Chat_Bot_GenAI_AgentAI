"""
Enterprise Logging Configuration

Supports:
- Console logging
- File logging
- Error logging
- Agent logging
- API logging
- RAG logging
- LLM logging
"""

from pathlib import Path
from loguru import logger
import sys

from app.config.settings import settings


class LoggingConfig:

    def __init__(self):

        self.log_dir = Path(settings.LOG_DIR)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.configure()

    def configure(self):

        logger.remove()

        # -----------------------------
        # Console Logger
        # -----------------------------
        logger.add(
            sys.stdout,
            level=settings.LOG_LEVEL,
            colorize=True,
            enqueue=True,
            backtrace=True,
            diagnose=True,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                   "<level>{level: <8}</level> | "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
                   "<level>{message}</level>"
        )

        # -----------------------------
        # Application Log
        # -----------------------------
        logger.add(
            self.log_dir / "application.log",
            rotation="10 MB",
            retention="30 days",
            compression="zip",
            level="INFO",
            enqueue=True,
            encoding="utf-8"
        )

        # -----------------------------
        # Error Log
        # -----------------------------
        logger.add(
            self.log_dir / "error.log",
            level="ERROR",
            rotation="10 MB",
            retention="60 days",
            compression="zip",
            enqueue=True
        )

        # -----------------------------
        # API Log
        # -----------------------------
        logger.add(
            self.log_dir / "api.log",
            filter=lambda record: record["extra"].get("module") == "api",
            rotation="10 MB",
            retention="15 days",
            enqueue=True
        )

        # -----------------------------
        # Agent Log
        # -----------------------------
        logger.add(
            self.log_dir / "agents.log",
            filter=lambda record: record["extra"].get("module") == "agent",
            rotation="10 MB",
            retention="15 days",
            enqueue=True
        )

        # -----------------------------
        # RAG Log
        # -----------------------------
        logger.add(
            self.log_dir / "rag.log",
            filter=lambda record: record["extra"].get("module") == "rag",
            rotation="10 MB",
            retention="15 days",
            enqueue=True
        )

        # -----------------------------
        # LLM Log
        # -----------------------------
        logger.add(
            self.log_dir / "llm.log",
            filter=lambda record: record["extra"].get("module") == "llm",
            rotation="10 MB",
            retention="15 days",
            enqueue=True
        )


logging_config = LoggingConfig()