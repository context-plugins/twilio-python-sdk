from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_service_destination_alpha_sender import (
    MessagingV1ServiceDestinationAlphaSender,
    MessagingV1ServiceDestinationAlphaSenderDict,
)
from .meta import Meta, MetaDict


class ListDestinationAlphaSenderResponse(SdkBaseModel):
    alpha_senders: Optional[list[MessagingV1ServiceDestinationAlphaSender]] = UNSET
    meta: Optional[Meta] = UNSET


class ListDestinationAlphaSenderResponseDict(TypedDict):
    alpha_senders: NotRequired[
        list[MessagingV1ServiceDestinationAlphaSender | MessagingV1ServiceDestinationAlphaSenderDict]
    ]
    meta: NotRequired[Meta | MetaDict]
