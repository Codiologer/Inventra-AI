from fastapi import FastAPI

from app.api.product_api import router as product_router
from app.database.database import Base, engine
from app.api.trend_api import router as trend_router
from app.models.sale import Sale
from app.api.sale_routes import router as sale_router
from app.api import graph

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventra AI",
    version="1.0.0",
    description="Predictive Supply Chain Automation Platform",
)

app.include_router(product_router)
app.include_router(sale_router)
app.include_router(trend_router)
app.include_router(graph.router)

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "Inventra AI",
    }