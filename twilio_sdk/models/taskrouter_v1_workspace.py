from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.workspace_enum_queue_order import WorkspaceEnumQueueOrderOrStr


class TaskrouterV1Workspace(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Workspace resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    default_activity_name: OptionalNullable[str] = UNSET
    """The name of the default activity."""

    default_activity_sid: OptionalNullable[str] = UNSET
    """The SID of the Activity that will be used when new Workers are created in the Workspace."""

    event_callback_url: OptionalNullable[AnyUrl] = UNSET
    """The URL we call when an event occurs. If provided, the Workspace will publish events to this URL, for example, to
    collect data for reporting. See `Workspace Events <https://www.twilio.com/docs/taskrouter/api/event>`__ for more
    information. This parameter supports Twilio's `Webhooks (HTTP callbacks) Connection Overrides
    <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__."""

    events_filter: OptionalNullable[str] = UNSET
    """The list of Workspace events for which to call ``event_callback_url``. For example, if
    ``EventsFilter=task.created, task.canceled, worker.activity.update``, then TaskRouter will call event_callback_url
    only when a task is created, canceled, or a Worker activity is updated."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the Workspace resource. For example ``Customer Support`` or ``2014
    Election Campaign``."""

    multi_task_enabled: OptionalNullable[bool] = UNSET
    """Whether multi-tasking is enabled. The default is ``true``, which enables multi-tasking. Multi-tasking allows
    Workers to handle multiple Tasks simultaneously. When enabled (``true``), each Worker can receive parallel
    reservations up to the per-channel maximums defined in the Workers section. In single-tasking each Worker would only
    receive a new reservation when the previous task is completed. Learn more at `Multitasking
    <https://www.twilio.com/docs/taskrouter/multitasking>`__."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Workspace resource."""

    timeout_activity_name: OptionalNullable[str] = UNSET
    """The name of the timeout activity."""

    timeout_activity_sid: OptionalNullable[str] = UNSET
    """The SID of the Activity that will be assigned to a Worker when a Task reservation times out without a
    response."""

    prioritize_queue_order: Optional[WorkspaceEnumQueueOrderOrStr] = UNSET
    """The type of TaskQueue to prioritize when Workers are receiving Tasks from both types of TaskQueues. Can be:
    ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see `Queue Ordering
    <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Workspace resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class TaskrouterV1WorkspaceDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    default_activity_name: NotRequired[str | None]
    default_activity_sid: NotRequired[str | None]
    event_callback_url: NotRequired[AnyUrl | None]
    events_filter: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    multi_task_enabled: NotRequired[bool | None]
    sid: NotRequired[str | None]
    timeout_activity_name: NotRequired[str | None]
    timeout_activity_sid: NotRequired[str | None]
    prioritize_queue_order: NotRequired[WorkspaceEnumQueueOrderOrStr]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
