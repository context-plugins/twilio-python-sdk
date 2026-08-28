from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .proxy_v1_service_session import ProxyV1ServiceSession, ProxyV1ServiceSessionDict


class ListSessionResponse(SdkBaseModel):
    sessions: Optional[list[ProxyV1ServiceSession]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSessionResponseDict(TypedDict):
    sessions: NotRequired[list[ProxyV1ServiceSession | ProxyV1ServiceSessionDict]]
    meta: NotRequired[Meta | MetaDict]
