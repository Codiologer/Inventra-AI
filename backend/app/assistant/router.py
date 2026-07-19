from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.assistant.tools import InventoryTools

router = APIRouter(
    prefix="/assistant",
    tags=["AI Assistant"]
)


@router.get("/health")
def health():

    return {

        "success": True,

        "message": "AI Assistant Ready"

    }


@router.get("/summary")
def summary(

    db: Session = Depends(get_db)

):

    return InventoryTools.get_inventory_summary(db)


@router.get("/products")
def products(

    db: Session = Depends(get_db)

):

    return InventoryTools.get_products(db)


@router.get("/sales")
def sales(

    db: Session = Depends(get_db)

):

    return InventoryTools.get_sales(db)