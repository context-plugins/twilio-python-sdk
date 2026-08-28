from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_task_queue import TaskrouterV1WorkspaceTaskQueue, TaskrouterV1WorkspaceTaskQueueDict


class ListTaskQueueResponse(SdkBaseModel):
    task_queues: Optional[list[TaskrouterV1WorkspaceTaskQueue]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTaskQueueResponseDict(TypedDict):
    task_queues: NotRequired[list[TaskrouterV1WorkspaceTaskQueue | TaskrouterV1WorkspaceTaskQueueDict]]
    meta: NotRequired[Meta | MetaDict]
