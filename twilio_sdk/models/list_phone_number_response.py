from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_service_phone_number import MessagingV1ServicePhoneNumber, MessagingV1ServicePhoneNumberDict
from .meta import Meta, MetaDict


class ListPhoneNumberResponse(SdkBaseModel):
    phone_numbers: Optional[list[MessagingV1ServicePhoneNumber]] = UNSET
    meta: Optional[Meta] = UNSET


class ListPhoneNumberResponseDict(TypedDict):
    phone_numbers: NotRequired[list[MessagingV1ServicePhoneNumber | MessagingV1ServicePhoneNumberDict]]
    meta: NotRequired[Meta | MetaDict]
