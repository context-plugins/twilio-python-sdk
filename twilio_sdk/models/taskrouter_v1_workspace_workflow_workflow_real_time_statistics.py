from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Workflow resource."""

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

    workflow_sid: OptionalNullable[str] = UNSET
    """Returns the list of Tasks that are being controlled by the Workflow with the specified SID value."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Workflow."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Workflow statistics resource."""


class TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    longest_task_waiting_age: NotRequired[int]
    longest_task_waiting_sid: NotRequired[str | None]
    tasks_by_priority: NotRequired[Any | None]
    tasks_by_status: NotRequired[Any | None]
    total_tasks: NotRequired[int]
    workflow_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
