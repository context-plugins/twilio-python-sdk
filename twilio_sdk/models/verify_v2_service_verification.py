from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.verification_enum_channel import VerificationEnumChannelOrStr


class VerifyV2ServiceVerification(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Verification resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ the resource is associated with."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Verification
    resource."""

    to: OptionalNullable[str] = UNSET
    """The phone number or `email <https://www.twilio.com/docs/verify/email>`__ being verified. Phone numbers must be in
    `E.164 format <https://www.twilio.com/docs/glossary/what-e164>`__."""

    channel: Optional[VerificationEnumChannelOrStr] = UNSET
    """The verification method used. One of: https://www.twilio.com/docs/verify/email, ``sms``, ``whatsapp``, ``call``,
    ``sna``, or ``rcs``."""

    status: OptionalNullable[str] = UNSET
    """The status of the verification. Can be: ``pending``, ``approved``, ``canceled``, ``max_attempts_reached``,
    ``deleted``, ``failed`` or ``expired``."""

    valid: OptionalNullable[bool] = UNSET
    """Use "status" instead. Legacy property indicating whether the verification was successful."""

    lookup: OptionalNullable[Any] = UNSET
    """Information about the phone number being verified."""

    amount: OptionalNullable[str] = UNSET
    """The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled."""

    payee: OptionalNullable[str] = UNSET
    """The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled."""

    send_code_attempts: Optional[list[Any | None]] = UNSET
    """An array of verification attempt objects containing the channel attempted and the channel-specific transaction
    SID."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    sna: OptionalNullable[Any] = UNSET
    """The set of fields used for a silent network auth (``sna``) verification. Contains a single field with the URL to
    be invoked to verify the phone number."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Verification resource."""


class VerifyV2ServiceVerificationDict(TypedDict):
    sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    to: NotRequired[str | None]
    channel: NotRequired[VerificationEnumChannelOrStr]
    status: NotRequired[str | None]
    valid: NotRequired[bool | None]
    lookup: NotRequired[Any | None]
    amount: NotRequired[str | None]
    payee: NotRequired[str | None]
    send_code_attempts: NotRequired[list[Any | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    sna: NotRequired[Any | None]
    url: NotRequired[str | None]
