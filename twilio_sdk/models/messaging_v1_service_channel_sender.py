from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1ServiceChannelSender(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the ChannelSender
    resource."""

    messaging_service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/messaging/services>`__ the resource is associated with."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the ChannelSender resource."""

    sender: OptionalNullable[str] = UNSET
    """The unique string that identifies the sender e.g whatsapp:+123456XXXX."""

    sender_type: OptionalNullable[str] = UNSET
    """A string value that identifies the sender type e.g WhatsApp, Messenger."""

    country_code: OptionalNullable[str] = UNSET
    """The 2-character `ISO Country Code <https://www.iso.org/iso-3166-country-codes.html>`__ of the number."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the ChannelSender resource."""


class MessagingV1ServiceChannelSenderDict(TypedDict):
    account_sid: NotRequired[str | None]
    messaging_service_sid: NotRequired[str | None]
    sid: NotRequired[str | None]
    sender: NotRequired[str | None]
    sender_type: NotRequired[str | None]
    country_code: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
