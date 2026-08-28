from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the TaskQueue resource."""

    activity_statistics: Optional[list[Any | None]] = UNSET
    """The number of current Workers by Activity."""

    longest_task_waiting_age: Optional[int] = UNSET
    """The age of the longest waiting Task."""

    longest_task_waiting_sid: OptionalNullable[str] = UNSET
    """The SID of the longest waiting Task."""

    longest_relative_task_age_in_queue: Optional[int] = UNSET
    """The relative age in the TaskQueue for the longest waiting Task. Calculation is based on the time when the Task
    entered the TaskQueue."""

    longest_relative_task_sid_in_queue: OptionalNullable[str] = UNSET
    """The Task SID of the Task waiting in the TaskQueue the longest. Calculation is based on the time when the Task
    entered the TaskQueue."""

    task_queue_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskQueue from which these statistics were calculated."""

    tasks_by_priority: OptionalNullable[Any] = UNSET
    """The number of Tasks by priority. For example: ``{"0": "10", "99": "5"}`` shows 10 Tasks at priority 0 and 5 at
    priority 99."""

    tasks_by_status: OptionalNullable[Any] = UNSET
    """The number of Tasks by their current status. For example: ``{"pending": "1", "reserved": "3", "assigned": "2",
    "completed": "5"}``."""

    total_available_workers: Optional[int] = UNSET
    """The total number of Workers in the TaskQueue with an ``available`` status. Workers with an ``available`` status
    may already have active interactions or may have none."""

    total_eligible_workers: Optional[int] = UNSET
    """The total number of Workers eligible for Tasks in the TaskQueue, independent of their Activity state."""

    total_tasks: Optional[int] = UNSET
    """The total number of Tasks."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the TaskQueue."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the TaskQueue statistics resource."""


class TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    activity_statistics: NotRequired[list[Any | None]]
    longest_task_waiting_age: NotRequired[int]
    longest_task_waiting_sid: NotRequired[str | None]
    longest_relative_task_age_in_queue: NotRequired[int]
    longest_relative_task_sid_in_queue: NotRequired[str | None]
    task_queue_sid: NotRequired[str | None]
    tasks_by_priority: NotRequired[Any | None]
    tasks_by_status: NotRequired[Any | None]
    total_available_workers: NotRequired[int]
    total_eligible_workers: NotRequired[int]
    total_tasks: NotRequired[int]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
