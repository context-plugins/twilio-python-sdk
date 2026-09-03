from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination_meta import PaginationMeta, PaginationMetaDict
from .sender_id_country import SenderIdCountry, SenderIdCountryDict


class SenderIdCountriesResponsePage(SdkBaseModel):
    results: Optional[list[SenderIdCountry]] = UNSET
    """List of countries associated with the Sender ID."""

    meta: Optional[PaginationMeta] = UNSET


class SenderIdCountriesResponsePageDict(TypedDict):
    results: NotRequired[list[SenderIdCountry | SenderIdCountryDict]]
    meta: NotRequired[PaginationMeta | PaginationMetaDict]
