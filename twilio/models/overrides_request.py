from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.line_type import LineTypeOrStr


class OverridesRequest(SdkBaseModel):
    line_type: Optional[LineTypeOrStr] = UNSET
    """The new line type to override the original line type"""

    reason: Optional[str] = UNSET
    """The reason for the override"""


class OverridesRequestDict(TypedDict):
    line_type: NotRequired[LineTypeOrStr]
    reason: NotRequired[str]
