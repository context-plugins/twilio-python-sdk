from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .sync_v1_service import SyncV1Service, SyncV1ServiceDict


class ListServiceResponse4(SdkBaseModel):
    services: Optional[list[SyncV1Service]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceResponse4Dict(TypedDict):
    services: NotRequired[list[SyncV1Service | SyncV1ServiceDict]]
    meta: NotRequired[Meta | MetaDict]
