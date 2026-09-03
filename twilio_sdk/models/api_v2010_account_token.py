from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .ice_server import IceServer, IceServerDict


class ApiV2010AccountToken(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Token resource."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    ice_servers: Optional[list[IceServer | None]] = UNSET
    """An array representing the ephemeral credentials and the STUN and TURN server URIs."""

    password: OptionalNullable[str] = UNSET
    """The temporary password that the username will use when authenticating with Twilio."""

    ttl: OptionalNullable[str] = UNSET
    """The duration in seconds for which the username and password are valid."""

    username: OptionalNullable[str] = UNSET
    """The temporary username that uniquely identifies a Token."""


class ApiV2010AccountTokenDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    ice_servers: NotRequired[list[IceServer | IceServerDict | None]]
    password: NotRequired[str | None]
    ttl: NotRequired[str | None]
    username: NotRequired[str | None]
