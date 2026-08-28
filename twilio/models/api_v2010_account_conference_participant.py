from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.participant_enum_status import ParticipantEnumStatusOrStr


class ApiV2010AccountConferenceParticipant(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Participant
    resource."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Participant resource is
    associated with."""

    label: OptionalNullable[str] = UNSET
    """The user-specified label of this participant, if one was given when the participant was created. This may be used
    to fetch, update or delete the participant."""

    call_sid_to_coach: OptionalNullable[str] = UNSET
    """The SID of the participant who is being ``coached``. The participant being coached is the only participant who
    can hear the participant who is ``coaching``."""

    coaching: OptionalNullable[bool] = UNSET
    """Whether the participant is coaching another call. Can be: ``true`` or ``false``. If not present, defaults to
    ``false`` unless ``call_sid_to_coach`` is defined. If ``true``, ``call_sid_to_coach`` must be defined."""

    conference_sid: OptionalNullable[str] = UNSET
    """The SID of the conference the participant is in."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    end_conference_on_exit: OptionalNullable[bool] = UNSET
    """Whether the conference ends when the participant leaves. Can be: ``true`` or ``false`` and the default is
    ``false``. If ``true``, the conference ends and all other participants drop out when the participant leaves."""

    muted: OptionalNullable[bool] = UNSET
    """Whether the participant is muted. Can be ``true`` or ``false``."""

    hold: OptionalNullable[bool] = UNSET
    """Whether the participant is on hold. Can be ``true`` or ``false``."""

    start_conference_on_enter: OptionalNullable[bool] = UNSET
    """Whether the conference starts when the participant joins the conference, if it has not already started. Can be:
    ``true`` or ``false`` and the default is ``true``. If ``false`` and the conference has not started, the participant
    is muted and hears background music until another participant starts the conference."""

    status: Optional[ParticipantEnumStatusOrStr] = UNSET
    """The status of the participant's call in a session. Can be: ``queued``, ``connecting``, ``ringing``,
    ``connected``, ``complete``, or ``failed``."""

    queue_time: OptionalNullable[str] = UNSET
    """The wait time in milliseconds before participant's call is placed. Only available in the response to a create
    participant request."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountConferenceParticipantDict(TypedDict):
    account_sid: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    label: NotRequired[str | None]
    call_sid_to_coach: NotRequired[str | None]
    coaching: NotRequired[bool | None]
    conference_sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    end_conference_on_exit: NotRequired[bool | None]
    muted: NotRequired[bool | None]
    hold: NotRequired[bool | None]
    start_conference_on_enter: NotRequired[bool | None]
    status: NotRequired[ParticipantEnumStatusOrStr]
    queue_time: NotRequired[str | None]
    uri: NotRequired[str | None]
