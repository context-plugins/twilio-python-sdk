from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountValidationRequest(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for the Caller ID."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Caller ID is associated
    with."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number to verify in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format, which consists
    of a + followed by the country code and subscriber number."""

    validation_code: OptionalNullable[str] = UNSET
    """The 6 digit validation code that someone must enter to validate the Caller ID when ``phone_number`` is called."""


class ApiV2010AccountValidationRequestDict(TypedDict):
    account_sid: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    validation_code: NotRequired[str | None]
