from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .taskrouter_v1_workspace_worker_worker_channel import (
    TaskrouterV1WorkspaceWorkerWorkerChannel,
    TaskrouterV1WorkspaceWorkerWorkerChannelDict,
)


class ListWorkerChannelResponse(SdkBaseModel):
    channels: Optional[list[TaskrouterV1WorkspaceWorkerWorkerChannel]] = UNSET
    meta: Optional[Meta] = UNSET


class ListWorkerChannelResponseDict(TypedDict):
    channels: NotRequired[list[TaskrouterV1WorkspaceWorkerWorkerChannel | TaskrouterV1WorkspaceWorkerWorkerChannelDict]]
    meta: NotRequired[Meta | MetaDict]
