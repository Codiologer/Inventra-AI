from fastapi import APIRouter

from app.services.trend_service import TrendService

router = APIRouter(
    prefix="/api/v1/trends",
    tags=["Trends"]
)


@router.get("/{keyword}")
def get_trend(keyword: str):

    return TrendService.get_google_trend(keyword)