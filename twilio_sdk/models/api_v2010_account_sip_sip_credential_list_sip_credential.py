from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountSipSipCredentialListSipCredential(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique id of the Account that is responsible for this resource."""

    credential_list_sid: OptionalNullable[str] = UNSET
    """The unique id that identifies the credential list that includes this credential."""

    username: OptionalNullable[str] = UNSET
    """The username for this credential."""

    date_created: OptionalNullable[str] = UNSET
    """The date that this resource was created, given as GMT in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date that this resource was last updated, given as GMT in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format."""

    uri: OptionalNullable[str] = UNSET
    """The URI for this resource, relative to ``https://api.twilio.com``"""


class ApiV2010AccountSipSipCredentialListSipCredentialDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    credential_list_sid: NotRequired[str | None]
    username: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    uri: NotRequired[str | None]
