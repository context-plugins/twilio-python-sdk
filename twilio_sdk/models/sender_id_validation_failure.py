from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SenderIdValidationFailure(SdkBaseModel):
    error_code: int
    """Associated error code with validation failure"""

    reason: str
    """Friendly description of error for validation failure"""


class SenderIdValidationFailureDict(TypedDict):
    error_code: int
    reason: str
