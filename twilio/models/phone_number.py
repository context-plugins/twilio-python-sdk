from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PhoneNumber(SdkBaseModel):
    phone_number: Optional[str] = UNSET
    label: Optional[str] = UNSET


class PhoneNumberDict(TypedDict):
    phone_number: NotRequired[str]
    label: NotRequired[str]
