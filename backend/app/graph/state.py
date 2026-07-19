from typing import TypedDict, Optional

from app.models.product import Product


class InventoryState(TypedDict):

    product_name: str

    product: Optional[Product]

    sales: dict

    trend: dict

    forecast: dict

    recommendation: dict

    ai_recommendation: str