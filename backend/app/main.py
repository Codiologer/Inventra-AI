from fastapi import FastAPI

from app.api.product_api import router as product_router
from app.database.database import Base, engine
from app.api.trend_api import router as trend_router
from app.models.sale import Sale
from app.api.sale_routes import router as sale_router
from app.api import graph
from app.api.ai import router as ai_router
from app.api.dashboard import router as dashboard_router
from app.assistant.router import router as assistant_router



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
app.include_router(ai_router)
app.include_router(dashboard_router)
app.include_router(assistant_router)

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "Inventra AI",
    }