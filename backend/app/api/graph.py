from fastapi import APIRouter

from app.graph.inventory_graph import inventory_graph

router = APIRouter(
    prefix="/graph",
    tags=["LangGraph"]
)


@router.get("/health")

def graph_health():

    state = {

        "product_name": "Rice",

        "product": {},

        "sales": {},

        "trend": {},

        "forecast": {},

        "recommendation": {}
    }

    result = inventory_graph.invoke(state)

    return {

        "message": "LangGraph Working",

        "graph_result": result
    }