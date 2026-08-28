from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .losing_carrier_information import LosingCarrierInformation, LosingCarrierInformationDict
from .phone_number_result import PhoneNumberResult, PhoneNumberResultDict


class NumbersV1PortingPortIn(SdkBaseModel):
    port_in_request_sid: OptionalNullable[str] = UNSET
    """The SID of the Port In request. This is a unique identifier of the port in request."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this Port In request"""

    account_sid: OptionalNullable[str] = UNSET
    """Account Sid or subaccount where the phone number(s) will be Ported"""

    notification_emails: Optional[list[str | None]] = UNSET
    """Additional emails to send a copy of the signed LOA to."""

    target_port_in_date: OptionalNullable[Date] = UNSET
    """Target date to port the number. We cannot guarantee that this date will be honored by the other carriers, please
    work with Ops to get a confirmation of the firm order commitment (FOC) date. Expected format is ISO Local Date,
    example: ‘2011-12-03`. This date must be at least 7 days in the future for US ports and 10 days in the future for
    Japanese ports. If a start and end range is provided, the date will be converted to its UTC equivalent with the
    ranges as reference and stored in UTC. We can't guarantee the exact date and time, as this depends on the losing
    carrier."""

    target_port_in_time_range_start: OptionalNullable[str] = UNSET
    """The earliest time that the port should occur on the target port in date. Expected format is ISO Offset Time,
    example: ‘10:15:00-08:00'. We can't guarantee the exact date and time, as this depends on the losing carrier. The
    time will be stored and returned as UTC standard timezone."""

    target_port_in_time_range_end: OptionalNullable[str] = UNSET
    """The latest time that the port should occur on the target port in date. Expected format is ISO Offset Time,
    example: ‘10:15:00-08:00'. We can't guarantee the exact date and time, as this depends on the losing carrier. The
    time will be stored and returned as UTC standard timezone."""

    port_in_request_status: OptionalNullable[str] = UNSET
    """The status of the port in request. The possible values are: In progress, Completed, Expired, In review, Waiting
    for Signature, Action Required, and Canceled."""

    order_cancellation_reason: OptionalNullable[str] = UNSET
    """If the order is cancelled this field will provide further context on the cause of the cancellation."""

    losing_carrier_information: Optional[LosingCarrierInformation] = UNSET
    phone_numbers: Optional[list[PhoneNumberResult | None]] = UNSET
    bundle_sid: OptionalNullable[str] = UNSET
    """The bundle sid is an optional identifier to reference a group of regulatory documents for a port request."""

    portability_advance_carrier: OptionalNullable[str] = UNSET
    """A field only required for Japan port in requests. It is a unique identifier for the donor carrier service the
    line is being ported from."""

    auto_cancel_approval_numbers: OptionalNullable[str] = UNSET
    """Japan specific field, indicates the number of phone numbers to automatically approve for cancellation."""

    documents: Optional[list[str | None]] = UNSET
    """List of document SIDs for all phone numbers included in the port in request. At least one document SID referring
    to a document of the type Utility Bill is required."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    support_ticket_id: Optional[int] = UNSET
    """Unique ID of the request's support ticket"""

    signature_request_url: OptionalNullable[AnyUrl] = UNSET


class NumbersV1PortingPortInDict(TypedDict):
    port_in_request_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    account_sid: NotRequired[str | None]
    notification_emails: NotRequired[list[str | None]]
    target_port_in_date: NotRequired[Date | None]
    target_port_in_time_range_start: NotRequired[str | None]
    target_port_in_time_range_end: NotRequired[str | None]
    port_in_request_status: NotRequired[str | None]
    order_cancellation_reason: NotRequired[str | None]
    losing_carrier_information: NotRequired[LosingCarrierInformation | LosingCarrierInformationDict]
    phone_numbers: NotRequired[list[PhoneNumberResult | PhoneNumberResultDict | None]]
    bundle_sid: NotRequired[str | None]
    portability_advance_carrier: NotRequired[str | None]
    auto_cancel_approval_numbers: NotRequired[str | None]
    documents: NotRequired[list[str | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    support_ticket_id: NotRequired[int]
    signature_request_url: NotRequired[AnyUrl | None]
