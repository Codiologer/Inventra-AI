import math
from sqlalchemy.orm import Session

from app.repositories.product_repository import ProductRepository
from app.repositories.sale_repository import SaleRepository

from app.services.trend_service import TrendService


class ForecastService:

    @staticmethod
    def calculate_forecast(
        stock: int,
        daily_sales: float,
        trend_score: int,
        lead_time: int
    ):

        # Prevent division by zero
        if daily_sales <= 0:
            daily_sales = 1

        # Days until stock finishes
        days_remaining = stock / daily_sales

        # Risk Score
        risk_score = (
            (trend_score * 0.4)
            + (daily_sales * 4 * 0.4)
            + ((100 - stock) * 0.2)
        )

        # Risk Category

        if days_remaining <= lead_time:

            risk = "CRITICAL"

        elif risk_score >= 80:

            risk = "HIGH"

        elif risk_score >= 50:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        # Reorder Quantity

        recommended_order = max(
            math.ceil((lead_time + 15) * daily_sales - stock),
            0
        )

        return {

            "days_remaining": round(days_remaining, 2),

            "trend_score": trend_score,

            "risk_score": round(risk_score, 2),

            "risk_level": risk,

            "recommended_order": recommended_order
        }
        
    @staticmethod
    def get_average_daily_sales(db: Session, product_name: str):

        sales = SaleRepository.get_all_sales(db)

        total_quantity = 0

        for sale in sales:

            if sale.product_name.lower() == product_name.lower():

                total_quantity += sale.quantity

        average_daily_sales = total_quantity / 30

        return round(average_daily_sales, 2)
    
    @staticmethod
    def forecast_product(db: Session, product_name: str):

        # Get Product
        product = ProductRepository.get_product_by_name(db, product_name)

        if not product:
            return {
                "success": False,
                "message": "Product not found"
            }

        # Average Daily Sales
        daily_sales = ForecastService.get_average_daily_sales(
            db,
            product_name
        )

        # Trend Score
        trend = TrendService.get_trend(product_name)

        trend_score = trend["trend_score"]

        # Forecast Calculation
        forecast = ForecastService.calculate_forecast(
            stock=product.stock_quantity,
            daily_sales=daily_sales,
            trend_score=trend_score,
            lead_time=product.lead_time_days
        )

        return {

            "success": True,

            "product": product.name,

            "category": product.category,

            "current_stock": product.stock_quantity,

            "daily_sales": daily_sales,

            "lead_time": product.lead_time_days,

            **forecast
        }