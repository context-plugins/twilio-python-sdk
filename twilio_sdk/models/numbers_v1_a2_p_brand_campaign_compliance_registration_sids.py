from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class NumbersV1A2PBrandCampaignComplianceRegistrationSids(SdkBaseModel):
    campaign_compliance_registration_sid: OptionalNullable[str] = Field(
        default=UNSET, alias="campaignComplianceRegistrationSid"
    )
    """Sid associated with campaign compliance registration"""

    brand_compliance_registration_sid: OptionalNullable[str] = Field(
        default=UNSET, alias="brandComplianceRegistrationSid"
    )
    """Sid associated with brand compliance registration"""


class NumbersV1A2PBrandCampaignComplianceRegistrationSidsDict(TypedDict):
    campaign_compliance_registration_sid: NotRequired[str | None]
    brand_compliance_registration_sid: NotRequired[str | None]
