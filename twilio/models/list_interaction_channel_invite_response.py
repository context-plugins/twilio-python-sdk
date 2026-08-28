from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_interaction_interaction_channel_interaction_channel_invite import (
    FlexV1InteractionInteractionChannelInteractionChannelInvite,
    FlexV1InteractionInteractionChannelInteractionChannelInviteDict,
)
from .meta import Meta, MetaDict


class ListInteractionChannelInviteResponse(SdkBaseModel):
    invites: Optional[list[FlexV1InteractionInteractionChannelInteractionChannelInvite]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInteractionChannelInviteResponseDict(TypedDict):
    invites: NotRequired[
        list[
            (
                FlexV1InteractionInteractionChannelInteractionChannelInvite
                | FlexV1InteractionInteractionChannelInteractionChannelInviteDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
