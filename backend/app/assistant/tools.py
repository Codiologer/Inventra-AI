from sqlalchemy.orm import Session

from app.repositories.product_repository import ProductRepository
from app.repositories.sale_repository import SaleRepository


class InventoryTools:

    @staticmethod
    def get_inventory_summary(db: Session):

        return {

            "total_products": ProductRepository.count_products(db),

            "low_stock": len(
                ProductRepository.get_low_stock_products(db)
            ),

            "critical_stock": len(
                ProductRepository.get_critical_products(db)
            ),

            "inventory": ProductRepository.total_inventory(db),

            "revenue": SaleRepository.get_total_revenue(db),

            "quantity_sold": SaleRepository.get_total_quantity(db)

        }


    @staticmethod
    def get_products(db: Session):

        products = ProductRepository.get_all(db)

        return [

            {

                "name": p.name,

                "category": p.category,

                "stock": p.stock_quantity,

                "supplier": p.supplier,

                "lead_time": p.lead_time_days

            }

            for p in products

        ]


    @staticmethod
    def get_sales(db: Session):

        sales = SaleRepository.get_all(db)

        return [

            {

                "product": s.product_name,

                "quantity": s.quantity,

                "price": s.sale_price,

                "date": str(s.sale_date)

            }

            for s in sales

        ]