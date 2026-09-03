from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the TaskQueue resource."""

    avg_task_acceptance_time: Optional[int] = UNSET
    """The average time in seconds between Task creation and acceptance."""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The beginning of the interval during which these statistics were calculated, in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The end of the interval during which these statistics were calculated, in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    reservations_created: Optional[int] = UNSET
    """The total number of Reservations created for Tasks in the TaskQueue."""

    reservations_accepted: Optional[int] = UNSET
    """The total number of Reservations accepted for Tasks in the TaskQueue."""

    reservations_rejected: Optional[int] = UNSET
    """The total number of Reservations rejected for Tasks in the TaskQueue."""

    reservations_timed_out: Optional[int] = UNSET
    """The total number of Reservations that timed out for Tasks in the TaskQueue."""

    reservations_canceled: Optional[int] = UNSET
    """The total number of Reservations canceled for Tasks in the TaskQueue."""

    reservations_rescinded: Optional[int] = UNSET
    """The total number of Reservations rescinded."""

    split_by_wait_time: OptionalNullable[Any] = UNSET
    """A list of objects that describe the number of Tasks canceled and reservations accepted above and below the
    thresholds specified in seconds."""

    task_queue_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskQueue from which these statistics were calculated."""

    wait_duration_until_accepted: OptionalNullable[Any] = UNSET
    """The wait duration statistics (``avg``, ``min``, ``max``, ``total``) for Tasks accepted while in the TaskQueue.
    Calculation is based on the time when the Tasks were created. For transfers, the wait duration is counted from the
    moment ***the Task was created***, and not from when the transfer was initiated."""

    wait_duration_until_canceled: OptionalNullable[Any] = UNSET
    """The wait duration statistics (``avg``, ``min``, ``max``, ``total``) for Tasks canceled while in the TaskQueue."""

    wait_duration_in_queue_until_accepted: OptionalNullable[Any] = UNSET
    """The relative wait duration statistics (``avg``, ``min``, ``max``, ``total``) for Tasks accepted while in the
    TaskQueue. Calculation is based on the time when the Tasks entered the TaskQueue."""

    tasks_canceled: Optional[int] = UNSET
    """The total number of Tasks canceled in the TaskQueue."""

    tasks_completed: Optional[int] = UNSET
    """The total number of Tasks completed in the TaskQueue."""

    tasks_deleted: Optional[int] = UNSET
    """The total number of Tasks deleted in the TaskQueue."""

    tasks_entered: Optional[int] = UNSET
    """The total number of Tasks entered into the TaskQueue."""

    tasks_moved: Optional[int] = UNSET
    """The total number of Tasks that were moved from one queue to another."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the TaskQueue."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the TaskQueue statistics resource."""


class TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    avg_task_acceptance_time: NotRequired[int]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    reservations_created: NotRequired[int]
    reservations_accepted: NotRequired[int]
    reservations_rejected: NotRequired[int]
    reservations_timed_out: NotRequired[int]
    reservations_canceled: NotRequired[int]
    reservations_rescinded: NotRequired[int]
    split_by_wait_time: NotRequired[Any | None]
    task_queue_sid: NotRequired[str | None]
    wait_duration_until_accepted: NotRequired[Any | None]
    wait_duration_until_canceled: NotRequired[Any | None]
    wait_duration_in_queue_until_accepted: NotRequired[Any | None]
    tasks_canceled: NotRequired[int]
    tasks_completed: NotRequired[int]
    tasks_deleted: NotRequired[int]
    tasks_entered: NotRequired[int]
    tasks_moved: NotRequired[int]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
