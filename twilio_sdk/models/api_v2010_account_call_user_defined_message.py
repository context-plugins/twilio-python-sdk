from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountCallUserDefinedMessage(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created User Defined Message."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the User Defined Message is
    associated with."""

    sid: OptionalNullable[str] = UNSET
    """The SID that uniquely identifies this User Defined Message."""

    date_created: OptionalNullable[str] = UNSET
    """The date that this User Defined Message was created, given in RFC 2822 format."""


class ApiV2010AccountCallUserDefinedMessageDict(TypedDict):
    account_sid: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
