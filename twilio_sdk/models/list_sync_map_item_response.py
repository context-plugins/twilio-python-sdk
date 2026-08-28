from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_sync_map_sync_map_item import SyncV1ServiceSyncMapSyncMapItem, SyncV1ServiceSyncMapSyncMapItemDict


class ListSyncMapItemResponse(SdkBaseModel):
    items: Optional[list[SyncV1ServiceSyncMapSyncMapItem]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSyncMapItemResponseDict(TypedDict):
    items: NotRequired[list[SyncV1ServiceSyncMapSyncMapItem | SyncV1ServiceSyncMapSyncMapItemDict]]
    meta: NotRequired[Meta | MetaDict]
