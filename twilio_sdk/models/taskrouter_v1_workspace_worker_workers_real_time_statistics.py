from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceWorkerWorkersRealTimeStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Worker resource."""

    activity_statistics: Optional[list[Any | None]] = UNSET
    """The number of current Workers by Activity."""

    total_workers: Optional[int] = UNSET
    """The total number of Workers."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Workers."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Workers statistics resource."""


class TaskrouterV1WorkspaceWorkerWorkersRealTimeStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    activity_statistics: NotRequired[list[Any | None]]
    total_workers: NotRequired[int]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
