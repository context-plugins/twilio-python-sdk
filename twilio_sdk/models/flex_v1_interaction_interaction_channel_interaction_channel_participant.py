from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.interaction_channel_participant_enum_type import InteractionChannelParticipantEnumTypeOrStr


class FlexV1InteractionInteractionChannelInteractionChannelParticipant(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string created by Twilio to identify an Interaction Channel Participant resource."""

    type_: Optional[InteractionChannelParticipantEnumTypeOrStr] = Field(default=UNSET, alias="type")
    """Participant type. Can be: ``agent``, ``customer``, ``supervisor``, ``external``, ``unknown``"""

    interaction_sid: OptionalNullable[str] = UNSET
    """The Interaction Sid for this channel."""

    channel_sid: OptionalNullable[str] = UNSET
    """The Channel Sid for this Participant."""

    url: OptionalNullable[AnyUrl] = UNSET
    routing_properties: OptionalNullable[Any] = UNSET
    """The Participant's routing properties."""


class FlexV1InteractionInteractionChannelInteractionChannelParticipantDict(TypedDict):
    sid: NotRequired[str | None]
    type_: NotRequired[InteractionChannelParticipantEnumTypeOrStr]
    interaction_sid: NotRequired[str | None]
    channel_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    routing_properties: NotRequired[Any | None]
