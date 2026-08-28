from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_document_document_permission import (
    SyncV1ServiceDocumentDocumentPermission,
    SyncV1ServiceDocumentDocumentPermissionDict,
)


class ListDocumentPermissionResponse(SdkBaseModel):
    permissions: Optional[list[SyncV1ServiceDocumentDocumentPermission]] = UNSET
    meta: Optional[Meta] = UNSET


class ListDocumentPermissionResponseDict(TypedDict):
    permissions: NotRequired[
        list[SyncV1ServiceDocumentDocumentPermission | SyncV1ServiceDocumentDocumentPermissionDict]
    ]
    meta: NotRequired[Meta | MetaDict]
