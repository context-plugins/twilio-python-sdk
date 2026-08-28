from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Paging(SdkBaseModel):
    """Paging metadata for the list."""

    uri: OptionalNullable[str] = UNSET
    next_page_uri: OptionalNullable[str] = UNSET
    previous_page_uri: OptionalNullable[str] = UNSET
    page_size: OptionalNullable[int] = UNSET
    num_pages: OptionalNullable[int] = UNSET
    total: OptionalNullable[int] = UNSET
    before_sid: OptionalNullable[str] = UNSET
    after_sid: OptionalNullable[str] = UNSET


class PagingDict(TypedDict):
    uri: NotRequired[str | None]
    next_page_uri: NotRequired[str | None]
    previous_page_uri: NotRequired[str | None]
    page_size: NotRequired[int | None]
    num_pages: NotRequired[int | None]
    total: NotRequired[int | None]
    before_sid: NotRequired[str | None]
    after_sid: NotRequired[str | None]
