import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.logger import get_logger


logger = get_logger("api")


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start = time.time()

        response = await call_next(request)

        duration = round(time.time() - start, 3)

        request_id = getattr(
            request.state,
            "request_id",
            "unknown"
        )

        logger.info(

            f"[{request_id}] "
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{duration}s"

        )

        return response