from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PhoneNumberReportFilter(SdkBaseModel):
    key: Optional[str] = UNSET
    """The name of the filter"""

    values: Optional[list[str]] = UNSET
    """List of supported filter values for the field name"""


class PhoneNumberReportFilterDict(TypedDict):
    key: NotRequired[str]
    values: NotRequired[list[str]]
