from fastapi import FastAPI
from routes.translation import router
from fastapi.exceptions import RequestValidationError
from utils.exception_handlers import custom_validation_exception_handler


app = FastAPI(title="Translation Microservice")


# Register the custom handler
app.add_exception_handler(RequestValidationError,
                          custom_validation_exception_handler)

# Include the translation routes
app.include_router(router)

# Health check endpoint


@app.get("/health")
def health_check():
    return {"status": "ok"}
