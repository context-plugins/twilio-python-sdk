from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountSipSipDomainSipIpAccessControlListMapping(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique id of the Account that is responsible for this resource."""

    date_created: OptionalNullable[str] = UNSET
    """The date that this resource was created, given as GMT in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date that this resource was last updated, given as GMT in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format."""

    domain_sid: OptionalNullable[str] = UNSET
    """The unique string that is created to identify the SipDomain resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human readable descriptive text for this resource, up to 64 characters long."""

    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    uri: OptionalNullable[str] = UNSET
    """The URI for this resource, relative to ``https://api.twilio.com``"""


class ApiV2010AccountSipSipDomainSipIpAccessControlListMappingDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    domain_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    sid: NotRequired[str | None]
    uri: NotRequired[str | None]
