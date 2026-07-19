from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.graph.state import InventoryState
from app.services.sale_service import SaleService


def load_sales_node(
    state: InventoryState
):

    db: Session = SessionLocal()

    try:

        product = state["product"]

        sales = SaleService.get_sales_summary(
            db,
            product.name
        )

        state["sales"] = sales

        return state

    finally:

        db.close()