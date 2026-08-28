from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_service_alpha_sender import MessagingV1ServiceAlphaSender, MessagingV1ServiceAlphaSenderDict
from .meta import Meta, MetaDict


class ListAlphaSenderResponse(SdkBaseModel):
    alpha_senders: Optional[list[MessagingV1ServiceAlphaSender]] = UNSET
    meta: Optional[Meta] = UNSET


class ListAlphaSenderResponseDict(TypedDict):
    alpha_senders: NotRequired[list[MessagingV1ServiceAlphaSender | MessagingV1ServiceAlphaSenderDict]]
    meta: NotRequired[Meta | MetaDict]
