from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaginationMeta(SdkBaseModel):
    previous_token: Optional[str] = UNSET
    next_token: Optional[str] = UNSET


class PaginationMetaDict(TypedDict):
    previous_token: NotRequired[str]
    next_token: NotRequired[str]
