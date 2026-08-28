from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .proxy_v1_service import ProxyV1Service, ProxyV1ServiceDict


class ListServiceResponse3(SdkBaseModel):
    services: Optional[list[ProxyV1Service]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceResponse3Dict(TypedDict):
    services: NotRequired[list[ProxyV1Service | ProxyV1ServiceDict]]
    meta: NotRequired[Meta | MetaDict]
