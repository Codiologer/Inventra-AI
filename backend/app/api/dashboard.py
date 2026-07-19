from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def get_dashboard_summary(
    db: Session = Depends(get_db)
):

    return DashboardService.get_summary(db)


@router.get("/alerts")
def dashboard_alerts(
    db: Session = Depends(get_db)
):

    return DashboardService.get_alerts(db)


@router.get("/top-products")
def top_products(
    db: Session = Depends(get_db)
):

    return DashboardService.get_top_products(db)


@router.get("/sales-analytics")
def sales_analytics(
    db: Session = Depends(get_db)
):

    return DashboardService.get_sales_analytics(db)