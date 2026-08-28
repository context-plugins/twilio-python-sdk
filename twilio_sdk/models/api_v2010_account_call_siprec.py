from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.siprec_enum_status import SiprecEnumStatusOrStr


class ApiV2010AccountCallSiprec(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The SID of the Siprec resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created this Siprec resource."""

    call_sid: OptionalNullable[str] = UNSET
    """The SID of the `Call <https://www.twilio.com/docs/voice/api/call-resource>`__ the Siprec resource is associated
    with."""

    name: OptionalNullable[str] = UNSET
    """The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used to stop
    the Siprec."""

    status: Optional[SiprecEnumStatusOrStr] = UNSET
    """The status - one of ``stopped``, ``in-progress``"""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that this resource was last updated, specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    uri: OptionalNullable[str] = UNSET
    """The URI of the resource, relative to ``https://api.twilio.com``."""


class ApiV2010AccountCallSiprecDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    call_sid: NotRequired[str | None]
    name: NotRequired[str | None]
    status: NotRequired[SiprecEnumStatusOrStr]
    date_updated: NotRequired[str | None]
    uri: NotRequired[str | None]
