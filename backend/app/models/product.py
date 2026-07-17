from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    sku = Column(String(50), unique=True, nullable=False)

    category = Column(String(100), nullable=False)

    stock_quantity = Column(Integer, default=0)

    minimum_stock = Column(Integer, default=10)

    supplier = Column(String(150))

    lead_time_days = Column(Integer, default=3)

    unit_price = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )