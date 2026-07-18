from pydantic import BaseModel


class ForecastResponse(BaseModel):

    success: bool

    product: str

    category: str

    current_stock: int

    daily_sales: float

    lead_time: int

    trend_score: int

    days_remaining: float

    risk_score: float

    risk_level: str

    recommended_order: int