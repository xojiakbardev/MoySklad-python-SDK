from pydantic import BaseModel, ConfigDict
from moysklad.models.base import Meta
from typing import Any


class StockRow(BaseModel):
    model_config = ConfigDict(extra="allow")

    meta: Meta
    assortmentId: str | None = None
    name: str | None = None
    code: str | None = None
    article: str | None = None
    stock: float | None = None
    inTransit: float | None = None
    reserve: float | None = None
    quantity: float | None = None
    price: float | None = None
    salePrice: float | None = None
    folder: dict[str, Any] | None = None
