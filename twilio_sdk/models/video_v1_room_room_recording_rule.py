from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .rule1 import Rule1, Rule1Dict


class VideoV1RoomRoomRecordingRule(SdkBaseModel):
    room_sid: OptionalNullable[str] = UNSET
    """The SID of the Room resource for the Recording Rules"""

    rules: Optional[list[Rule1 | None]] = UNSET
    """A collection of Recording Rules that describe how to include or exclude matching tracks for recording"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""


class VideoV1RoomRoomRecordingRuleDict(TypedDict):
    room_sid: NotRequired[str | None]
    rules: NotRequired[list[Rule1 | Rule1Dict | None]]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
