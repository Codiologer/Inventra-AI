from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    """Business logic for Product operations."""

    @staticmethod
    def create_product(db: Session, product: ProductCreate) -> Product:

        # Check duplicate SKU
        existing_product = ProductRepository.get_by_sku(db, product.sku)

        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="SKU already exists."
            )

        # Business Validations
        if product.stock_quantity < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Stock cannot be negative."
            )

        if product.minimum_stock < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Minimum stock cannot be negative."
            )

        if product.unit_price < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unit price cannot be negative."
            )

        if product.lead_time_days <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Lead time must be greater than zero."
            )

        return ProductRepository.create(db, product)

    @staticmethod
    def get_all_products(db: Session):

        return ProductRepository.get_all(db)

    @staticmethod
    def get_product(db: Session, product_id: int):

        product = ProductRepository.get_by_id(db, product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found."
            )

        return product

    @staticmethod
    def update_product(
        db: Session,
        product_id: int,
        product: ProductUpdate
    ):

        db_product = ProductRepository.get_by_id(db, product_id)

        if not db_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found."
            )

        return ProductRepository.update(
            db,
            db_product,
            product
        )

    @staticmethod
    def delete_product(
        db: Session,
        product_id: int
    ):

        db_product = ProductRepository.get_by_id(db, product_id)

        if not db_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found."
            )

        ProductRepository.delete(db, db_product)

        return {
            "message": "Product deleted successfully."
        }