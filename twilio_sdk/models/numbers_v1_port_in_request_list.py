from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class NumbersV1PortInRequestList(SdkBaseModel):
    port_in_request_sid: Optional[str] = UNSET
    """The SID of the Port-in request"""

    port_in_request_status: OptionalNullable[str] = UNSET
    """Status of the Port In Request"""

    status_last_updated_timestamp: OptionalNullable[str] = UNSET
    """The last updated timestamp of the request"""

    phone_numbers_requested: OptionalNullable[int] = UNSET
    """Amount of phone numbers requested"""

    phone_numbers_ported: OptionalNullable[int] = UNSET
    """Amount of phone numbers ported"""

    suggested_action: OptionalNullable[str] = UNSET
    """Suggested action on this ticket"""


class NumbersV1PortInRequestListDict(TypedDict):
    port_in_request_sid: NotRequired[str]
    port_in_request_status: NotRequired[str | None]
    status_last_updated_timestamp: NotRequired[str | None]
    phone_numbers_requested: NotRequired[int | None]
    phone_numbers_ported: NotRequired[int | None]
    suggested_action: NotRequired[str | None]
