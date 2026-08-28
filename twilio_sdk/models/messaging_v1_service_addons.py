from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1ServiceAddons(SdkBaseModel):
    sid: Optional[str] = UNSET
    """The unique string that we created to identify the add on resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the add on resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/chat/rest/service-resource>`__ the resource is associated
    with."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    add_on_type_sid: OptionalNullable[str] = UNSET
    """The SID that identifies the add on type."""

    add_on_config: OptionalNullable[str] = UNSET
    """The config of the add on in JSON string format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the add on resource."""


class MessagingV1ServiceAddonsDict(TypedDict):
    sid: NotRequired[str]
    account_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    add_on_type_sid: NotRequired[str | None]
    add_on_config: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
