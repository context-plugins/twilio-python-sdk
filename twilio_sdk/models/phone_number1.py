from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PhoneNumber1(SdkBaseModel):
    phone_number: str
    """Phone number to be ported. This must be in the E164 Format."""

    pin: Optional[str] = UNSET
    """Some losing carriers require a PIN to authorize the port of a phone number. If the phone number is a US mobile
    phone number, the PIN is mandatory to process a porting request. Other carriers and number types may also require a
    PIN, you'll need to contact the losing carrier to determine what your phone number's PIN is."""


class PhoneNumber1Dict(TypedDict):
    phone_number: str
    pin: NotRequired[str]
