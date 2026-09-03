from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.sms_fallback_method6 import SmsFallbackMethod6OrStr
from .enums.sms_method6 import SmsMethod6OrStr


class ApiV2010AccountShortCode(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this ShortCode resource."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to start a new TwiML session when an SMS message is sent to this short code."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that this resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that this resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """A string that you assigned to describe this resource. By default, the ``FriendlyName`` is the short code."""

    short_code: OptionalNullable[str] = UNSET
    """The short code. e.g., 894546."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify this ShortCode resource."""

    sms_fallback_method: OptionalNullable[SmsFallbackMethod6OrStr] = UNSET
    """The HTTP method we use to call the ``sms_fallback_url``. Can be: ``GET`` or ``POST``."""

    sms_fallback_url: OptionalNullable[str] = UNSET
    """The URL that we call if an error occurs while retrieving or executing the TwiML from ``sms_url``."""

    sms_method: OptionalNullable[SmsMethod6OrStr] = UNSET
    """The HTTP method we use to call the ``sms_url``. Can be: ``GET`` or ``POST``."""

    sms_url: OptionalNullable[str] = UNSET
    """The URL we call when receiving an incoming SMS message to this short code."""

    uri: OptionalNullable[str] = UNSET
    """The URI of this resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountShortCodeDict(TypedDict):
    account_sid: NotRequired[str | None]
    api_version: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    short_code: NotRequired[str | None]
    sid: NotRequired[str | None]
    sms_fallback_method: NotRequired[SmsFallbackMethod6OrStr | None]
    sms_fallback_url: NotRequired[str | None]
    sms_method: NotRequired[SmsMethod6OrStr | None]
    sms_url: NotRequired[str | None]
    uri: NotRequired[str | None]
