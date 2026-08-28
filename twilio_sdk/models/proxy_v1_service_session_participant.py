from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ProxyV1ServiceSessionParticipant(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Participant resource."""

    session_sid: OptionalNullable[str] = UNSET
    """The SID of the parent `Session <https://www.twilio.com/docs/proxy/api/session>`__ resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the resource's parent `Service <https://www.twilio.com/docs/proxy/api/service>`__ resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Participant
    resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the participant. This value must be 255 characters or fewer. Supports
    UTF-8 characters. **This value should not have PII.**"""

    identifier: OptionalNullable[str] = UNSET
    """The phone number or channel identifier of the Participant. This value must be 191 characters or fewer. Supports
    UTF-8 characters."""

    proxy_identifier: OptionalNullable[str] = UNSET
    """The phone number or short code (masked number) of the participant's partner. The participant will call or message
    the partner participant at this number."""

    proxy_identifier_sid: OptionalNullable[str] = UNSET
    """The SID of the Proxy Identifier assigned to the Participant."""

    date_deleted: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Participant was removed from the
    session."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was last
    updated."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Participant resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs to resources related the participant."""


class ProxyV1ServiceSessionParticipantDict(TypedDict):
    sid: NotRequired[str | None]
    session_sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    identifier: NotRequired[str | None]
    proxy_identifier: NotRequired[str | None]
    proxy_identifier_sid: NotRequired[str | None]
    date_deleted: NotRequired[RFC3339DateTime | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
