from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.sale import SaleCreate, SaleUpdate, SaleResponse
from app.services.sale_service import SaleService

router = APIRouter(
    prefix="/api/v1/sales",
    tags=["Sales"]
)


@router.get("", response_model=List[SaleResponse])
def get_sales(db: Session = Depends(get_db)):
    return SaleService.get_all_sales(db)


@router.get("/{sale_id}", response_model=SaleResponse)
def get_sale(
    sale_id: int,
    db: Session = Depends(get_db)
):
    return SaleService.get_sale(db, sale_id)


@router.post("", response_model=SaleResponse, status_code=201)
def create_sale(
    sale: SaleCreate,
    db: Session = Depends(get_db)
):
    return SaleService.create_sale(db, sale)


@router.put("/{sale_id}", response_model=SaleResponse)
def update_sale(
    sale_id: int,
    sale: SaleUpdate,
    db: Session = Depends(get_db)
):
    return SaleService.update_sale(db, sale_id, sale)


@router.delete("/{sale_id}")
def delete_sale(
    sale_id: int,
    db: Session = Depends(get_db)
):
    return SaleService.delete_sale(db, sale_id)