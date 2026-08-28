from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.dependent_phone_number_enum_address_requirement import DependentPhoneNumberEnumAddressRequirementOrStr
from .enums.dependent_phone_number_enum_emergency_status import DependentPhoneNumberEnumEmergencyStatusOrStr
from .enums.sms_fallback_method import SmsFallbackMethodOrStr
from .enums.sms_method import SmsMethodOrStr
from .enums.status_callback_method import StatusCallbackMethodOrStr
from .enums.voice_fallback_method import VoiceFallbackMethodOrStr
from .enums.voice_method import VoiceMethodOrStr


class ApiV2010AccountAddressDependentPhoneNumber(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the DependentPhoneNumber resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the DependentPhoneNumber
    resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format, which consists of a +
    followed by the country code and subscriber number."""

    voice_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call when the phone number receives a call. The ``voice_url`` will not be used if a
    ``voice_application_sid`` or a ``trunk_sid`` is set."""

    voice_method: OptionalNullable[VoiceMethodOrStr] = UNSET
    """The HTTP method we use to call ``voice_url``. Can be: ``GET`` or ``POST``."""

    voice_fallback_method: OptionalNullable[VoiceFallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``voice_fallback_url``. Can be: ``GET`` or ``POST``."""

    voice_fallback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL that we call when an error occurs retrieving or executing the TwiML requested by ``url``."""

    voice_caller_id_lookup: OptionalNullable[bool] = UNSET
    """Whether we look up the caller's caller-ID name from the CNAM database. Can be: ``true`` or ``false``. Caller ID
    lookups can cost $0.01 each."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    sms_fallback_method: OptionalNullable[SmsFallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``sms_fallback_url``. Can be: ``GET`` or ``POST``."""

    sms_fallback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL that we call when an error occurs while retrieving or executing the TwiML from ``sms_url``."""

    sms_method: OptionalNullable[SmsMethodOrStr] = UNSET
    """The HTTP method we use to call ``sms_url``. Can be: ``GET`` or ``POST``."""

    sms_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call when the phone number receives an incoming SMS message."""

    address_requirements: Optional[DependentPhoneNumberEnumAddressRequirementOrStr] = UNSET
    """Whether the phone number requires an `Address <https://www.twilio.com/docs/usage/api/address>`__ registered with
    Twilio. Can be: ``none``, ``any``, ``local``, or ``foreign``."""

    capabilities: OptionalNullable[Any] = UNSET
    """The set of Boolean properties that indicates whether a phone number can receive calls or messages. Capabilities
    are ``Voice``, ``SMS``, and ``MMS`` and each capability can be: ``true`` or ``false``."""

    status_callback: OptionalNullable[AnyUrl] = UNSET
    """The URL we call using the ``status_callback_method`` to send status information to your application."""

    status_callback_method: OptionalNullable[StatusCallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``status_callback``. Can be: ``GET`` or ``POST``."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to start a new TwiML session."""

    sms_application_sid: OptionalNullable[str] = UNSET
    """The SID of the application that handles SMS messages sent to the phone number. If an ``sms_application_sid`` is
    present, we ignore all ``sms_*_url`` values and use those of the application."""

    voice_application_sid: OptionalNullable[str] = UNSET
    """The SID of the application that handles calls to the phone number. If a ``voice_application_sid`` is present, we
    ignore all of the voice urls and use those set on the application. Setting a ``voice_application_sid`` will
    automatically delete your ``trunk_sid`` and vice versa."""

    trunk_sid: OptionalNullable[str] = UNSET
    """The SID of the Trunk that handles calls to the phone number. If a ``trunk_sid`` is present, we ignore all of the
    voice urls and voice applications and use those set on the Trunk. Setting a ``trunk_sid`` will automatically delete
    your ``voice_application_sid`` and vice versa."""

    emergency_status: Optional[DependentPhoneNumberEnumEmergencyStatusOrStr] = UNSET
    """Whether the phone number is enabled for emergency calling."""

    emergency_address_sid: OptionalNullable[str] = UNSET
    """The SID of the emergency address configuration that we use for emergency calling from the phone number."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountAddressDependentPhoneNumberDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    voice_url: NotRequired[AnyUrl | None]
    voice_method: NotRequired[VoiceMethodOrStr | None]
    voice_fallback_method: NotRequired[VoiceFallbackMethodOrStr | None]
    voice_fallback_url: NotRequired[AnyUrl | None]
    voice_caller_id_lookup: NotRequired[bool | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    sms_fallback_method: NotRequired[SmsFallbackMethodOrStr | None]
    sms_fallback_url: NotRequired[AnyUrl | None]
    sms_method: NotRequired[SmsMethodOrStr | None]
    sms_url: NotRequired[AnyUrl | None]
    address_requirements: NotRequired[DependentPhoneNumberEnumAddressRequirementOrStr]
    capabilities: NotRequired[Any | None]
    status_callback: NotRequired[AnyUrl | None]
    status_callback_method: NotRequired[StatusCallbackMethodOrStr | None]
    api_version: NotRequired[str | None]
    sms_application_sid: NotRequired[str | None]
    voice_application_sid: NotRequired[str | None]
    trunk_sid: NotRequired[str | None]
    emergency_status: NotRequired[DependentPhoneNumberEnumEmergencyStatusOrStr]
    emergency_address_sid: NotRequired[str | None]
    uri: NotRequired[str | None]
