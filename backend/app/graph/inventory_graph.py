from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.graph.state import InventoryState
from app.graph.nodes.product_node import load_product_node
from app.graph.nodes.sales_node import load_sales_node
from app.graph.nodes.trend_node import load_trend_node
from app.graph.nodes.forecast_node import load_forecast_node
from app.graph.nodes.recommendation_node import recommendation_node
from app.graph.nodes.ai_node import ai_node


workflow = StateGraph(InventoryState)

workflow.add_node(
    "load_product",
    load_product_node
)

workflow.add_node(
    "load_sales",
    load_sales_node
)

workflow.add_node(
    "load_trend",
    load_trend_node
)

workflow.add_node(
    "load_forecast",
    load_forecast_node
)

workflow.add_node(

    "recommendation",

    recommendation_node

)

workflow.add_node(

    "ai",

    ai_node

)


workflow.add_edge(
    START,
    "load_product"
)

workflow.add_edge(
    "load_product",
    "load_sales"
)

workflow.add_edge(
    "load_sales",
    "load_trend"
)

workflow.add_edge(
    "load_trend",
    "load_forecast"
)

workflow.add_edge(

    "load_forecast",

    "recommendation"

)

workflow.add_edge(

    "recommendation",

    "ai"

)

workflow.add_edge(

    "ai",

    END

)

inventory_graph = workflow.compile()