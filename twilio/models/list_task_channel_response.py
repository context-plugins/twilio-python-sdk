from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_task_channel import TaskrouterV1WorkspaceTaskChannel, TaskrouterV1WorkspaceTaskChannelDict


class ListTaskChannelResponse(SdkBaseModel):
    channels: Optional[list[TaskrouterV1WorkspaceTaskChannel]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTaskChannelResponseDict(TypedDict):
    channels: NotRequired[list[TaskrouterV1WorkspaceTaskChannel | TaskrouterV1WorkspaceTaskChannelDict]]
    meta: NotRequired[Meta | MetaDict]
