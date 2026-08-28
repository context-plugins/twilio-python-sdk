from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .proxy_v1_service_session_participant import ProxyV1ServiceSessionParticipant, ProxyV1ServiceSessionParticipantDict


class ListParticipantResponse1(SdkBaseModel):
    participants: Optional[list[ProxyV1ServiceSessionParticipant]] = UNSET
    meta: Optional[Meta] = UNSET


class ListParticipantResponse1Dict(TypedDict):
    participants: NotRequired[list[ProxyV1ServiceSessionParticipant | ProxyV1ServiceSessionParticipantDict]]
    meta: NotRequired[Meta | MetaDict]
