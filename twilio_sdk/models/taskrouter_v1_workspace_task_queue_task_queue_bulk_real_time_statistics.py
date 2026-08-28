from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the TaskQueue resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the TaskQueue."""

    task_queue_data: Optional[list[Any | None]] = UNSET
    """The real-time statistics for each requested TaskQueue SID. ``task_queue_data`` returns the following attributes:

    ``task_queue_sid``: The SID of the TaskQueue from which these statistics were calculated.

    ``total_available_workers``: The total number of Workers available for Tasks in the TaskQueue.

    ``total_eligible_workers``: The total number of Workers eligible for Tasks in the TaskQueue, regardless of their
    Activity state.

    ``total_tasks``: The total number of Tasks.

    ``longest_task_waiting_age``: The age of the longest waiting Task.

    ``longest_task_waiting_sid``: The SID of the longest waiting Task.

    ``tasks_by_status``: The number of Tasks grouped by their current status.

    ``tasks_by_priority``: The number of Tasks grouped by priority.

    ``activity_statistics``: The number of current Workers grouped by Activity."""

    task_queue_response_count: Optional[int] = UNSET
    """The number of TaskQueue statistics received in task_queue_data."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the TaskQueue statistics resource."""


class TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    task_queue_data: NotRequired[list[Any | None]]
    task_queue_response_count: NotRequired[int]
    url: NotRequired[AnyUrl | None]
