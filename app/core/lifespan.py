from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.startup import startup

from app.core.shutdown import shutdown


@asynccontextmanager
async def lifespan(app: FastAPI):

    startup()

    yield

    shutdown()