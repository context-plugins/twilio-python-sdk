from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LineTypeIntelligenceInfo(SdkBaseModel):
    mobile_country_code: Optional[str] = UNSET
    mobile_network_code: Optional[str] = UNSET
    carrier_name: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    error_code: Optional[int] = UNSET


class LineTypeIntelligenceInfoDict(TypedDict):
    mobile_country_code: NotRequired[str]
    mobile_network_code: NotRequired[str]
    carrier_name: NotRequired[str]
    type_: NotRequired[str]
    error_code: NotRequired[int]
