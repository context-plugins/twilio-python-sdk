from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Meta(SdkBaseModel):
    first_page_url: Optional[AnyUrl] = UNSET
    key: Optional[str] = UNSET
    next_page_url: OptionalNullable[AnyUrl] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_url: OptionalNullable[AnyUrl] = UNSET
    url: Optional[AnyUrl] = UNSET


class MetaDict(TypedDict):
    first_page_url: NotRequired[AnyUrl]
    key: NotRequired[str]
    next_page_url: NotRequired[AnyUrl | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_url: NotRequired[AnyUrl | None]
    url: NotRequired[AnyUrl]
