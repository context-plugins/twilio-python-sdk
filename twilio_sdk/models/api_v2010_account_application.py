from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.sms_fallback_method import SmsFallbackMethodOrStr
from .enums.sms_method import SmsMethodOrStr
from .enums.status_callback_method import StatusCallbackMethodOrStr
from .enums.voice_fallback_method import VoiceFallbackMethodOrStr
from .enums.voice_method import VoiceMethodOrStr


class ApiV2010AccountApplication(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Application
    resource."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to start a new TwiML session."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    message_status_callback: OptionalNullable[AnyUrl] = UNSET
    """The URL we call using a POST method to send message status information to your application."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the Application resource."""

    sms_fallback_method: OptionalNullable[SmsFallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``sms_fallback_url``. Can be: ``GET`` or ``POST``."""

    sms_fallback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL that we call when an error occurs while retrieving or executing the TwiML from ``sms_url``."""

    sms_method: OptionalNullable[SmsMethodOrStr] = UNSET
    """The HTTP method we use to call ``sms_url``. Can be: ``GET`` or ``POST``."""

    sms_status_callback: OptionalNullable[AnyUrl] = UNSET
    """The URL we call using a POST method to send status information to your application about SMS messages that refer
    to the application."""

    sms_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call when the phone number receives an incoming SMS message."""

    status_callback: OptionalNullable[AnyUrl] = UNSET
    """The URL we call using the ``status_callback_method`` to send status information to your application."""

    status_callback_method: OptionalNullable[StatusCallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``status_callback``. Can be: ``GET`` or ``POST``."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    voice_caller_id_lookup: OptionalNullable[bool] = UNSET
    """Whether we look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be:
    ``true`` or ``false``."""

    voice_fallback_method: OptionalNullable[VoiceFallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``voice_fallback_url``. Can be: ``GET`` or ``POST``."""

    voice_fallback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL that we call when an error occurs retrieving or executing the TwiML requested by ``url``."""

    voice_method: OptionalNullable[VoiceMethodOrStr] = UNSET
    """The HTTP method we use to call ``voice_url``. Can be: ``GET`` or ``POST``."""

    voice_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call when the phone number assigned to this application receives a call."""

    public_application_connect_enabled: OptionalNullable[bool] = UNSET
    """Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: ``true`` or ``false``."""


class ApiV2010AccountApplicationDict(TypedDict):
    account_sid: NotRequired[str | None]
    api_version: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    message_status_callback: NotRequired[AnyUrl | None]
    sid: NotRequired[str | None]
    sms_fallback_method: NotRequired[SmsFallbackMethodOrStr | None]
    sms_fallback_url: NotRequired[AnyUrl | None]
    sms_method: NotRequired[SmsMethodOrStr | None]
    sms_status_callback: NotRequired[AnyUrl | None]
    sms_url: NotRequired[AnyUrl | None]
    status_callback: NotRequired[AnyUrl | None]
    status_callback_method: NotRequired[StatusCallbackMethodOrStr | None]
    uri: NotRequired[str | None]
    voice_caller_id_lookup: NotRequired[bool | None]
    voice_fallback_method: NotRequired[VoiceFallbackMethodOrStr | None]
    voice_fallback_url: NotRequired[AnyUrl | None]
    voice_method: NotRequired[VoiceMethodOrStr | None]
    voice_url: NotRequired[AnyUrl | None]
    public_application_connect_enabled: NotRequired[bool | None]
