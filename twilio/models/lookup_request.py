from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .lookup_request_with_cor_id import LookupRequestWithCorId, LookupRequestWithCorIdDict


class LookupRequest(SdkBaseModel):
    phone_numbers: Optional[list[LookupRequestWithCorId]] = UNSET


class LookupRequestDict(TypedDict):
    phone_numbers: NotRequired[list[LookupRequestWithCorId | LookupRequestWithCorIdDict]]
