from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_worker import TaskrouterV1WorkspaceWorker, TaskrouterV1WorkspaceWorkerDict


class ListWorkerResponse(SdkBaseModel):
    workers: Optional[list[TaskrouterV1WorkspaceWorker]] = UNSET
    meta: Optional[Meta] = UNSET


class ListWorkerResponseDict(TypedDict):
    workers: NotRequired[list[TaskrouterV1WorkspaceWorker | TaskrouterV1WorkspaceWorkerDict]]
    meta: NotRequired[Meta | MetaDict]
