from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaginationMeta1(SdkBaseModel):
    """Pagination metadata containing navigation tokens and result information, this schema should according to
    convention be added to the response payload's 'meta' attribute"""

    key: str
    """The key of the list property contains the actual data items. This enables programmatic iteration over paginated
    results."""

    page_size: int = Field(alias="pageSize")
    """The actual number of items returned in this response. May be less than the requested pageSize for the last
    page."""

    previous_token: OptionalNullable[str] = Field(default=UNSET, alias="previousToken")
    """Token to fetch the previous page of results. Only included if there is a previous page, otherwise omitted."""

    next_token: OptionalNullable[str] = Field(default=UNSET, alias="nextToken")
    """Token to fetch the next page of results. Only included if there is a next page, otherwise omitted."""


class PaginationMeta1Dict(TypedDict):
    key: str
    page_size: int
    previous_token: NotRequired[str | None]
    next_token: NotRequired[str | None]
