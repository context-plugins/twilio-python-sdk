from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.sender_id_purpose import SenderIdPurposeOrStr


class ValidateSenderId(SdkBaseModel):
    iso_country: str
    """ISO 3166-1 alpha-2 standard Country Code"""

    purpose: SenderIdPurposeOrStr
    """Purpose for using Sender ID"""

    sender_id: str
    """Sender ID string"""


class ValidateSenderIdDict(TypedDict):
    iso_country: str
    purpose: SenderIdPurposeOrStr
    sender_id: str
