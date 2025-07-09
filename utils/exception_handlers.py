from fastapi.requests import Request
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi import HTTPException, status


class UnsupportedLanguageException(HTTPException):
    def __init__(self, lang_code: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported language code: '{lang_code}'. Supported: hi, ta, kn, bn"
        )


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


async def unsupported_lang_exception_handler(request: Request, exc: UnsupportedLanguageException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )
