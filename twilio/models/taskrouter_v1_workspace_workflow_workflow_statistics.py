from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceWorkflowWorkflowStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Workflow resource."""

    cumulative: OptionalNullable[Any] = UNSET
    """An object that contains the cumulative statistics for the Workflow."""

    realtime: OptionalNullable[Any] = UNSET
    """An object that contains the real-time statistics for the Workflow."""

    workflow_sid: OptionalNullable[str] = UNSET
    """Returns the list of Tasks that are being controlled by the Workflow with the specified SID value."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Workflow."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Workflow statistics resource."""


class TaskrouterV1WorkspaceWorkflowWorkflowStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    cumulative: NotRequired[Any | None]
    realtime: NotRequired[Any | None]
    workflow_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
