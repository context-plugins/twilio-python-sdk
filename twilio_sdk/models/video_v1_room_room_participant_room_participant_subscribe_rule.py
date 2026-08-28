from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .rule import Rule, RuleDict


class VideoV1RoomRoomParticipantRoomParticipantSubscribeRule(SdkBaseModel):
    participant_sid: OptionalNullable[str] = UNSET
    """The SID of the Participant resource for the Subscribe Rules."""

    room_sid: OptionalNullable[str] = UNSET
    """The SID of the Room resource for the Subscribe Rules"""

    rules: Optional[list[Rule | None]] = UNSET
    """A collection of Subscribe Rules that describe how to include or exclude matching tracks. See the `Specifying
    Subscribe Rules <https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr>`__ section for further
    information."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""


class VideoV1RoomRoomParticipantRoomParticipantSubscribeRuleDict(TypedDict):
    participant_sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    rules: NotRequired[list[Rule | RuleDict | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
