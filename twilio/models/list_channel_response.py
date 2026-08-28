from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_channel import FlexV1Channel, FlexV1ChannelDict
from .meta import Meta, MetaDict


class ListChannelResponse(SdkBaseModel):
    flex_chat_channels: Optional[list[FlexV1Channel]] = UNSET
    meta: Optional[Meta] = UNSET


class ListChannelResponseDict(TypedDict):
    flex_chat_channels: NotRequired[list[FlexV1Channel | FlexV1ChannelDict]]
    meta: NotRequired[Meta | MetaDict]
