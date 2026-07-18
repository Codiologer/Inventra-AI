from typing import Optional

from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductRepository:
    """Handles all database operations related to Product."""

    @staticmethod
    def create(db: Session, product: ProductCreate) -> Product:
        db_product = Product(**product.model_dump())

        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product

    @staticmethod
    def get_all(db: Session) -> list[Product]:
        return db.query(Product).order_by(Product.id.desc()).all()

    @staticmethod
    def get_by_id(db: Session, product_id: int) -> Optional[Product]:
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    @staticmethod
    def get_by_sku(db: Session, sku: str) -> Optional[Product]:
        return (
            db.query(Product)
            .filter(Product.sku == sku)
            .first()
        )
        
    @staticmethod
    def get_product_by_name(
        db: Session,
        product_name: str
    ) -> Optional[Product]:

        return (
            db.query(Product)
            .filter(Product.name.ilike(product_name))
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        db_product: Product,
        product: ProductUpdate
    ) -> Product:

        update_data = product.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_product, key, value)

        db.commit()
        db.refresh(db_product)

        return db_product

    @staticmethod
    def delete(
        db: Session,
        db_product: Product
    ) -> None:

        db.delete(db_product)
        db.commit()