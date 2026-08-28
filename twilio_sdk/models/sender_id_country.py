from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status import StatusOrStr
from .status_override_info import StatusOverrideInfo, StatusOverrideInfoDict


class SenderIdCountry(SdkBaseModel):
    routing_table_sid: str
    """The unique identifier of the Sender ID Country."""

    iso_country: str
    """The ISO country code."""

    date_created: RFC3339DateTime
    """The date and time when the country routing table was created."""

    date_updated: RFC3339DateTime
    """The date and time when the country routing table was last updated."""

    default: bool
    """Indicates if this is the default routing table for the country."""

    status: StatusOrStr
    """The status of the country for the sender Id"""

    status_override_info: Optional[StatusOverrideInfo] = UNSET
    """The override status of the country for the sender Id"""


class SenderIdCountryDict(TypedDict):
    routing_table_sid: str
    iso_country: str
    date_created: RFC3339DateTime
    date_updated: RFC3339DateTime
    default: bool
    status: StatusOrStr
    status_override_info: NotRequired[StatusOverrideInfo | StatusOverrideInfoDict]
