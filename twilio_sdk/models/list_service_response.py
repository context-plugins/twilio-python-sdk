from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_service import MessagingV1Service, MessagingV1ServiceDict
from .meta import Meta, MetaDict


class ListServiceResponse(SdkBaseModel):
    services: Optional[list[MessagingV1Service]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceResponseDict(TypedDict):
    services: NotRequired[list[MessagingV1Service | MessagingV1ServiceDict]]
    meta: NotRequired[Meta | MetaDict]
