from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_hosted_number_order import NumbersV2HostedNumberOrder, NumbersV2HostedNumberOrderDict


class ListHostedNumberOrderResponse(SdkBaseModel):
    items: Optional[list[NumbersV2HostedNumberOrder]] = UNSET
    meta: Optional[Meta] = UNSET


class ListHostedNumberOrderResponseDict(TypedDict):
    items: NotRequired[list[NumbersV2HostedNumberOrder | NumbersV2HostedNumberOrderDict]]
    meta: NotRequired[Meta | MetaDict]
