from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ApiV2010AccountQueue(SdkBaseModel):
    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that this resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    current_size: Optional[int] = UNSET
    """The number of calls currently in the queue."""

    friendly_name: OptionalNullable[str] = UNSET
    """A string that you assigned to describe this resource."""

    uri: OptionalNullable[str] = UNSET
    """The URI of this resource, relative to ``https://api.twilio.com``."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this Queue resource."""

    average_wait_time: Optional[int] = UNSET
    """The average wait time in seconds of the members in this queue. This is calculated at the time of the request."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify this Queue resource."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that this resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    max_size: Optional[int] = UNSET
    """The maximum number of calls that can be in the queue. The default is 1000 and the maximum is 5000."""


class ApiV2010AccountQueueDict(TypedDict):
    date_updated: NotRequired[str | None]
    current_size: NotRequired[int]
    friendly_name: NotRequired[str | None]
    uri: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    average_wait_time: NotRequired[int]
    sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    max_size: NotRequired[int]
