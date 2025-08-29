from fastapi import FastAPI

app = FastAPI(title="Mini_HIS", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "healthy"}
