from fastapi import FastAPI

from app.api.product_api import router as product_router
from app.database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventra AI",
    version="1.0.0",
    description="Predictive Supply Chain Automation Platform",
)

app.include_router(product_router)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "Inventra AI",
    }