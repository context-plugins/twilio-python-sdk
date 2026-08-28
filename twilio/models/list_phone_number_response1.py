from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .proxy_v1_service_phone_number import ProxyV1ServicePhoneNumber, ProxyV1ServicePhoneNumberDict


class ListPhoneNumberResponse1(SdkBaseModel):
    phone_numbers: Optional[list[ProxyV1ServicePhoneNumber]] = UNSET
    meta: Optional[Meta] = UNSET


class ListPhoneNumberResponse1Dict(TypedDict):
    phone_numbers: NotRequired[list[ProxyV1ServicePhoneNumber | ProxyV1ServicePhoneNumberDict]]
    meta: NotRequired[Meta | MetaDict]
