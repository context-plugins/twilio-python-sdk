from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sender_id_purpose import SenderIdPurposeOrStr


class CreateSenderIdRegistration(SdkBaseModel):
    iso_countries: Optional[list[str]] = UNSET
    """List of Iso countries"""

    company_subsidiary: bool
    """Whether registering on behalf of subsidiary"""

    business_profile_sid: Optional[str] = UNSET
    """Business profile Bundle sid used for the application"""

    identity_sid: Optional[str] = UNSET
    """Identity sid used for the application. It must be of IdentityType 'sender_id_customer_profile'"""

    address_sid: Optional[str] = UNSET
    """Address sid used for the application"""

    purpose: SenderIdPurposeOrStr
    """Purpose for using Sender ID"""


class CreateSenderIdRegistrationDict(TypedDict):
    iso_countries: NotRequired[list[str]]
    company_subsidiary: bool
    business_profile_sid: NotRequired[str]
    identity_sid: NotRequired[str]
    address_sid: NotRequired[str]
    purpose: SenderIdPurposeOrStr
