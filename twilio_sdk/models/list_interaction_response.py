from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .proxy_v1_service_session_interaction import ProxyV1ServiceSessionInteraction, ProxyV1ServiceSessionInteractionDict


class ListInteractionResponse(SdkBaseModel):
    interactions: Optional[list[ProxyV1ServiceSessionInteraction]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInteractionResponseDict(TypedDict):
    interactions: NotRequired[list[ProxyV1ServiceSessionInteraction | ProxyV1ServiceSessionInteractionDict]]
    meta: NotRequired[Meta | MetaDict]
