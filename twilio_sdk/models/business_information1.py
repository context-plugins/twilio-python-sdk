from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BusinessInformation1(SdkBaseModel):
    """Business information associated with the application."""

    managing_company_profile: Optional[str] = UNSET
    customer_facing_profile: Optional[str] = UNSET
    business_website: Optional[str] = UNSET
    ein_managing_company_profile: Optional[str] = UNSET
    ein_customer_facing_profile: Optional[str] = UNSET


class BusinessInformation1Dict(TypedDict):
    managing_company_profile: NotRequired[str]
    customer_facing_profile: NotRequired[str]
    business_website: NotRequired[str]
    ein_managing_company_profile: NotRequired[str]
    ein_customer_facing_profile: NotRequired[str]
