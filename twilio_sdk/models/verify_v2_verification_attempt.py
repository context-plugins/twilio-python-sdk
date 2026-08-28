from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.verification_attempt_enum_channels import VerificationAttemptEnumChannelsOrStr
from .enums.verification_attempt_enum_conversion_status import VerificationAttemptEnumConversionStatusOrStr


class VerifyV2VerificationAttempt(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The SID that uniquely identifies the verification attempt resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Verification
    resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ used to generate the attempt."""

    verification_sid: OptionalNullable[str] = UNSET
    """The SID of the `Verification <https://www.twilio.com/docs/verify/api/verification>`__ that generated the
    attempt."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this Attempt was created, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this Attempt was updated, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    conversion_status: Optional[VerificationAttemptEnumConversionStatusOrStr] = UNSET
    """A string specifying the conversion status of the verification. A conversion happens when the user is able to
    provide the correct code. Possible values are ``CONVERTED`` and ``UNCONVERTED``."""

    channel: Optional[VerificationAttemptEnumChannelsOrStr] = UNSET
    """A string specifying the communication channel used for the verification attempt."""

    price: OptionalNullable[Any] = UNSET
    """An object containing the charge for this verification attempt related to the channel costs and the currency used.
    The costs related to the succeeded verifications are not included. May not be immediately available. More
    information on pricing is available `here <https://www.twilio.com/en-us/verify/pricing>`__."""

    channel_data: OptionalNullable[Any] = UNSET
    """An object containing the channel specific information for an attempt."""

    url: OptionalNullable[AnyUrl] = UNSET


class VerifyV2VerificationAttemptDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    verification_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    conversion_status: NotRequired[VerificationAttemptEnumConversionStatusOrStr]
    channel: NotRequired[VerificationAttemptEnumChannelsOrStr]
    price: NotRequired[Any | None]
    channel_data: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
