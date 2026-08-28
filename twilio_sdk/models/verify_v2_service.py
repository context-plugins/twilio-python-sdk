from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class VerifyV2Service(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Service resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Service resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The name that appears in the body of your verification messages. It can be up to 30 characters long and can
    include letters, numbers, spaces, dashes, underscores. Phone numbers, special characters or links are NOT allowed.
    It cannot contain more than 4 (consecutive or non-consecutive) digits. **This value should not contain PII.**"""

    code_length: Optional[int] = UNSET
    """The length of the verification code to generate."""

    lookup_enabled: OptionalNullable[bool] = UNSET
    """Whether to perform a lookup with each verification started and return info about the phone number."""

    psd2_enabled: OptionalNullable[bool] = UNSET
    """Whether to pass PSD2 transaction parameters when starting a verification."""

    skip_sms_to_landlines: OptionalNullable[bool] = UNSET
    """Whether to skip sending SMS verifications to landlines. Requires ``lookup_enabled``."""

    dtmf_input_required: OptionalNullable[bool] = UNSET
    """Whether to ask the user to press a number before delivering the verify code in a phone call."""

    tts_name: OptionalNullable[str] = UNSET
    """The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages."""

    do_not_share_warning_enabled: OptionalNullable[bool] = UNSET
    """Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to
    SMS. Example SMS body: ``Your AppName verification code is: 1234. Don’t share this code with anyone; our employees
    will never ask for the code``"""

    custom_code_enabled: OptionalNullable[bool] = UNSET
    """Whether to allow sending verifications with a custom code instead of a randomly generated one."""

    push: OptionalNullable[Any] = UNSET
    """Configurations for the Push factors (channel) created under this Service."""

    totp: OptionalNullable[Any] = UNSET
    """Configurations for the TOTP factors (channel) created under this Service."""

    default_template_sid: OptionalNullable[str] = UNSET
    whatsapp: OptionalNullable[Any] = UNSET
    passkeys: OptionalNullable[Any] = UNSET
    verify_event_subscription_enabled: OptionalNullable[bool] = UNSET
    """Whether to allow verifications from the service to reach the stream-events sinks if configured"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class VerifyV2ServiceDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    code_length: NotRequired[int]
    lookup_enabled: NotRequired[bool | None]
    psd2_enabled: NotRequired[bool | None]
    skip_sms_to_landlines: NotRequired[bool | None]
    dtmf_input_required: NotRequired[bool | None]
    tts_name: NotRequired[str | None]
    do_not_share_warning_enabled: NotRequired[bool | None]
    custom_code_enabled: NotRequired[bool | None]
    push: NotRequired[Any | None]
    totp: NotRequired[Any | None]
    default_template_sid: NotRequired[str | None]
    whatsapp: NotRequired[Any | None]
    passkeys: NotRequired[Any | None]
    verify_event_subscription_enabled: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
