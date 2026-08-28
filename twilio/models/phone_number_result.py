from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class PhoneNumberResult(SdkBaseModel):
    not_portability_reason: OptionalNullable[str] = UNSET
    """The not portability reason code description. This field may be null if the number is portable or if the
    portability for a number has not yet been evaluated."""

    not_portability_reason_code: OptionalNullable[int] = UNSET
    """The not portability reason code. This field may be null if the number is portable or if the portability for a
    number has not yet been evaluated."""

    number_type: OptionalNullable[str] = UNSET
    """The number type of the phone number. This can be: toll-free, local, mobile or unknown. This field may be null if
    the number is not portable or if the portability for a number has not yet been evaluated."""

    phone_number: Optional[str] = UNSET
    """Phone number to be ported. This will be in the E164 Format."""

    port_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp the phone number will be ported. This will only be set once a port date has been confirmed. Not all
    carriers can guarantee a specific time on the port date. Twilio will try its best to get the port completed by this
    time on the port date. Please subscribe to webhooks for confirmation on when a port has actually been completed."""

    port_in_phone_number_sid: Optional[str] = UNSET
    """The SID of the Phone number. This is a unique identifier of the phone number."""

    port_in_phone_number_status: Optional[str] = UNSET
    """The status of the port in phone number."""

    portable: OptionalNullable[bool] = UNSET
    """Whether the number is portable by Twilio or not. This field may be null if the number portability has not yet
    been evaluated. If a number is not portable reference the ``not_portability_reason_code`` and
    ``not_portability_reason`` fields for more details"""

    rejection_reason: OptionalNullable[str] = UNSET
    """The description of the rejection reason provided by the losing carrier. This field may be null if the number has
    not been rejected by the losing carrier."""

    rejection_reason_code: OptionalNullable[str] = UNSET
    """The code for the rejection reason provided by the losing carrier. This field may be null if the number has not
    been rejected by the losing carrier."""

    status_last_time_updated_timestamp: OptionalNullable[str] = UNSET
    """Timestamp indicating when the Port In Phone Number resource was last modified."""

    external_porting_vendor_phone_number_id: OptionalNullable[str] = UNSET


class PhoneNumberResultDict(TypedDict):
    not_portability_reason: NotRequired[str | None]
    not_portability_reason_code: NotRequired[int | None]
    number_type: NotRequired[str | None]
    phone_number: NotRequired[str]
    port_date: NotRequired[RFC3339DateTime | None]
    port_in_phone_number_sid: NotRequired[str]
    port_in_phone_number_status: NotRequired[str]
    portable: NotRequired[bool | None]
    rejection_reason: NotRequired[str | None]
    rejection_reason_code: NotRequired[str | None]
    status_last_time_updated_timestamp: NotRequired[str | None]
    external_porting_vendor_phone_number_id: NotRequired[str | None]
