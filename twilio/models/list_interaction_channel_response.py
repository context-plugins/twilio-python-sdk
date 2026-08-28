from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flex_v1_interaction_interaction_channel import (
    FlexV1InteractionInteractionChannel,
    FlexV1InteractionInteractionChannelDict,
)
from .meta import Meta, MetaDict


class ListInteractionChannelResponse(SdkBaseModel):
    channels: Optional[list[FlexV1InteractionInteractionChannel]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInteractionChannelResponseDict(TypedDict):
    channels: NotRequired[list[FlexV1InteractionInteractionChannel | FlexV1InteractionInteractionChannelDict]]
    meta: NotRequired[Meta | MetaDict]
