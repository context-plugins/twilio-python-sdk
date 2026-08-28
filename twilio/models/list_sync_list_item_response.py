from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_sync_list_sync_list_item import (
    SyncV1ServiceSyncListSyncListItem,
    SyncV1ServiceSyncListSyncListItemDict,
)


class ListSyncListItemResponse(SdkBaseModel):
    items: Optional[list[SyncV1ServiceSyncListSyncListItem]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSyncListItemResponseDict(TypedDict):
    items: NotRequired[list[SyncV1ServiceSyncListSyncListItem | SyncV1ServiceSyncListSyncListItemDict]]
    meta: NotRequired[Meta | MetaDict]
