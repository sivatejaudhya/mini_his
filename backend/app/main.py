from fastapi import FastAPI
from .config import settings  # import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

@app.get("/health")
def root():
    return {
        "message": f"{settings.PROJECT_NAME} backend is alive 🚀",
        "version": settings.VERSION
    }
