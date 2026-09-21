from pydantic import BaseModel, ConfigDict
from moysklad.models.base import Meta


class Webhook(BaseModel):
    model_config = ConfigDict(extra="allow")

    meta: Meta | None = None
    id: str | None = None
    accountId: str | None = None
    entityType: str | None = None
    url: str | None = None
    method: str | None = None
    enabled: bool = True
    action: str | None = None
