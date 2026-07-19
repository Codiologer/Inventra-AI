from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.graph.state import InventoryState
from app.services.product_service import ProductService


def load_product_node(
    state: InventoryState
):

    db: Session = SessionLocal()

    try:

        product = ProductService.get_product_by_name(
            db,
            state["product_name"]
        )

        state["product"] = product

        return state

    finally:

        db.close()