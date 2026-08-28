from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.channel3 import Channel3OrStr


class ConversationsV2SendMessageParticipant(SdkBaseModel):
    """Identifies a participant for an Action. Supports three resolution modes:
    1. participantId + channel: Resolves address from participant's registered addresses
    2. participantId only: Resolves when participant has exactly one address
    3. address + channel: Uses explicit address"""

    participant_id: Optional[str] = Field(default=UNSET, alias="participantId")
    """Participant ID to resolve address from."""

    address: Optional[str] = UNSET
    """Explicit address formatted according to channel type."""

    channel: Optional[Channel3OrStr] = UNSET
    """Channel type for address resolution."""


class ConversationsV2SendMessageParticipantDict(TypedDict):
    participant_id: NotRequired[str]
    address: NotRequired[str]
    channel: NotRequired[Channel3OrStr]
