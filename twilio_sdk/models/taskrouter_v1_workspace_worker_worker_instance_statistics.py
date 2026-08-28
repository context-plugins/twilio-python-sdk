from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Worker resource."""

    cumulative: OptionalNullable[Any] = UNSET
    """An object that contains the cumulative statistics for the Worker."""

    worker_sid: OptionalNullable[str] = UNSET
    """The SID of the Worker that contains the WorkerChannel."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the WorkerChannel."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the WorkerChannel statistics resource."""


class TaskrouterV1WorkspaceWorkerWorkerInstanceStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    cumulative: NotRequired[Any | None]
    worker_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
