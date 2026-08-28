from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status1 import Status1OrStr


class StatusOverrideInfo(SdkBaseModel):
    """The override status of the country for the sender Id"""

    status: Optional[Status1OrStr] = UNSET


class StatusOverrideInfoDict(TypedDict):
    status: NotRequired[Status1OrStr]
