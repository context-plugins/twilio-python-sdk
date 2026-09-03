from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.original_line_type import OriginalLineTypeOrStr
from .enums.overridden_line_type import OverriddenLineTypeOrStr


class OverridesResponse(SdkBaseModel):
    phone_number: Optional[str] = UNSET
    """The phone number for which the override was created"""

    original_line_type: Optional[OriginalLineTypeOrStr] = UNSET
    """The original line type"""

    overridden_line_type: Optional[OverriddenLineTypeOrStr] = UNSET
    """The new line type after the override"""

    override_reason: Optional[str] = UNSET
    """The reason for the override"""

    override_timestamp: Optional[RFC3339DateTime] = UNSET
    overridden_by_account_sid: Optional[str] = UNSET
    """The Account SID for the user who made the override"""


class OverridesResponseDict(TypedDict):
    phone_number: NotRequired[str]
    original_line_type: NotRequired[OriginalLineTypeOrStr]
    overridden_line_type: NotRequired[OverriddenLineTypeOrStr]
    override_reason: NotRequired[str]
    override_timestamp: NotRequired[RFC3339DateTime]
    overridden_by_account_sid: NotRequired[str]
