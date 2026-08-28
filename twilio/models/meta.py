from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Meta(SdkBaseModel):
    first_page_url: Optional[str] = UNSET
    key: Optional[str] = UNSET
    next_page_url: OptionalNullable[str] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_url: OptionalNullable[str] = UNSET
    url: Optional[str] = UNSET


class MetaDict(TypedDict):
    first_page_url: NotRequired[str]
    key: NotRequired[str]
    next_page_url: NotRequired[str | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_url: NotRequired[str | None]
    url: NotRequired[str]
