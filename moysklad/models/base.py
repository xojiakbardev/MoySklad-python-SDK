from typing import Generic, TypeVar, Any
from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class Meta(BaseModel):
    model_config = ConfigDict(extra="allow")

    href: str
    metadataHref: str | None = None
    type: str | None = None
    mediaType: str | None = None
    uuidHref: str | None = None
    downloadHref: str | None = None
    downloadPermanentHref: str | None = None
    # Поля пагинации присутствуют в meta списков.
    size: int | None = None
    limit: int | None = None
    offset: int | None = None


class ContextEmployee(BaseModel):
    model_config = ConfigDict(extra="allow")
    meta: Meta


class Context(BaseModel):
    model_config = ConfigDict(extra="allow")
    employee: ContextEmployee | None = None


class ListResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(extra="allow")
    context: Context | None = None
    meta: Meta
    rows: list[T] = []


class BaseEntity(BaseModel):
    # Состав полей в ответах МойСклад зависит от тарифа/типа сущности.
    # extra=allow: salePrices, images, characteristics и т.п. не теряются.
    model_config = ConfigDict(extra="allow")

    meta: Meta
    id: str | None = None
    accountId: str | None = None
    updated: str | None = None
    name: str | None = None


class BaseDocument(BaseEntity):
    moment: str | None = None
    applicable: bool | None = None
    sum: float | None = None
    description: str | None = None
    state: dict[str, Any] | None = None
    organization: dict[str, Any] | None = None
