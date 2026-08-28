from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .configuration3 import Configuration3, Configuration3Dict
from .participant import Participant, ParticipantDict


class V2ConversationsRequest(SdkBaseModel):
    configuration_id: str = Field(alias="configurationId")
    """The ID of an existing configuration."""

    name: Optional[str] = UNSET
    """The name of the conversation."""

    configuration: Optional[Configuration3] = UNSET
    """Conversation configuration settings."""

    participants: Optional[list[Participant]] = UNSET
    """Optional list of Participants to create with the Conversation."""


class V2ConversationsRequestDict(TypedDict):
    configuration_id: str
    name: NotRequired[str]
    configuration: NotRequired[Configuration3 | Configuration3Dict]
    participants: NotRequired[list[Participant | ParticipantDict]]
