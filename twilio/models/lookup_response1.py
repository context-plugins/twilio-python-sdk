from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .lookup_batch_response import LookupBatchResponse, LookupBatchResponseDict


class LookupResponse1(SdkBaseModel):
    phone_numbers: Optional[list[LookupBatchResponse]] = UNSET


class LookupResponse1Dict(TypedDict):
    phone_numbers: NotRequired[list[LookupBatchResponse | LookupBatchResponseDict]]
