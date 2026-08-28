from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_sync_map_sync_map_permission import (
    SyncV1ServiceSyncMapSyncMapPermission,
    SyncV1ServiceSyncMapSyncMapPermissionDict,
)


class ListSyncMapPermissionResponse(SdkBaseModel):
    permissions: Optional[list[SyncV1ServiceSyncMapSyncMapPermission]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSyncMapPermissionResponseDict(TypedDict):
    permissions: NotRequired[list[SyncV1ServiceSyncMapSyncMapPermission | SyncV1ServiceSyncMapSyncMapPermissionDict]]
    meta: NotRequired[Meta | MetaDict]
