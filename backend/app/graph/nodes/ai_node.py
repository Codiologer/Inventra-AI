from app.graph.state import InventoryState
from app.services.ai_service import AIService


def ai_node(state: InventoryState):

    product = state["product"]

    sales = state["sales"]

    trend = state["trend"]

    forecast = state["forecast"]

    recommendation = state["recommendation"]


    print("=" * 50)
    print("PRODUCT =", product)
    print("SALES =", sales)
    print("TREND =", trend)
    print("FORECAST =", forecast)
    print("RECOMMENDATION =", recommendation)
    print("=" * 50)

    prompt = f"""
        You are an expert Inventory and Supply Chain Consultant.

        Analyze the following inventory data.

        Product Name:
        {product.name}

        Category:
        {product.category}

        Current Stock:
        {product.stock_quantity}

        Supplier:
        {product.supplier}

        Daily Sales:
        {sales["daily_sales"]}

        Total Quantity Sold:
        {sales["total_quantity"]}

        Trend:
        {trend["trend"]}

        Trend Score:
        {trend["trend_score"]}

        Risk Level:
        {forecast["risk_level"]}

        Days Remaining:
        {forecast["days_remaining"]}

        Recommended Order Quantity:
        {forecast["reorder_quantity"]}

        System Recommendation:
        {recommendation["message"]}

        Provide:

        1. Inventory Analysis
        2. Business Risk
        3. Recommended Action
        4. Final Summary

        Maximum 120 words.
        """

    print(prompt)

    response = AIService.generate_inventory_analysis(prompt)

    state["ai_recommendation"] = response

    return state