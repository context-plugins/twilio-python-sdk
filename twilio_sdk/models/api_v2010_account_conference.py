from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.conference_enum_reason_conference_ended import ConferenceEnumReasonConferenceEndedOrStr
from .enums.conference_enum_status import ConferenceEnumStatusOrStr


class ApiV2010AccountConference(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this Conference
    resource."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in UTC that this resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in UTC that this resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    api_version: OptionalNullable[str] = UNSET
    """The API version used to create this conference."""

    friendly_name: OptionalNullable[str] = UNSET
    """A string that you assigned to describe this conference room. Maximum length is 128 characters."""

    region: OptionalNullable[str] = UNSET
    """A string that represents the Twilio Region where the conference audio was mixed. May be ``us1``, ``us2``,
    ``ie1``, ``de1``, ``sg1``, ``br1``, ``au1``, and ``jp1``. Basic conference audio will always be mixed in ``us1``.
    Global Conference audio will be mixed nearest to the majority of participants."""

    sid: OptionalNullable[str] = UNSET
    """The unique, Twilio-provided string used to identify this Conference resource."""

    status: Optional[ConferenceEnumStatusOrStr] = UNSET
    """The status of this conference. Can be: ``init``, ``in-progress``, or ``completed``."""

    uri: OptionalNullable[str] = UNSET
    """The URI of this resource, relative to ``https://api.twilio.com``."""

    subresource_uris: OptionalNullable[Any] = UNSET
    """A list of related resources identified by their URIs relative to ``https://api.twilio.com``."""

    reason_conference_ended: Optional[ConferenceEnumReasonConferenceEndedOrStr] = UNSET
    """The reason why a conference ended. When a conference is in progress, will be ``null``. When conference is
    completed, can be: ``conference-ended-via-api``, ``participant-with-end-conference-on-exit-left``,
    ``participant-with-end-conference-on-exit-kicked``, ``last-participant-kicked``, or ``last-participant-left``."""

    call_sid_ending_conference: OptionalNullable[str] = UNSET
    """The call SID that caused the conference to end."""


class ApiV2010AccountConferenceDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    api_version: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    region: NotRequired[str | None]
    sid: NotRequired[str | None]
    status: NotRequired[ConferenceEnumStatusOrStr]
    uri: NotRequired[str | None]
    subresource_uris: NotRequired[Any | None]
    reason_conference_ended: NotRequired[ConferenceEnumReasonConferenceEndedOrStr]
    call_sid_ending_conference: NotRequired[str | None]
