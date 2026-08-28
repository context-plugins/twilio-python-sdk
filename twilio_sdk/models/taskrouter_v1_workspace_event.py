from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceEvent(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Event resource."""

    actor_sid: OptionalNullable[str] = UNSET
    """The SID of the resource that triggered the event."""

    actor_type: OptionalNullable[str] = UNSET
    """The type of resource that triggered the event."""

    actor_url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource that triggered the event."""

    description: OptionalNullable[str] = UNSET
    """A description of the event."""

    event_data: OptionalNullable[Any] = UNSET
    """Data about the event. For more information, see `Event types
    <https://www.twilio.com/docs/taskrouter/api/event#event-types>`__."""

    event_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The time the event was sent, specified in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    event_date_ms: OptionalNullable[int] = UNSET
    """The time the event was sent in milliseconds."""

    event_type: OptionalNullable[str] = UNSET
    """The identifier for the event."""

    resource_sid: OptionalNullable[str] = UNSET
    """The SID of the object the event is most relevant to, such as a TaskSid, ReservationSid, or a WorkerSid."""

    resource_type: OptionalNullable[str] = UNSET
    """The type of object the event is most relevant to, such as a Task, Reservation, or a Worker)."""

    resource_url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the resource the event is most relevant to."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Event resource."""

    source: OptionalNullable[str] = UNSET
    """Where the Event originated."""

    source_ip_address: OptionalNullable[str] = UNSET
    """The IP from which the Event originated."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Event resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Event."""


class TaskrouterV1WorkspaceEventDict(TypedDict):
    account_sid: NotRequired[str | None]
    actor_sid: NotRequired[str | None]
    actor_type: NotRequired[str | None]
    actor_url: NotRequired[AnyUrl | None]
    description: NotRequired[str | None]
    event_data: NotRequired[Any | None]
    event_date: NotRequired[RFC3339DateTime | None]
    event_date_ms: NotRequired[int | None]
    event_type: NotRequired[str | None]
    resource_sid: NotRequired[str | None]
    resource_type: NotRequired[str | None]
    resource_url: NotRequired[AnyUrl | None]
    sid: NotRequired[str | None]
    source: NotRequired[str | None]
    source_ip_address: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    workspace_sid: NotRequired[str | None]
