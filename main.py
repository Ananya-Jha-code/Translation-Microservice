from fastapi import FastAPI
from routes.translation import router

app = FastAPI(title="Translation Microservice")

# Include the translation routes
app.include_router(router)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
