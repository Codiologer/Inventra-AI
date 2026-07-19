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