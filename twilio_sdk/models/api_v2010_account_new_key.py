from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountNewKey(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that that we created to identify the NewKey resource. You will use this as the basic-auth
    ``user`` when authenticating to the API."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    date_created: OptionalNullable[str] = UNSET
    """The date and time in GMT that the API Key was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date and time in GMT that the new API Key was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    secret: OptionalNullable[str] = UNSET
    """The secret your application uses to sign Access Tokens and to authenticate to the REST API (you will use this as
    the basic-auth ``password``). **Note that for security reasons, this field is ONLY returned when the API Key is
    first created.**"""


class ApiV2010AccountNewKeyDict(TypedDict):
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    secret: NotRequired[str | None]
