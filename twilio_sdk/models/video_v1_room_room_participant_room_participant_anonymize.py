from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.room_participant_anonymize_enum_status import RoomParticipantAnonymizeEnumStatusOrStr


class VideoV1RoomRoomParticipantRoomParticipantAnonymize(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the RoomParticipant resource."""

    room_sid: OptionalNullable[str] = UNSET
    """The SID of the participant's room."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the RoomParticipant
    resource."""

    status: Optional[RoomParticipantAnonymizeEnumStatusOrStr] = UNSET
    """The status of the Participant. Can be: ``connected`` or ``disconnected``."""

    identity: OptionalNullable[str] = UNSET
    """The SID of the participant."""

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

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""


class VideoV1RoomRoomParticipantRoomParticipantAnonymizeDict(TypedDict):
    sid: NotRequired[str | None]
    room_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    status: NotRequired[RoomParticipantAnonymizeEnumStatusOrStr]
    identity: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    duration: NotRequired[int | None]
    url: NotRequired[AnyUrl | None]
