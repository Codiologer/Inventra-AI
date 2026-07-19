from fastapi import APIRouter

from app.graph.inventory_graph import inventory_graph

router = APIRouter(
    prefix="/graph",
    tags=["LangGraph"]
)


@router.get("/analyze/{product_name}")
def analyze_product(product_name: str):

    state = {

        "product_name": product_name,

        "product": {},

        "sales": {},

        "trend": {},

        "forecast": {},

        "recommendation": {},

        "ai_recommendation": ""
    }

    result = inventory_graph.invoke(state)

    return {

        "success": True,

        "graph_result": result
    }


@router.get("/health")
def graph_health():

    return analyze_product("Rice")