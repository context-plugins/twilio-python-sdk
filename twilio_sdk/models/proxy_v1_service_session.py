from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.session_enum_mode import SessionEnumModeOrStr
from .enums.session_enum_status import SessionEnumStatusOrStr


class ProxyV1ServiceSession(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Session resource."""

    service_sid: OptionalNullable[str] = UNSET
    """The SID of the `Service <https://www.twilio.com/docs/proxy/api/service>`__ the session is associated with."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Session resource."""

    date_started: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session started."""

    date_ended: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session ended."""

    date_last_interaction: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session last had an interaction."""

    date_expiry: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date when the Session should expire. If this is value
    is present, it overrides the ``ttl`` value."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer
    in length and be unique. Supports UTF-8 characters. **This value should not have PII.**"""

    status: Optional[SessionEnumStatusOrStr] = UNSET
    """The status of the Session. Can be: ``open``, ``in-progress``, ``closed``, ``failed``, or ``unknown``."""

    closed_reason: OptionalNullable[str] = UNSET
    """The reason the Session ended."""

    ttl: Optional[int] = UNSET
    """The time, in seconds, when the session will expire. The time is measured from the last Session create or the
    Session's last Interaction."""

    mode: Optional[SessionEnumModeOrStr] = UNSET
    """The Mode of the Session. Can be: ``message-only``, ``voice-only``, or ``voice-and-message``."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date and time in GMT when the resource was last
    updated."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Session resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of resources related to the Session."""


class ProxyV1ServiceSessionDict(TypedDict):
    sid: NotRequired[str | None]
    service_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    date_started: NotRequired[RFC3339DateTime | None]
    date_ended: NotRequired[RFC3339DateTime | None]
    date_last_interaction: NotRequired[RFC3339DateTime | None]
    date_expiry: NotRequired[RFC3339DateTime | None]
    unique_name: NotRequired[str | None]
    status: NotRequired[SessionEnumStatusOrStr]
    closed_reason: NotRequired[str | None]
    ttl: NotRequired[int]
    mode: NotRequired[SessionEnumModeOrStr]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
