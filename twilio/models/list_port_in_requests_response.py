from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .numbers_v1_port_in_request_list import NumbersV1PortInRequestList, NumbersV1PortInRequestListDict
from .numbers_v1_port_in_request_list_meta import NumbersV1PortInRequestListMeta, NumbersV1PortInRequestListMetaDict


class ListPortInRequestsResponse(SdkBaseModel):
    port_in_requests: Optional[list[NumbersV1PortInRequestList]] = UNSET
    meta: Optional[NumbersV1PortInRequestListMeta] = UNSET


class ListPortInRequestsResponseDict(TypedDict):
    port_in_requests: NotRequired[list[NumbersV1PortInRequestList | NumbersV1PortInRequestListDict]]
    meta: NotRequired[NumbersV1PortInRequestListMeta | NumbersV1PortInRequestListMetaDict]
