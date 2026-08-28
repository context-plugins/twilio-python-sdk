from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sender_id_purpose import SenderIdPurposeOrStr
from .enums.status2 import Status2OrStr


class SenderIdRegistration(SdkBaseModel):
    application_sid: str
    """Sender ID Registration Application SID"""

    account_sid: str
    """Owning Account SID of the Sender ID"""

    status: Status2OrStr
    """Status of the Sender ID Registration Application"""

    registration_info: list[Any]
    """List of Sender ID Registration information"""

    purpose: Optional[SenderIdPurposeOrStr] = UNSET
    """Purpose for using Sender ID"""

    company_subsidiary: Optional[bool] = UNSET
    """Whether registering on behalf of subsidiary"""

    emails_for_notification: list[str]
    """List of emails to send Sender ID Application updates"""


class SenderIdRegistrationDict(TypedDict):
    application_sid: str
    account_sid: str
    status: Status2OrStr
    registration_info: list[Any]
    purpose: NotRequired[SenderIdPurposeOrStr]
    company_subsidiary: NotRequired[bool]
    emails_for_notification: list[str]
