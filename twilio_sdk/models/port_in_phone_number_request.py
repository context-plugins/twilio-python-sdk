from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.rejection_reason import RejectionReasonOrStr


class PortInPhoneNumberRequest(SdkBaseModel):
    port_in_phone_number_sid: str
    """The SID of the Port In Phone Number resource that is being updated."""

    port_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp the phone number will be ported. This will only be set once a port date has been confirmed. Not all
    carriers can guarantee a specific time on the port date. Twilio will try its best to get the port completed by this
    time on the port date."""

    rejection_reason: OptionalNullable[RejectionReasonOrStr] = UNSET
    """The description of the rejection reason provided by the losing carrier. This field may be null if the number has
    not been rejected by the losing carrier."""


class PortInPhoneNumberRequestDict(TypedDict):
    port_in_phone_number_sid: str
    port_date: NotRequired[RFC3339DateTime | None]
    rejection_reason: NotRequired[RejectionReasonOrStr | None]
