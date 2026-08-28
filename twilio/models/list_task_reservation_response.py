from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_task_task_reservation import (
    TaskrouterV1WorkspaceTaskTaskReservation,
    TaskrouterV1WorkspaceTaskTaskReservationDict,
)


class ListTaskReservationResponse(SdkBaseModel):
    reservations: Optional[list[TaskrouterV1WorkspaceTaskTaskReservation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTaskReservationResponseDict(TypedDict):
    reservations: NotRequired[
        list[TaskrouterV1WorkspaceTaskTaskReservation | TaskrouterV1WorkspaceTaskTaskReservationDict]
    ]
    meta: NotRequired[Meta | MetaDict]
