from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.room_participant_enum_status import RoomParticipantEnumStatusOrStr


class VideoV1RoomRoomParticipant(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the RoomParticipant resource."""

    room_sid: OptionalNullable[str] = UNSET
    """The SID of the participant's room."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the RoomParticipant
    resource."""

    status: Optional[RoomParticipantEnumStatusOrStr] = UNSET
    """The status of the Participant. Can be: ``connected`` or ``disconnected``."""

    identity: OptionalNullable[str] = UNSET
    """The application-defined string that uniquely identifies the resource's User within a Room. If a client joins with
    an existing Identity, the existing client is disconnected. See `access tokens
    <https://www.twilio.com/docs/video/tutorials/user-identity-access-tokens>`__ and `limits
    <https://www.twilio.com/docs/video/programmable-video-limits>`__ for more info."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The time of participant connected to the room in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__
    format."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The time when the participant disconnected from the room in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601#UTC>`__ format."""

    duration: OptionalNullable[int] = UNSET
    """The duration in seconds that the participant was ``connected``. Populated only after the participant is
    ``disconnected``."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class VideoV1RoomRoomParticipantDict(TypedDict):
    sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    status: NotRequired[RoomParticipantEnumStatusOrStr]
    identity: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    duration: NotRequired[int | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
