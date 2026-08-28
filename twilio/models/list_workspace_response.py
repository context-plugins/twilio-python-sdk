from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace import TaskrouterV1Workspace, TaskrouterV1WorkspaceDict


class ListWorkspaceResponse(SdkBaseModel):
    workspaces: Optional[list[TaskrouterV1Workspace]] = UNSET
    meta: Optional[Meta] = UNSET


class ListWorkspaceResponseDict(TypedDict):
    workspaces: NotRequired[list[TaskrouterV1Workspace | TaskrouterV1WorkspaceDict]]
    meta: NotRequired[Meta | MetaDict]
