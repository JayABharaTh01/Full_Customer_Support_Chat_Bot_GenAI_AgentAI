"""
Global Exception Handler
"""

from fastapi import Request
from fastapi.responses import JSONResponse

from app.api.exceptions.custom_exceptions import CustomerSupportException

from app.utils.logger import get_logger

logger = get_logger("api")


async def customer_support_exception_handler(
    request: Request,
    exc: CustomerSupportException
):

    logger.error(
        f"{exc.error_code} | {exc.message}"
    )

    return JSONResponse(

        status_code=exc.status_code,

        content={

            "success": False,

            "error_code": exc.error_code,

            "message": exc.message

        }

    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(str(exc))

    return JSONResponse(

        status_code=500,

        content={

            "success": False,

            "error_code": "INTERNAL_SERVER_ERROR",

            "message": "Something went wrong."

        }

    )