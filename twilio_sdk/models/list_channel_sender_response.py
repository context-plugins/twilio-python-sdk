from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_service_channel_sender import MessagingV1ServiceChannelSender, MessagingV1ServiceChannelSenderDict
from .meta import Meta, MetaDict


class ListChannelSenderResponse(SdkBaseModel):
    senders: Optional[list[MessagingV1ServiceChannelSender]] = UNSET
    meta: Optional[Meta] = UNSET


class ListChannelSenderResponseDict(TypedDict):
    senders: NotRequired[list[MessagingV1ServiceChannelSender | MessagingV1ServiceChannelSenderDict]]
    meta: NotRequired[Meta | MetaDict]
