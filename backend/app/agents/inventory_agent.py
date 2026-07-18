from sqlalchemy.orm import Session

from app.services.forecast_service import ForecastService


class InventoryAgent:

    @staticmethod
    def analyze_product(
        db: Session,
        product_name: str
    ):

        forecast = ForecastService.forecast_product(
            db,
            product_name
        )

        if not forecast["success"]:
            return forecast

        risk = forecast["risk_level"]

        if risk == "CRITICAL":

            priority = "URGENT"

            action = (
                "Immediately create a Purchase Order "
                "and notify the inventory manager."
            )

        elif risk == "HIGH":

            priority = "HIGH"

            action = (
                "Reorder stock within 24 hours."
            )

        elif risk == "MEDIUM":

            priority = "MEDIUM"

            action = (
                "Monitor inventory daily."
            )

        else:

            priority = "LOW"

            action = (
                "No action required."
            )

        return {

            **forecast,

            "priority": priority,

            "recommended_action": action
        }