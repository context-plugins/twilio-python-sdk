from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceTaskQueueTaskQueuesStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the TaskQueue resource."""

    cumulative: OptionalNullable[Any] = UNSET
    """An object that contains the cumulative statistics for the TaskQueues."""

    realtime: OptionalNullable[Any] = UNSET
    """An object that contains the real-time statistics for the TaskQueues."""

    task_queue_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskQueue from which these statistics were calculated."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the TaskQueues."""


class TaskrouterV1WorkspaceTaskQueueTaskQueuesStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    cumulative: NotRequired[Any | None]
    realtime: NotRequired[Any | None]
    task_queue_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
