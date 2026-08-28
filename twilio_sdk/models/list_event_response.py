from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_event import TaskrouterV1WorkspaceEvent, TaskrouterV1WorkspaceEventDict


class ListEventResponse(SdkBaseModel):
    events: Optional[list[TaskrouterV1WorkspaceEvent]] = UNSET
    meta: Optional[Meta] = UNSET


class ListEventResponseDict(TypedDict):
    events: NotRequired[list[TaskrouterV1WorkspaceEvent | TaskrouterV1WorkspaceEventDict]]
    meta: NotRequired[Meta | MetaDict]
