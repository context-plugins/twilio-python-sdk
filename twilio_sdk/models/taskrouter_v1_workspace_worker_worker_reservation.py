from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.worker_reservation_enum_status import WorkerReservationEnumStatusOrStr


class TaskrouterV1WorkspaceWorkerWorkerReservation(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the WorkerReservation
    resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    reservation_status: Optional[WorkerReservationEnumStatusOrStr] = UNSET
    """The current status of the reservation. Can be: ``pending``, ``accepted``, ``rejected``, ``timeout``,
    ``canceled``, or ``rescinded``."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the WorkerReservation resource."""

    task_sid: OptionalNullable[str] = UNSET
    """The SID of the reserved Task resource."""

    worker_name: OptionalNullable[str] = UNSET
    """The ``friendly_name`` of the Worker that is reserved."""

    worker_sid: OptionalNullable[str] = UNSET
    """The SID of the reserved Worker resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that this worker is contained within."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the WorkerReservation resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class TaskrouterV1WorkspaceWorkerWorkerReservationDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    reservation_status: NotRequired[WorkerReservationEnumStatusOrStr]
    sid: NotRequired[str | None]
    task_sid: NotRequired[str | None]
    worker_name: NotRequired[str | None]
    worker_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
