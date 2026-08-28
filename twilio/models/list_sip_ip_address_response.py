from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address import (
    ApiV2010AccountSipSipIpAccessControlListSipIpAddress,
    ApiV2010AccountSipSipIpAccessControlListSipIpAddressDict,
)


class ListSipIpAddressResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[str] = UNSET
    next_page_uri: OptionalNullable[str] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[str] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[str] = UNSET
    ip_addresses: Optional[list[ApiV2010AccountSipSipIpAccessControlListSipIpAddress]] = UNSET


class ListSipIpAddressResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[str]
    next_page_uri: NotRequired[str | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[str | None]
    start: NotRequired[int]
    uri: NotRequired[str]
    ip_addresses: NotRequired[
        list[
            (
                ApiV2010AccountSipSipIpAccessControlListSipIpAddress
                | ApiV2010AccountSipSipIpAccessControlListSipIpAddressDict
            )
        ]
    ]
