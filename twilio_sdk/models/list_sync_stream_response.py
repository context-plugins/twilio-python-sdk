from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_sync_stream import SyncV1ServiceSyncStream, SyncV1ServiceSyncStreamDict


class ListSyncStreamResponse(SdkBaseModel):
    streams: Optional[list[SyncV1ServiceSyncStream]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSyncStreamResponseDict(TypedDict):
    streams: NotRequired[list[SyncV1ServiceSyncStream | SyncV1ServiceSyncStreamDict]]
    meta: NotRequired[Meta | MetaDict]
