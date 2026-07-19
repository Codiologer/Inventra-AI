from app.graph.state import InventoryState
from app.services.trend_service import TrendService


def load_trend_node(
    state: InventoryState
):

    product = state["product"]

    trend = TrendService.get_google_trend(
        product.name
    )

    state["trend"] = trend

    print("Trend Node Executed")
    print(state["trend"])

    return state