from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier import Carrier, CarrierDict


class CountyCarrierValue(SdkBaseModel):
    country: Optional[str] = UNSET
    carriers: Optional[list[Carrier]] = UNSET


class CountyCarrierValueDict(TypedDict):
    country: NotRequired[str]
    carriers: NotRequired[list[Carrier | CarrierDict]]
