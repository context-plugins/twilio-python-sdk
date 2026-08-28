from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_worker_worker_reservation import (
    TaskrouterV1WorkspaceWorkerWorkerReservation,
    TaskrouterV1WorkspaceWorkerWorkerReservationDict,
)


class ListWorkerReservationResponse(SdkBaseModel):
    reservations: Optional[list[TaskrouterV1WorkspaceWorkerWorkerReservation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListWorkerReservationResponseDict(TypedDict):
    reservations: NotRequired[
        list[TaskrouterV1WorkspaceWorkerWorkerReservation | TaskrouterV1WorkspaceWorkerWorkerReservationDict]
    ]
    meta: NotRequired[Meta | MetaDict]
