"""
Database Dependency
"""

from app.config.settings import settings


def get_database():

    if settings.DATABASE_TYPE == "sqlite":

        return "SQLite"

    elif settings.DATABASE_TYPE == "postgres":

        return "PostgreSQL"

    raise ValueError(
        "Database not supported."
    )