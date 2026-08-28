from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_activity import TaskrouterV1WorkspaceActivity, TaskrouterV1WorkspaceActivityDict


class ListActivityResponse(SdkBaseModel):
    activities: Optional[list[TaskrouterV1WorkspaceActivity]] = UNSET
    meta: Optional[Meta] = UNSET


class ListActivityResponseDict(TypedDict):
    activities: NotRequired[list[TaskrouterV1WorkspaceActivity | TaskrouterV1WorkspaceActivityDict]]
    meta: NotRequired[Meta | MetaDict]
