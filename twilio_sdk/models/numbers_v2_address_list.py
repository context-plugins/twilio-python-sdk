from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .numbers_v2_address import NumbersV2Address, NumbersV2AddressDict
from .paging import Paging, PagingDict


class NumbersV2AddressList(SdkBaseModel):
    addresses: Optional[list[NumbersV2Address]] = UNSET
    """List of address resources."""

    paging: Optional[Paging] = UNSET
    """Paging metadata for the list."""


class NumbersV2AddressListDict(TypedDict):
    addresses: NotRequired[list[NumbersV2Address | NumbersV2AddressDict]]
    paging: NotRequired[Paging | PagingDict]
