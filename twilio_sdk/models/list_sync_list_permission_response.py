from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_sync_list_sync_list_permission import (
    SyncV1ServiceSyncListSyncListPermission,
    SyncV1ServiceSyncListSyncListPermissionDict,
)


class ListSyncListPermissionResponse(SdkBaseModel):
    permissions: Optional[list[SyncV1ServiceSyncListSyncListPermission]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSyncListPermissionResponseDict(TypedDict):
    permissions: NotRequired[
        list[SyncV1ServiceSyncListSyncListPermission | SyncV1ServiceSyncListSyncListPermissionDict]
    ]
    meta: NotRequired[Meta | MetaDict]
