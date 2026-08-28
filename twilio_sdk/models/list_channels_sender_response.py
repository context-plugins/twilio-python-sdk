from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v2_channels_sender_response import (
    MessagingV2ChannelsSenderResponse,
    MessagingV2ChannelsSenderResponseDict,
)
from .meta import Meta, MetaDict


class ListChannelsSenderResponse(SdkBaseModel):
    senders: Optional[list[MessagingV2ChannelsSenderResponse]] = UNSET
    meta: Optional[Meta] = UNSET


class ListChannelsSenderResponseDict(TypedDict):
    senders: NotRequired[list[MessagingV2ChannelsSenderResponse | MessagingV2ChannelsSenderResponseDict]]
    meta: NotRequired[Meta | MetaDict]
