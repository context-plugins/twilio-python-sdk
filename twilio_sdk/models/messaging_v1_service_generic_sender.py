from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1ServiceGenericSender(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The SID to identify the number or channel sender resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the number or channel
    sender resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ the resource is associated
    with."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    sender: OptionalNullable[str] = UNSET
    """The unique string that identifies the number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format
    or the channel sender e.g whatsapp:+123456XXXX."""

    sender_type: OptionalNullable[str] = UNSET
    """A string value that identifies the number or channel sender type e.g AlphaSenderId, LongCode, ShortCode,
    Whatsapp, RCS."""

    country_code: OptionalNullable[str] = UNSET
    """The 2-character `ISO Country Code <https://www.iso.org/iso-3166-country-codes.html>`__ of the number or channel
    sender."""


class MessagingV1ServiceGenericSenderDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    sender: NotRequired[str | None]
    sender_type: NotRequired[str | None]
    country_code: NotRequired[str | None]
