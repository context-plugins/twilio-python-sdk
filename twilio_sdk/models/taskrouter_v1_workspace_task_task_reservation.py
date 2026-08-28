from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.task_reservation_enum_status import TaskReservationEnumStatusOrStr


class TaskrouterV1WorkspaceTaskTaskReservation(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the TaskReservation
    resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    reservation_status: Optional[TaskReservationEnumStatusOrStr] = UNSET
    """The current status of the reservation. Can be: ``pending``, ``accepted``, ``rejected``, or ``timeout``."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the TaskReservation resource."""

    task_sid: OptionalNullable[str] = UNSET
    """The SID of the reserved Task resource."""

    worker_name: OptionalNullable[str] = UNSET
    """The ``friendly_name`` of the Worker that is reserved."""

    worker_sid: OptionalNullable[str] = UNSET
    """The SID of the reserved Worker resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that this task is contained within."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the TaskReservation reservation."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class TaskrouterV1WorkspaceTaskTaskReservationDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    reservation_status: NotRequired[TaskReservationEnumStatusOrStr]
    sid: NotRequired[str | None]
    task_sid: NotRequired[str | None]
    worker_name: NotRequired[str | None]
    worker_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
