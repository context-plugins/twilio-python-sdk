from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class VerifyV2ServiceMessagingConfiguration(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Service resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/verify/api/service>`__ that the resource is associated
    with."""

    country: OptionalNullable[str] = UNSET
    """The `ISO-3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code of the country this
    configuration will be applied to. If this is a global configuration, Country will take the value ``all``."""

    messaging_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Messaging Service <https://www.twilio.com/docs/messaging/api/service-resource>`__ to be used to
    send SMS to the country of this configuration."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    url: OptionalNullable[str] = UNSET
    """The URL of this resource."""


class VerifyV2ServiceMessagingConfigurationDict(TypedDict):
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    country: NotRequired[str | None]
    messaging_service_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
