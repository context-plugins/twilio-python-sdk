from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.verification_check_enum_channel import VerificationCheckEnumChannelOrStr


class VerifyV2ServiceVerificationCheck(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the VerificationCheck resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is associated with."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the VerificationCheck
    resource."""

    to: OptionalNullable[str] = UNSET
    """The phone number or `email <https://www.twilio.com/docs/verify/email>`__ being verified. Phone numbers must be in
    `E.164 format <https://www.twilio.com/docs/glossary/what-e164>`__."""

    channel: Optional[VerificationCheckEnumChannelOrStr] = UNSET
    """The verification method to use. One of: https://www.twilio.com/docs/verify/email, ``sms``, ``whatsapp``,
    ``call``, or ``sna``."""

    status: OptionalNullable[str] = UNSET
    """The status of the verification. Can be: ``pending``, ``approved``, ``canceled``, ``max_attempts_reached``,
    ``deleted``, ``failed`` or ``expired``."""

    valid: OptionalNullable[bool] = UNSET
    """Use "status" instead. Legacy property indicating whether the verification was successful."""

    amount: OptionalNullable[str] = UNSET
    """The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled."""

    payee: OptionalNullable[str] = UNSET
    """The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the Verification Check
    resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the Verification Check
    resource was last updated."""

    sna_attempts_error_codes: Optional[list[Any | None]] = UNSET
    """List of error codes as a result of attempting a verification using the ``sna`` channel. The error codes are
    chronologically ordered, from the first attempt to the latest attempt. This will be an empty list if no errors
    occured or ``null`` if the last channel used wasn't ``sna``."""


class VerifyV2ServiceVerificationCheckDict(TypedDict):
    sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    to: NotRequired[str | None]
    channel: NotRequired[VerificationCheckEnumChannelOrStr]
    status: NotRequired[str | None]
    valid: NotRequired[bool | None]
    amount: NotRequired[str | None]
    payee: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    sna_attempts_error_codes: NotRequired[list[Any | None]]
