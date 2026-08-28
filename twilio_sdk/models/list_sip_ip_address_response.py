from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address import (
    ApiV2010AccountSipSipIpAccessControlListSipIpAddress,
    ApiV2010AccountSipSipIpAccessControlListSipIpAddressDict,
)


class ListSipIpAddressResponse(SdkBaseModel):
    end: Optional[int] = UNSET
    first_page_uri: Optional[AnyUrl] = UNSET
    next_page_uri: OptionalNullable[AnyUrl] = UNSET
    page: Optional[int] = UNSET
    page_size: Optional[int] = UNSET
    previous_page_uri: OptionalNullable[AnyUrl] = UNSET
    start: Optional[int] = UNSET
    uri: Optional[AnyUrl] = UNSET
    ip_addresses: Optional[list[ApiV2010AccountSipSipIpAccessControlListSipIpAddress]] = UNSET


class ListSipIpAddressResponseDict(TypedDict):
    end: NotRequired[int]
    first_page_uri: NotRequired[AnyUrl]
    next_page_uri: NotRequired[AnyUrl | None]
    page: NotRequired[int]
    page_size: NotRequired[int]
    previous_page_uri: NotRequired[AnyUrl | None]
    start: NotRequired[int]
    uri: NotRequired[AnyUrl]
    ip_addresses: NotRequired[
        list[
            (
                ApiV2010AccountSipSipIpAccessControlListSipIpAddress
                | ApiV2010AccountSipSipIpAccessControlListSipIpAddressDict
            )
        ]
    ]
