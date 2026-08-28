from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.voice_fallback_method import VoiceFallbackMethodOrStr
from .enums.voice_method import VoiceMethodOrStr
from .enums.voice_status_callback_method import VoiceStatusCallbackMethodOrStr


class ApiV2010AccountSipSipDomain(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the SipDomain resource."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to process the call."""

    auth_type: OptionalNullable[str] = UNSET
    """The types of authentication you have mapped to your domain. Can be: ``IP_ACL`` and ``CREDENTIAL_LIST``. If you
    have both defined for your domain, both will be returned in a comma delimited string. If ``auth_type`` is not
    defined, the domain will not be able to receive any traffic."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    domain_name: OptionalNullable[str] = UNSET
    """The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters,
    digits, and "-" and must end with ``sip.twilio.com``."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the SipDomain resource."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    voice_fallback_method: OptionalNullable[VoiceFallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``voice_fallback_url``. Can be: ``GET`` or ``POST``."""

    voice_fallback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL that we call when an error occurs while retrieving or executing the TwiML requested from
    ``voice_url``."""

    voice_method: OptionalNullable[VoiceMethodOrStr] = UNSET
    """The HTTP method we use to call ``voice_url``. Can be: ``GET`` or ``POST``."""

    voice_status_callback_method: OptionalNullable[VoiceStatusCallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``voice_status_callback_url``. Either ``GET`` or ``POST``."""

    voice_status_callback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL that we call to pass status parameters (such as call ended) to your application."""

    voice_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call using the ``voice_method`` when the domain receives a call."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of mapping resources associated with the SIP Domain resource identified by their relative URIs."""

    sip_registration: OptionalNullable[bool] = UNSET
    """Whether to allow SIP Endpoints to register with the domain to receive calls."""

    emergency_calling_enabled: OptionalNullable[bool] = UNSET
    """Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone
    numbers with validated addresses."""

    secure: OptionalNullable[bool] = UNSET
    """Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all
    incoming calls to this sip domain."""

    byoc_trunk_sid: OptionalNullable[str] = UNSET
    """The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with."""

    emergency_caller_sid: OptionalNullable[str] = UNSET
    """Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the
    callback for the emergency call."""


class ApiV2010AccountSipSipDomainDict(TypedDict):
    account_sid: NotRequired[str | None]
    api_version: NotRequired[str | None]
    auth_type: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    domain_name: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    sid: NotRequired[str | None]
    uri: NotRequired[str | None]
    voice_fallback_method: NotRequired[VoiceFallbackMethodOrStr | None]
    voice_fallback_url: NotRequired[AnyUrl | None]
    voice_method: NotRequired[VoiceMethodOrStr | None]
    voice_status_callback_method: NotRequired[VoiceStatusCallbackMethodOrStr | None]
    voice_status_callback_url: NotRequired[AnyUrl | None]
    voice_url: NotRequired[AnyUrl | None]
    subresource_uris: NotRequired[Any | None]
    sip_registration: NotRequired[bool | None]
    emergency_calling_enabled: NotRequired[bool | None]
    secure: NotRequired[bool | None]
    byoc_trunk_sid: NotRequired[str | None]
    emergency_caller_sid: NotRequired[str | None]
