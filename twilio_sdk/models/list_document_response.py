from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service_document import SyncV1ServiceDocument, SyncV1ServiceDocumentDict


class ListDocumentResponse(SdkBaseModel):
    documents: Optional[list[SyncV1ServiceDocument]] = UNSET
    meta: Optional[Meta] = UNSET


class ListDocumentResponseDict(TypedDict):
    documents: NotRequired[list[SyncV1ServiceDocument | SyncV1ServiceDocumentDict]]
    meta: NotRequired[Meta | MetaDict]
