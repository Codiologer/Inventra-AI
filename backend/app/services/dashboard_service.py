from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.repositories.product_repository import ProductRepository
from app.repositories.sale_repository import SaleRepository


class DashboardService:

    @staticmethod
    def get_summary(db: Session):

        total_products = ProductRepository.count_products(db)

        low_stock = ProductRepository.get_low_stock_products(db)

        critical_stock = ProductRepository.get_critical_products(db)

        total_inventory = ProductRepository.total_inventory(db)

        total_revenue = SaleRepository.get_total_revenue(db)

        total_quantity = SaleRepository.get_total_quantity(db)

        return {

            "total_products": total_products,

            "low_stock_products": len(low_stock),

            "critical_products": len(critical_stock),

            "total_inventory": total_inventory,

            "total_revenue": total_revenue,

            "total_quantity_sold": total_quantity

        }

    @staticmethod
    def get_alerts(db: Session):

        products = ProductRepository.get_all(db)

        alerts = []

        for product in products:

            if product.stock_quantity <= 20:

                alerts.append({

                    "type": "CRITICAL",

                    "product": product.name,

                    "message": f"Only {product.stock_quantity} units left."

                })

            elif product.stock_quantity <= 50:

                alerts.append({

                    "type": "LOW STOCK",

                    "product": product.name,

                    "message": f"Current stock is {product.stock_quantity}."

                })

        return alerts

    @staticmethod
    def get_top_products(db: Session):

        sales = SaleRepository.get_all(db)

        products = {}

        for sale in sales:

            if sale.product_name not in products:

                products[sale.product_name] = {

                    "product": sale.product_name,

                    "quantity_sold": 0,

                    "revenue": 0

                }

            products[sale.product_name]["quantity_sold"] += sale.quantity

            price = sale.sale_price or 0

            products[sale.product_name]["revenue"] += (

                sale.quantity * price

            )

        top_products = sorted(

            products.values(),

            key=lambda x: x["quantity_sold"],

            reverse=True

        )

        return top_products

    @staticmethod
    def get_sales_analytics(

        db: Session,

        days: int = 7

    ):

        analytics_data = {}

        today = datetime.now()

        # Prepare last N days
        for i in range(days - 1, -1, -1):

            date_str = (

                today - timedelta(days=i)

            ).strftime("%Y-%m-%d")

            analytics_data[date_str] = {

                "date": date_str,

                "sales": 0,

                "revenue": 0

            }

        sales = SaleRepository.get_all(db)

        for sale in sales:

            if sale.sale_date:

                sale_date = sale.sale_date.strftime("%Y-%m-%d")

                if sale_date in analytics_data:

                    price = sale.sale_price or 0

                    analytics_data[sale_date]["sales"] += sale.quantity

                    analytics_data[sale_date]["revenue"] += (

                        sale.quantity * price

                    )

        return list(

            analytics_data.values()

        )