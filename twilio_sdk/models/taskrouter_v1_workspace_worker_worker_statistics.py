from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceWorkerWorkerStatistics(SdkBaseModel):
    realtime: OptionalNullable[Any] = UNSET
    """An object that contains the real-time statistics for the Worker."""

    cumulative: OptionalNullable[Any] = UNSET
    """An object that contains the cumulative statistics for the Worker."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Worker resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Worker."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Worker statistics resource."""


class TaskrouterV1WorkspaceWorkerWorkerStatisticsDict(TypedDict):
    realtime: NotRequired[Any | None]
    cumulative: NotRequired[Any | None]
    account_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
