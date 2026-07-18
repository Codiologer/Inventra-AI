from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SaleBase(BaseModel):
    product_name: str
    quantity: int
    sale_price: Optional[float] = None
    sale_date: date


class SaleCreate(SaleBase):
    pass


class SaleUpdate(BaseModel):
    product_name: Optional[str] = None
    quantity: Optional[int] = None
    sale_price: Optional[float] = None
    sale_date: Optional[date] = None


class SaleResponse(SaleBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)