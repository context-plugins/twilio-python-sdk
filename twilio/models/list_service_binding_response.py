from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .conversations_v1_service_service_binding import (
    ConversationsV1ServiceServiceBinding,
    ConversationsV1ServiceServiceBindingDict,
)
from .meta import Meta, MetaDict


class ListServiceBindingResponse(SdkBaseModel):
    bindings: Optional[list[ConversationsV1ServiceServiceBinding]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceBindingResponseDict(TypedDict):
    bindings: NotRequired[list[ConversationsV1ServiceServiceBinding | ConversationsV1ServiceServiceBindingDict]]
    meta: NotRequired[Meta | MetaDict]
