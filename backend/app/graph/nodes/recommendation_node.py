from app.graph.state import InventoryState
from app.services.recommendation_service import RecommendationService


def recommendation_node(

    state: InventoryState

):

    recommendation = RecommendationService.generate_recommendation(

        state["product"],

        state["sales"],

        state["trend"],

        state["forecast"]

    )

    state["recommendation"] = recommendation

    return state