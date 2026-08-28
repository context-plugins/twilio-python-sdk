from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ApiV2010AccountQueueMember(SdkBaseModel):
    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Member resource is associated
    with."""

    date_enqueued: OptionalNullable[str] = UNSET
    """The date that the member was enqueued, given in RFC 2822 format."""

    position: Optional[int] = UNSET
    """This member's current position in the queue."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""

    wait_time: Optional[int] = UNSET
    """The number of seconds the member has been in the queue."""

    queue_sid: OptionalNullable[str] = UNSET
    """The SID of the Queue the member is in."""


class ApiV2010AccountQueueMemberDict(TypedDict):
    call_sid: NotRequired[str | None]
    date_enqueued: NotRequired[str | None]
    position: NotRequired[int]
    uri: NotRequired[str | None]
    wait_time: NotRequired[int]
    queue_sid: NotRequired[str | None]
