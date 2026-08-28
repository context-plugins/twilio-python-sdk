from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination_meta1 import PaginationMeta1, PaginationMeta1Dict


class InsightsQueryResponse(SdkBaseModel):
    domain: Optional[str] = UNSET
    """Indicates the business domain the query was executed against"""

    items: Optional[list[Any]] = UNSET
    """Array of result objects containing the query results. Each object contains properties matching the requested
    measures and dimensions."""

    meta: Optional[PaginationMeta1] = UNSET
    """Pagination metadata containing navigation tokens and result information, this schema should according to
    convention be added to the response payload's 'meta' attribute"""


class InsightsQueryResponseDict(TypedDict):
    domain: NotRequired[str]
    items: NotRequired[list[Any]]
    meta: NotRequired[PaginationMeta1 | PaginationMeta1Dict]
