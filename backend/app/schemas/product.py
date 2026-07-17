from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    sku: str
    category: str
    stock_quantity: int
    minimum_stock: int
    supplier: str
    lead_time_days: int
    unit_price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    stock_quantity: int | None = None
    minimum_stock: int | None = None
    supplier: str | None = None
    lead_time_days: int | None = None
    unit_price: float | None = None


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)