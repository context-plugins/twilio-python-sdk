from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.business_identity import BusinessIdentityOrStr
from .enums.message_purpose import MessagePurposeOrStr


class CreateRegistrationRequest(SdkBaseModel):
    global_hq_country: str
    """Global HQ country code (ISO 3166-1 alpha-2)"""

    target_country: str
    """Target country for sender ID registration"""

    message_purpose: MessagePurposeOrStr
    """Purpose of SMS messages"""

    sender_id: str
    """Requested alphanumeric sender ID value"""

    business_identity: BusinessIdentityOrStr
    """Business customer type"""

    is_subassigned: bool
    """Whether sender ID will be subassigned to other accounts"""

    friendly_name: str
    """Human-readable name for the registration"""

    customer_profile_bundle_sid: str
    """Bundle SID of customer's profile"""

    isv_opt_in_consent: Optional[bool] = UNSET
    """ISV opt-in consent flag. Defaults to true if not provided. Only rejected when explicitly set to false for ISV
    customers registering in Australia."""


class CreateRegistrationRequestDict(TypedDict):
    global_hq_country: str
    target_country: str
    message_purpose: MessagePurposeOrStr
    sender_id: str
    business_identity: BusinessIdentityOrStr
    is_subassigned: bool
    friendly_name: str
    customer_profile_bundle_sid: str
    isv_opt_in_consent: NotRequired[bool]
