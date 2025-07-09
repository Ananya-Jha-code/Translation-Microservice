from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import request_validation_exception_handler


async def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    for err in errors:
        if (
            err["loc"] == ("body", "text")
            and err["type"] == "value_error.any_str.max_length"
        ):
            return JSONResponse(
                status_code=400,
                content={"error": "Text too long. Max 1000 characters allowed."}
            )

    return await request_validation_exception_handler(request, exc)
