from fastapi import FastAPI
from routes.translation import router
from fastapi.exceptions import RequestValidationError
from utils.exception_handlers import custom_validation_exception_handler


app = FastAPI(title="Translation Microservice")

app.add_exception_handler(RequestValidationError,
                          custom_validation_exception_handler)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
