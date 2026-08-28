from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1ServiceDestinationAlphaSender(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the AlphaSender resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the AlphaSender
    resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ the resource is associated
    with."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    alpha_sender: OptionalNullable[str] = UNSET
    """The Alphanumeric Sender ID string."""

    capabilities: Optional[list[str | None]] = UNSET
    """An array of values that describe whether the number can receive calls or messages. Can be: ``SMS``."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the AlphaSender resource."""

    iso_country_code: OptionalNullable[str] = UNSET
    """The Two Character ISO Country Code the Alphanumeric Sender ID will be used for. For Default Alpha Senders that
    work across countries, this value will be an empty string"""


class MessagingV1ServiceDestinationAlphaSenderDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    alpha_sender: NotRequired[str | None]
    capabilities: NotRequired[list[str | None]]
    url: NotRequired[AnyUrl | None]
    iso_country_code: NotRequired[str | None]
