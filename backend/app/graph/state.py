from typing import TypedDict


class InventoryState(TypedDict):

    product_name: str

    product: dict

    sales: dict

    trend: dict

    forecast: dict

    recommendation: dict