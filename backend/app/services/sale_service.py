from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.sale_repository import SaleRepository
from app.schemas.sale import SaleCreate, SaleUpdate


class SaleService:

    @staticmethod
    def get_all_sales(db: Session):
        return SaleRepository.get_all(db)

    @staticmethod
    def get_sale(db: Session, sale_id: int):

        sale = SaleRepository.get_by_id(db, sale_id)

        if not sale:
            raise HTTPException(
                status_code=404,
                detail="Sale not found"
            )

        return sale

    @staticmethod
    def create_sale(db: Session, sale: SaleCreate):
        return SaleRepository.create(db, sale)

    @staticmethod
    def update_sale(db: Session, sale_id: int, sale: SaleUpdate):

        db_sale = SaleRepository.get_by_id(db, sale_id)

        if not db_sale:
            raise HTTPException(
                status_code=404,
                detail="Sale not found"
            )

        return SaleRepository.update(db, db_sale, sale)

    @staticmethod
    def delete_sale(db: Session, sale_id: int):

        db_sale = SaleRepository.get_by_id(db, sale_id)

        if not db_sale:
            raise HTTPException(
                status_code=404,
                detail="Sale not found"
            )

        SaleRepository.delete(db, db_sale)

        return {
            "message": "Sale deleted successfully"
        }