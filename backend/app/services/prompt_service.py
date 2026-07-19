class PromptService:

    @staticmethod
    def inventory_prompt(

        product,

        sales,

        trend,

        forecast,

        recommendation

    ):

        return f"""
You are an expert Inventory Management AI.

Analyze the following inventory data.

Product Name:
{product.name}

Category:
{product.category}

Current Stock:
{product.stock_quantity}

Minimum Stock:
{product.minimum_stock}

Lead Time:
{product.lead_time_days} days

Daily Sales:
{sales["daily_sales"]}

Total Quantity Sold:
{sales["total_quantity"]}

Total Sales Amount:
{sales["total_sales"]}

Google Trend Score:
{trend["trend_score"]}

Forecast:

Days Remaining:
{forecast["days_remaining"]}

Risk Level:
{forecast["risk_level"]}

Risk Score:
{forecast["risk_score"]}

Recommended Order:
{forecast["reorder_quantity"]}

Current Rule Based Recommendation:

Action:
{recommendation["action"]}

Priority:
{recommendation["priority"]}

Reason:
{recommendation["reason"]}

Respond ONLY in the following format:

Summary:
...

Business Risk:
...

Recommendation:
...

Reason:
...
"""