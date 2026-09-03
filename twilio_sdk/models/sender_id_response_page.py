from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination_meta import PaginationMeta, PaginationMetaDict
from .sender_id import SenderId, SenderIdDict


class SenderIdResponsePage(SdkBaseModel):
    results: Optional[list[SenderId]] = UNSET
    """List of Sender IDs."""

    meta: Optional[PaginationMeta] = UNSET


class SenderIdResponsePageDict(TypedDict):
    results: NotRequired[list[SenderId | SenderIdDict]]
    meta: NotRequired[PaginationMeta | PaginationMetaDict]
