from app.graph.state import InventoryState
from app.services.forecast_service import ForecastService


def load_forecast_node(
    state: InventoryState
):

    product = state["product"]

    sales = state["sales"]

    trend = state["trend"]

    forecast = ForecastService.calculate_forecast(

        stock=product.stock_quantity,

        daily_sales=sales["daily_sales"],

        trend_score=trend["trend_score"],

        lead_time=product.lead_time_days

    )

    state["forecast"] = forecast

    print("Forecast Node Executed")
    print(state["forecast"])
    print(forecast)

    return state