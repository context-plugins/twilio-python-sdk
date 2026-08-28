from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceWorkerWorkerChannel(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Worker resource."""

    assigned_tasks: Optional[int] = UNSET
    """The total number of Tasks assigned to Worker for the TaskChannel type."""

    available: OptionalNullable[bool] = UNSET
    """Whether the Worker should receive Tasks of the TaskChannel type."""

    available_capacity_percentage: Optional[int] = UNSET
    """The current percentage of capacity the TaskChannel has available. Can be a number between ``0`` and ``100``. A
    value of ``0`` indicates that TaskChannel has no capacity available and a value of ``100`` means the Worker is
    available to receive any Tasks of this TaskChannel type."""

    configured_capacity: Optional[int] = UNSET
    """The current configured capacity for the WorkerChannel. TaskRouter will not create any reservations after the
    assigned Tasks for the Worker reaches the value."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the WorkerChannel resource."""

    task_channel_sid: OptionalNullable[str] = UNSET
    """The SID of the TaskChannel."""

    task_channel_unique_name: OptionalNullable[str] = UNSET
    """The unique name of the TaskChannel, such as ``voice`` or ``sms``."""

    worker_sid: OptionalNullable[str] = UNSET
    """The SID of the Worker that contains the WorkerChannel."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the WorkerChannel."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the WorkerChannel resource."""


class TaskrouterV1WorkspaceWorkerWorkerChannelDict(TypedDict):
    account_sid: NotRequired[str | None]
    assigned_tasks: NotRequired[int]
    available: NotRequired[bool | None]
    available_capacity_percentage: NotRequired[int]
    configured_capacity: NotRequired[int]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    sid: NotRequired[str | None]
    task_channel_sid: NotRequired[str | None]
    task_channel_unique_name: NotRequired[str | None]
    worker_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
