from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceWorkspaceCumulativeStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Workspace resource."""

    avg_task_acceptance_time: Optional[int] = UNSET
    """The average time in seconds between Task creation and acceptance."""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The beginning of the interval during which these statistics were calculated, in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The end of the interval during which these statistics were calculated, in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    reservations_created: Optional[int] = UNSET
    """The total number of Reservations that were created for Workers."""

    reservations_accepted: Optional[int] = UNSET
    """The total number of Reservations accepted by Workers."""

    reservations_rejected: Optional[int] = UNSET
    """The total number of Reservations that were rejected."""

    reservations_timed_out: Optional[int] = UNSET
    """The total number of Reservations that were timed out."""

    reservations_canceled: Optional[int] = UNSET
    """The total number of Reservations that were canceled."""

    reservations_rescinded: Optional[int] = UNSET
    """The total number of Reservations that were rescinded."""

    split_by_wait_time: OptionalNullable[Any] = UNSET
    """A list of objects that describe the number of Tasks canceled and reservations accepted above and below the
    thresholds specified in seconds."""

    wait_duration_until_accepted: OptionalNullable[Any] = UNSET
    """The wait duration statistics (``avg``, ``min``, ``max``, ``total``) for Tasks that were accepted."""

    wait_duration_until_canceled: OptionalNullable[Any] = UNSET
    """The wait duration statistics (``avg``, ``min``, ``max``, ``total``) for Tasks that were canceled."""

    tasks_canceled: Optional[int] = UNSET
    """The total number of Tasks that were canceled."""

    tasks_completed: Optional[int] = UNSET
    """The total number of Tasks that were completed."""

    tasks_created: Optional[int] = UNSET
    """The total number of Tasks created."""

    tasks_deleted: Optional[int] = UNSET
    """The total number of Tasks that were deleted."""

    tasks_moved: Optional[int] = UNSET
    """The total number of Tasks that were moved from one queue to another."""

    tasks_timed_out_in_workflow: Optional[int] = UNSET
    """The total number of Tasks that were timed out of their Workflows (and deleted)."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Workspace statistics resource."""


class TaskrouterV1WorkspaceWorkspaceCumulativeStatisticsDict(TypedDict):
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
    wait_duration_until_accepted: NotRequired[Any | None]
    wait_duration_until_canceled: NotRequired[Any | None]
    tasks_canceled: NotRequired[int]
    tasks_completed: NotRequired[int]
    tasks_created: NotRequired[int]
    tasks_deleted: NotRequired[int]
    tasks_moved: NotRequired[int]
    tasks_timed_out_in_workflow: NotRequired[int]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
