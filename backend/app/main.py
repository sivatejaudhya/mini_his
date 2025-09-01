from fastapi import FastAPI
from .config import settings  # import settings
from app.routes import auth

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/health")
def root():
    return {
        "message": f"{settings.PROJECT_NAME} backend is alive 🚀",
        "version": settings.VERSION,
    }
