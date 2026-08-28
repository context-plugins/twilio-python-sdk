from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_sync_list import SyncV1ServiceSyncList, SyncV1ServiceSyncListDict


class ListSyncListResponse(SdkBaseModel):
    lists: Optional[list[SyncV1ServiceSyncList]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSyncListResponseDict(TypedDict):
    lists: NotRequired[list[SyncV1ServiceSyncList | SyncV1ServiceSyncListDict]]
    meta: NotRequired[Meta | MetaDict]
