from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.new_status import NewStatusOrStr
from .port_in_phone_number_request import PortInPhoneNumberRequest, PortInPhoneNumberRequestDict


class NumbersV1PortingBulkUpdateStatusRequest(SdkBaseModel):
    new_status: NewStatusOrStr
    """The new status to set for the port in request."""

    port_in_phone_number_requests: list[PortInPhoneNumberRequest]


class NumbersV1PortingBulkUpdateStatusRequestDict(TypedDict):
    new_status: NewStatusOrStr
    port_in_phone_number_requests: list[PortInPhoneNumberRequest | PortInPhoneNumberRequestDict]
