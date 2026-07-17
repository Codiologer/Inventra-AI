from fastapi import FastAPI

from app.database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventra AI",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "Inventra AI"
    }