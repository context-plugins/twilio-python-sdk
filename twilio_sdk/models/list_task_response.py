from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_task import TaskrouterV1WorkspaceTask, TaskrouterV1WorkspaceTaskDict


class ListTaskResponse(SdkBaseModel):
    tasks: Optional[list[TaskrouterV1WorkspaceTask]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTaskResponseDict(TypedDict):
    tasks: NotRequired[list[TaskrouterV1WorkspaceTask | TaskrouterV1WorkspaceTaskDict]]
    meta: NotRequired[Meta | MetaDict]
