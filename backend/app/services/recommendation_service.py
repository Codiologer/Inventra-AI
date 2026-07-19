class RecommendationService:

    @staticmethod
    def generate_recommendation(

        product,
        sales,
        trend,
        forecast

    ):

        risk = forecast["risk_level"]

        trend_score = trend["trend_score"]

        recommendation = {}

        if risk == "CRITICAL":

            recommendation = {

                "action": "Order Immediately",

                "priority": "High",

                "message":
                "Stock is likely to run out very soon.",

                "reorder_quantity":
                forecast["reorder_quantity"]

            }

        elif risk == "HIGH":

            recommendation = {

                "action": "Reorder Soon",

                "priority": "Medium",

                "message":
                "Demand is increasing.",

                "reorder_quantity":
                forecast["reorder_quantity"]
            }

        elif trend_score >= 70:

            recommendation = {

                "action": "Increase Inventory",

                "priority": "Medium",

                "message":
                "Trend score is very high."

            }

        else:

            recommendation = {

                "action": "No Action Needed",

                "priority": "Low",

                "message":
                "Current inventory is sufficient."

            }

        return recommendation