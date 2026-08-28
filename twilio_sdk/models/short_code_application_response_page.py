from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .short_code_application import ShortCodeApplication, ShortCodeApplicationDict


class ShortCodeApplicationResponsePage(SdkBaseModel):
    total_elements: Optional[int] = UNSET
    total_pages: Optional[int] = UNSET
    current_page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    has_next: Optional[bool] = UNSET
    has_prev: Optional[bool] = UNSET
    results: Optional[list[ShortCodeApplication]] = UNSET
    """List of Short Code Applications."""


class ShortCodeApplicationResponsePageDict(TypedDict):
    total_elements: NotRequired[int]
    total_pages: NotRequired[int]
    current_page: NotRequired[int]
    per_page: NotRequired[int]
    has_next: NotRequired[bool]
    has_prev: NotRequired[bool]
    results: NotRequired[list[ShortCodeApplication | ShortCodeApplicationDict]]
