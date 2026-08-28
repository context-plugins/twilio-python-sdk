from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_item import CatalogItem, CatalogItemDict


class TwilioCatalog(SdkBaseModel):
    """twilio/catalog type lets recipients view list of catalog products, ask questions about products, order
    products."""

    title: Optional[str] = UNSET
    body: str
    subtitle: Optional[str] = UNSET
    id: Optional[str] = UNSET
    items: Optional[list[CatalogItem]] = UNSET
    dynamic_items: Optional[str] = UNSET


class TwilioCatalogDict(TypedDict):
    title: NotRequired[str]
    body: str
    subtitle: NotRequired[str]
    id: NotRequired[str]
    items: NotRequired[list[CatalogItem | CatalogItemDict]]
    dynamic_items: NotRequired[str]
