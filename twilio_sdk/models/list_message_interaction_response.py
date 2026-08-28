from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .proxy_v1_service_session_participant_message_interaction import (
    ProxyV1ServiceSessionParticipantMessageInteraction,
    ProxyV1ServiceSessionParticipantMessageInteractionDict,
)


class ListMessageInteractionResponse(SdkBaseModel):
    interactions: Optional[list[ProxyV1ServiceSessionParticipantMessageInteraction]] = UNSET
    meta: Optional[Meta] = UNSET


class ListMessageInteractionResponseDict(TypedDict):
    interactions: NotRequired[
        list[
            ProxyV1ServiceSessionParticipantMessageInteraction | ProxyV1ServiceSessionParticipantMessageInteractionDict
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
