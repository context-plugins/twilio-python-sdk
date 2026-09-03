from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_sync_map import SyncV1ServiceSyncMap, SyncV1ServiceSyncMapDict


class ListSyncMapResponse(SdkBaseModel):
    maps: Optional[list[SyncV1ServiceSyncMap]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSyncMapResponseDict(TypedDict):
    maps: NotRequired[list[SyncV1ServiceSyncMap | SyncV1ServiceSyncMapDict]]
    meta: NotRequired[Meta | MetaDict]
