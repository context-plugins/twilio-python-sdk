from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ApiV2010AccountSipSipIpAccessControlListSipIpAddress(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """A 34 character string that uniquely identifies this resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The unique id of the Account that is responsible for this resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human readable descriptive text for this resource, up to 255 characters long."""

    ip_address: OptionalNullable[str] = UNSET
    """An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP
    address will be allowed by Twilio. IPv4 only supported today."""

    cidr_prefix_length: Optional[int] = UNSET
    """An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By
    default the entire IP address is used."""

    ip_access_control_list_sid: OptionalNullable[str] = UNSET
    """The unique id of the IpAccessControlList resource that includes this resource."""

    date_created: OptionalNullable[str] = UNSET
    """The date that this resource was created, given as GMT in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format."""

    date_updated: OptionalNullable[str] = UNSET
    """The date that this resource was last updated, given as GMT in `RFC 2822
    <https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822>`__ format."""

    uri: OptionalNullable[str] = UNSET
    """The URI for this resource, relative to ``https://api.twilio.com``"""


class ApiV2010AccountSipSipIpAccessControlListSipIpAddressDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    ip_address: NotRequired[str | None]
    cidr_prefix_length: NotRequired[int]
    ip_access_control_list_sid: NotRequired[str | None]
    date_created: NotRequired[str | None]
    date_updated: NotRequired[str | None]
    uri: NotRequired[str | None]
