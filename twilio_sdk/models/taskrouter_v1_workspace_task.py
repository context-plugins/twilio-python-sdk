from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.task_enum_status import TaskEnumStatusOrStr


class TaskrouterV1WorkspaceTask(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Task resource."""

    age: Optional[int] = UNSET
    """The number of seconds since the Task was created."""

    assignment_status: Optional[TaskEnumStatusOrStr] = UNSET
    """The current status of the Task's assignment. Can be: ``pending``, ``reserved``, ``assigned``, ``canceled``,
    ``wrapping``, or ``completed``."""

    attributes: OptionalNullable[str] = UNSET
    """The JSON string with custom attributes of the work. **Note** If this property has been assigned a value, it will
    only be displayed in FETCH action that returns a single resource. Otherwise, it will be null."""

    addons: OptionalNullable[str] = UNSET
    """An object that contains the `Add-on <https://www.twilio.com/docs/add-ons>`__ data for all installed Add-ons."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    task_queue_entered_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the Task entered the TaskQueue, specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    priority: Optional[int] = UNSET
    """The current priority score of the Task as assigned to a Worker by the workflow. Tasks with higher priority values
    will be assigned before Tasks with lower values."""

    reason: OptionalNullable[str] = UNSET
    """The reason the Task was canceled or completed, if applicable."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Task resource."""

    task_queue_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskQueue."""

    task_queue_friendly_name: OptionalNullable[str] = UNSET
    """The friendly name of the TaskQueue."""

    task_channel_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskChannel."""

    task_channel_unique_name: OptionalNullable[str] = UNSET
    """The unique name of the TaskChannel."""

    timeout: Optional[int] = UNSET
    """The amount of time in seconds that the Task can live before being assigned."""

    workflow_sid: OptionalNullable[str] = UNSET
    """The SID of the Workflow that is controlling the Task."""

    workflow_friendly_name: OptionalNullable[str] = UNSET
    """The friendly name of the Workflow that is controlling the Task."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Task."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Task resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""

    virtual_start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT indicating the ordering for routing of the Task specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    ignore_capacity: OptionalNullable[bool] = UNSET
    """A boolean that indicates if the Task should respect a Worker's capacity and availability during assignment. This
    field can only be used when the ``RoutingTarget`` field is set to a Worker SID. By setting ``IgnoreCapacity`` to a
    value of ``true``, ``1``, or ``yes``, the Task will be routed to the Worker without respecting their capacity and
    availability. Any other value will enforce the Worker's capacity and availability. The default value of
    ``IgnoreCapacity`` is ``true`` when the ``RoutingTarget`` is set to a Worker SID."""

    routing_target: OptionalNullable[str] = UNSET
    """A SID of a Worker, Queue, or Workflow to route a Task to"""


class TaskrouterV1WorkspaceTaskDict(TypedDict):
    account_sid: NotRequired[str | None]
    age: NotRequired[int]
    assignment_status: NotRequired[TaskEnumStatusOrStr]
    attributes: NotRequired[str | None]
    addons: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    task_queue_entered_date: NotRequired[RFC3339DateTime | None]
    priority: NotRequired[int]
    reason: NotRequired[str | None]
    sid: NotRequired[str | None]
    task_queue_sid: NotRequired[str | None]
    task_queue_friendly_name: NotRequired[str | None]
    task_channel_sid: NotRequired[str | None]
    task_channel_unique_name: NotRequired[str | None]
    timeout: NotRequired[int]
    workflow_sid: NotRequired[str | None]
    workflow_friendly_name: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
    virtual_start_time: NotRequired[RFC3339DateTime | None]
    ignore_capacity: NotRequired[bool | None]
    routing_target: NotRequired[str | None]
