from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.task_queue_enum_task_order import TaskQueueEnumTaskOrderOrStr


class TaskrouterV1WorkspaceTaskQueue(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the TaskQueue resource."""

    assignment_activity_sid: OptionalNullable[str] = UNSET
    """The SID of the Activity to assign Workers when a task is assigned for them."""

    assignment_activity_name: OptionalNullable[str] = UNSET
    """The name of the Activity to assign Workers when a task is assigned for them."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    max_reserved_workers: Optional[int] = UNSET
    """The maximum number of Workers to reserve for the assignment of a task in the queue. Can be an integer between 1
    and 50, inclusive and defaults to 1."""

    reservation_activity_sid: OptionalNullable[str] = UNSET
    """The SID of the Activity to assign Workers once a task is reserved for them."""

    reservation_activity_name: OptionalNullable[str] = UNSET
    """The name of the Activity to assign Workers once a task is reserved for them."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the TaskQueue resource."""

    target_workers: OptionalNullable[str] = UNSET
    """A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example
    ``'"language" == "spanish"'`` If no TargetWorkers parameter is provided, Tasks will wait in the TaskQueue until they
    are either deleted or moved to another TaskQueue. Additional examples on how to describing Worker selection criteria
    below. Defaults to 1==1."""

    task_order: Optional[TaskQueueEnumTaskOrderOrStr] = UNSET
    """How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently created Task first
    or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
    <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the TaskQueue resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the TaskQueue."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class TaskrouterV1WorkspaceTaskQueueDict(TypedDict):
    account_sid: NotRequired[str | None]
    assignment_activity_sid: NotRequired[str | None]
    assignment_activity_name: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    friendly_name: NotRequired[str | None]
    max_reserved_workers: NotRequired[int]
    reservation_activity_sid: NotRequired[str | None]
    reservation_activity_name: NotRequired[str | None]
    sid: NotRequired[str | None]
    target_workers: NotRequired[str | None]
    task_order: NotRequired[TaskQueueEnumTaskOrderOrStr]
    url: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    links: NotRequired[Any | None]
