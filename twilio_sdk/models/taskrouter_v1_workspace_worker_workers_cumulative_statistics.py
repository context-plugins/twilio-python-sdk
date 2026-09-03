from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Worker resource."""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The beginning of the interval during which these statistics were calculated, in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The end of the interval during which these statistics were calculated, in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    activity_durations: Optional[list[Any | None]] = UNSET
    """The minimum, average, maximum, and total time (in seconds) that Workers spent in each Activity."""

    reservations_created: Optional[int] = UNSET
    """The total number of Reservations that were created."""

    reservations_accepted: Optional[int] = UNSET
    """The total number of Reservations that were accepted."""

    reservations_rejected: Optional[int] = UNSET
    """The total number of Reservations that were rejected."""

    reservations_timed_out: Optional[int] = UNSET
    """The total number of Reservations that were timed out."""

    reservations_canceled: Optional[int] = UNSET
    """The total number of Reservations that were canceled."""

    reservations_rescinded: Optional[int] = UNSET
    """The total number of Reservations that were rescinded."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Workers."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Workers statistics resource."""


class TaskrouterV1WorkspaceWorkerWorkersCumulativeStatisticsDict(TypedDict):
    account_sid: NotRequired[str | None]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    activity_durations: NotRequired[list[Any | None]]
    reservations_created: NotRequired[int]
    reservations_accepted: NotRequired[int]
    reservations_rejected: NotRequired[int]
    reservations_timed_out: NotRequired[int]
    reservations_canceled: NotRequired[int]
    reservations_rescinded: NotRequired[int]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
