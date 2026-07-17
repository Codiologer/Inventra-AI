from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String, nullable=False)

    quantity = Column(Integer, nullable=False)

    sale_price = Column(Float, nullable=True)

    sale_date = Column(Date, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())