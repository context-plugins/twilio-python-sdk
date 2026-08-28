from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v1_conference_conference_participant import (
    InsightsV1ConferenceConferenceParticipant,
    InsightsV1ConferenceConferenceParticipantDict,
)
from .meta import Meta, MetaDict


class ListConferenceParticipantResponse(SdkBaseModel):
    participants: Optional[list[InsightsV1ConferenceConferenceParticipant]] = UNSET
    meta: Optional[Meta] = UNSET


class ListConferenceParticipantResponseDict(TypedDict):
    participants: NotRequired[
        list[InsightsV1ConferenceConferenceParticipant | InsightsV1ConferenceConferenceParticipantDict]
    ]
    meta: NotRequired[Meta | MetaDict]
