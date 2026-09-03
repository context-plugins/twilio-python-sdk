from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_interaction_interaction_channel_interaction_channel_participant import (
    FlexV1InteractionInteractionChannelInteractionChannelParticipant,
    FlexV1InteractionInteractionChannelInteractionChannelParticipantDict,
)
from .meta import Meta, MetaDict


class ListInteractionChannelParticipantResponse(SdkBaseModel):
    participants: Optional[list[FlexV1InteractionInteractionChannelInteractionChannelParticipant]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInteractionChannelParticipantResponseDict(TypedDict):
    participants: NotRequired[
        list[
            (
                FlexV1InteractionInteractionChannelInteractionChannelParticipant
                | FlexV1InteractionInteractionChannelInteractionChannelParticipantDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
