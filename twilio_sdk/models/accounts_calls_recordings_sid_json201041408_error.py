from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountsCallsRecordingsSidJson201041408Error(SdkBaseModel):
    code: Optional[int] = UNSET
    """Twilio-specific error code"""

    message: Optional[str] = UNSET
    """Error message"""

    more_info: Optional[str] = UNSET
    """Link to Error Code References"""

    status: Optional[int] = UNSET
    """HTTP response status code"""


class AccountsCallsRecordingsSidJson201041408ErrorDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    more_info: NotRequired[str]
    status: NotRequired[int]
