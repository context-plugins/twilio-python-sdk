from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status4 import Status4OrStr


class FlexV2Instance(SdkBaseModel):
    flex_instance_sid: Optional[str] = UNSET
    account_sid: Optional[str] = UNSET
    status: Optional[Status4OrStr] = UNSET
    date_created: Optional[RFC3339DateTime] = UNSET
    date_updated: Optional[RFC3339DateTime] = UNSET


class FlexV2InstanceDict(TypedDict):
    flex_instance_sid: NotRequired[str]
    account_sid: NotRequired[str]
    status: NotRequired[Status4OrStr]
    date_created: NotRequired[RFC3339DateTime]
    date_updated: NotRequired[RFC3339DateTime]
