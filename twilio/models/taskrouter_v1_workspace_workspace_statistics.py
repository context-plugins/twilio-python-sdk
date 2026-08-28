from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceWorkspaceStatistics(SdkBaseModel):
    realtime: OptionalNullable[Any] = UNSET
    """An object that contains the real-time statistics for the Workspace."""

    cumulative: OptionalNullable[Any] = UNSET
    """An object that contains the cumulative statistics for the Workspace."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Workspace resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Workspace statistics resource."""


class TaskrouterV1WorkspaceWorkspaceStatisticsDict(TypedDict):
    realtime: NotRequired[Any | None]
    cumulative: NotRequired[Any | None]
    account_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
