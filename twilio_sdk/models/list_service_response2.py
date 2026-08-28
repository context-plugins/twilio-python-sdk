from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service import ConversationsV1Service, ConversationsV1ServiceDict
from .meta import Meta, MetaDict


class ListServiceResponse2(SdkBaseModel):
    services: Optional[list[ConversationsV1Service]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceResponse2Dict(TypedDict):
    services: NotRequired[list[ConversationsV1Service | ConversationsV1ServiceDict]]
    meta: NotRequired[Meta | MetaDict]
