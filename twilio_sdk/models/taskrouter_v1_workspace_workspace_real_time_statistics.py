from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceWorkspaceRealTimeStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Workspace resource."""

    activity_statistics: Optional[list[Any | None]] = UNSET
    """The number of current Workers by Activity."""

    longest_task_waiting_age: Optional[int] = UNSET
    """The age of the longest waiting Task."""

    longest_task_waiting_sid: OptionalNullable[str] = UNSET
    """The SID of the longest waiting Task."""

    tasks_by_priority: OptionalNullable[Any] = UNSET
    """The number of Tasks by priority. For example: ``{"0": "10", "99": "5"}`` shows 10 Tasks at priority 0 and 5 at
    priority 99."""

    tasks_by_status: OptionalNullable[Any] = UNSET
    """The number of Tasks by their current status. For example: ``{"pending": "1", "reserved": "3", "assigned": "2",
    "completed": "5"}``."""

    total_tasks: Optional[int] = UNSET
    """The total number of Tasks."""

    total_workers: Optional[int] = UNSET
    """The total number of Workers in the Workspace."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Workspace statistics resource."""


class TaskrouterV1WorkspaceWorkspaceRealTimeStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    activity_statistics: NotRequired[list[Any | None]]
    longest_task_waiting_age: NotRequired[int]
    longest_task_waiting_sid: NotRequired[str | None]
    tasks_by_priority: NotRequired[Any | None]
    tasks_by_status: NotRequired[Any | None]
    total_tasks: NotRequired[int]
    total_workers: NotRequired[int]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
