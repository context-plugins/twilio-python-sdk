from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.sender_id_purpose import SenderIdPurposeOrStr
from .sender_id_validation_failure import SenderIdValidationFailure, SenderIdValidationFailureDict


class SenderIdValidationResult(SdkBaseModel):
    iso_country: str
    """ISO 3166-1 alpha-2 standard Country Code"""

    purpose: SenderIdPurposeOrStr
    """Purpose for using Sender ID"""

    sender_id: str
    """Sender ID string"""

    failures: list[SenderIdValidationFailure]
    """List of failures during the validation"""


class SenderIdValidationResultDict(TypedDict):
    iso_country: str
    purpose: SenderIdPurposeOrStr
    sender_id: str
    failures: list[SenderIdValidationFailure | SenderIdValidationFailureDict]
