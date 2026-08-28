from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .losing_carrier_information import LosingCarrierInformation, LosingCarrierInformationDict
from .phone_number1 import PhoneNumber1, PhoneNumber1Dict


class PortInRequest(SdkBaseModel):
    account_sid: str
    """Account Sid or subaccount where the phone number(s) will be Ported"""

    documents: list[str]
    """List of document SIDs for all phone numbers included in the port in request. At least one document SID referring
    to a document of the type Utility Bill is required."""

    phone_numbers: Optional[list[PhoneNumber1]] = UNSET
    """List of phone numbers to be ported. Maximum of 1,000 phone numbers per request."""

    losing_carrier_information: LosingCarrierInformation
    notification_emails: Optional[list[str | None]] = UNSET
    """Additional emails to send a copy of the signed LOA to."""

    target_port_in_date: OptionalNullable[Date] = UNSET
    """Target date to port the number. We cannot guarantee that this date will be honored by the other carriers, please
    work with Ops to get a confirmation of the firm order commitment (FOC) date. Expected format is ISO Local Date,
    example: ‘2011-12-03`. This date must be at least 7 days in the future for US ports and 10 days in the future for
    Japanese ports. We can't guarantee the exact date and time, as this depends on the losing carrier"""

    target_port_in_time_range_start: OptionalNullable[str] = UNSET
    """The earliest time that the port should occur on the target port in date. Expected format is ISO Offset Time,
    example: ‘10:15:00-08:00'. We can't guarantee the exact date and time, as this depends on the losing carrier"""

    target_port_in_time_range_end: OptionalNullable[str] = UNSET
    """The latest time that the port should occur on the target port in date. Expected format is ISO Offset Time,
    example: ‘10:15:00-08:00'. We can't guarantee the exact date and time, as this depends on the losing carrier"""

    bundle_sid: OptionalNullable[str] = UNSET
    """The bundle sid is an optional identifier to reference a group of regulatory documents for a port request."""

    portability_advance_carrier: OptionalNullable[str] = UNSET
    """A field only required for Japan port in requests. It is a unique identifier for the donor carrier service the
    line is being ported from."""

    auto_cancel_approval_numbers: OptionalNullable[str] = UNSET
    """Japan specific field, indicates the number of phone numbers to automatically approve for cancellation."""


class PortInRequestDict(TypedDict):
    account_sid: str
    documents: list[str]
    phone_numbers: NotRequired[list[PhoneNumber1 | PhoneNumber1Dict]]
    losing_carrier_information: LosingCarrierInformation | LosingCarrierInformationDict
    notification_emails: NotRequired[list[str | None]]
    target_port_in_date: NotRequired[Date | None]
    target_port_in_time_range_start: NotRequired[str | None]
    target_port_in_time_range_end: NotRequired[str | None]
    bundle_sid: NotRequired[str | None]
    portability_advance_carrier: NotRequired[str | None]
    auto_cancel_approval_numbers: NotRequired[str | None]
