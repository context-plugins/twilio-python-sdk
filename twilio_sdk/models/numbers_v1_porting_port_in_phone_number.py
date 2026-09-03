from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class NumbersV1PortingPortInPhoneNumber(SdkBaseModel):
    port_in_request_sid: OptionalNullable[str] = UNSET
    """The unique identifier for the port in request that this phone number is associated with."""

    phone_number_sid: OptionalNullable[str] = UNSET
    """The unique identifier for this phone number associated with this port in request."""

    url: OptionalNullable[str] = UNSET
    """URL reference for this resource."""

    account_sid: OptionalNullable[str] = UNSET
    """Account Sid or subaccount where the phone number(s) will be Ported."""

    phone_number_type: OptionalNullable[str] = UNSET
    """The number type of the phone number. This can be: toll-free, local, mobile or unknown. This field may be null if
    the number is not portable or if the portability for a number has not yet been evaluated."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp for when this port in phone number was created."""

    country: OptionalNullable[str] = UNSET
    """The ISO country code that this number is associated with. This field may be null if the number is not portable or
    if the portability for a number has not yet been evaluated."""

    missing_required_fields: OptionalNullable[bool] = UNSET
    """Indicates if the phone number is missing required fields such as a PIN or account number. This field may be null
    if the number is not portable or if the portability for a number has not yet been evaluated."""

    last_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp indicating when the Port In Phone Number resource was last modified."""

    phone_number: OptionalNullable[str] = UNSET
    """Phone number to be ported. This will be in the E164 Format."""

    portable: OptionalNullable[bool] = UNSET
    """If the number is portable by Twilio or not. This field may be null if the number portability has not yet been
    evaluated. If a number is not portable reference the ``not_portability_reason_code`` and ``not_portability_reason``
    fields for more details"""

    not_portability_reason: OptionalNullable[str] = UNSET
    """The not portability reason code description. This field may be null if the number is portable or if the
    portability for a number has not yet been evaluated."""

    not_portability_reason_code: OptionalNullable[int] = UNSET
    """The not portability reason code. This field may be null if the number is portable or if the portability for a
    number has not yet been evaluated."""

    port_in_phone_number_status: OptionalNullable[str] = UNSET
    """The status of the port in phone number."""

    port_out_pin: OptionalNullable[int] = UNSET
    """The pin required by the losing carrier to do the port out."""

    rejection_reason: OptionalNullable[str] = UNSET
    """The description of the rejection reason provided by the losing carrier. This field may be null if the number has
    not been rejected by the losing carrier."""

    rejection_reason_code: OptionalNullable[int] = UNSET
    """The code for the rejection reason provided by the losing carrier. This field may be null if the number has not
    been rejected by the losing carrier."""

    port_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp the phone number will be ported. This will only be set once a port date has been confirmed. Not all
    carriers can guarantee a specific time on the port date. Twilio will try its best to get the port completed by this
    time on the port date. Please subscribe to webhooks for confirmation on when a port has actually been completed."""


class NumbersV1PortingPortInPhoneNumberDict(TypedDict):
    port_in_request_sid: NotRequired[str | None]
    phone_number_sid: NotRequired[str | None]
    url: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    phone_number_type: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    country: NotRequired[str | None]
    missing_required_fields: NotRequired[bool | None]
    last_updated: NotRequired[RFC3339DateTime | None]
    phone_number: NotRequired[str | None]
    portable: NotRequired[bool | None]
    not_portability_reason: NotRequired[str | None]
    not_portability_reason_code: NotRequired[int | None]
    port_in_phone_number_status: NotRequired[str | None]
    port_out_pin: NotRequired[int | None]
    rejection_reason: NotRequired[str | None]
    rejection_reason_code: NotRequired[int | None]
    port_date: NotRequired[RFC3339DateTime | None]
