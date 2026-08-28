from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CatalogItem(SdkBaseModel):
    id: Optional[str] = UNSET
    section_title: Optional[str] = UNSET
    name: Optional[str] = UNSET
    media_url: Optional[str] = UNSET
    price: Optional[float] = UNSET
    description: Optional[str] = UNSET


class CatalogItemDict(TypedDict):
    id: NotRequired[str]
    section_title: NotRequired[str]
    name: NotRequired[str]
    media_url: NotRequired[str]
    price: NotRequired[float]
    description: NotRequired[str]
