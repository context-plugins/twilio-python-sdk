from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_customer_profile import TrusthubV1CustomerProfile, TrusthubV1CustomerProfileDict


class ListCustomerProfileResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1CustomerProfile]] = UNSET
    meta: Optional[Meta] = UNSET


class ListCustomerProfileResponseDict(TypedDict):
    results: NotRequired[list[TrusthubV1CustomerProfile | TrusthubV1CustomerProfileDict]]
    meta: NotRequired[Meta | MetaDict]
