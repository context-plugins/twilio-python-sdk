from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_web_channel import FlexV1WebChannel, FlexV1WebChannelDict
from .meta import Meta, MetaDict


class ListWebChannelResponse(SdkBaseModel):
    flex_chat_channels: Optional[list[FlexV1WebChannel]] = UNSET
    meta: Optional[Meta] = UNSET


class ListWebChannelResponseDict(TypedDict):
    flex_chat_channels: NotRequired[list[FlexV1WebChannel | FlexV1WebChannelDict]]
    meta: NotRequired[Meta | MetaDict]
