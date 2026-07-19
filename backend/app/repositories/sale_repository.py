from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.schemas.sale import SaleCreate, SaleUpdate


class SaleRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Sale).all()

    @staticmethod
    def get_by_id(db: Session, sale_id: int):
        return db.query(Sale).filter(Sale.id == sale_id).first()

    @staticmethod
    def create(db: Session, sale: SaleCreate):

        db_sale = Sale(
            product_name=sale.product_name,
            quantity=sale.quantity,
            sale_price=sale.sale_price,
            sale_date=sale.sale_date
        )

        db.add(db_sale)
        db.commit()
        db.refresh(db_sale)

        return db_sale

    @staticmethod
    def update(db: Session, db_sale: Sale, sale: SaleUpdate):

        update_data = sale.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_sale, key, value)

        db.commit()
        db.refresh(db_sale)

        return db_sale

    @staticmethod
    def delete(db: Session, db_sale: Sale):

        db.delete(db_sale)
        db.commit()
        
    @staticmethod
    def get_sales_by_product(
        db: Session,
        product_name: str
    ):
        return (
            db.query(Sale)
            .filter(Sale.product_name.ilike(f"%{product_name}%"))
            .order_by(Sale.sale_date.desc())
            .all()
    )