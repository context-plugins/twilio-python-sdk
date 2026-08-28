from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v2_rcs_compliance_country_response import (
    MessagingV2RcsComplianceCountryResponse,
    MessagingV2RcsComplianceCountryResponseDict,
)


class MessagingV2RcsComplianceResponse(SdkBaseModel):
    """The KYC compliance information. This section consists of response to the request launch."""

    registration_sid: str
    """The default compliance registration SID (e.g., from CR-Google) that applies to all countries unless overridden in
    the ``countries`` array."""

    countries: Optional[list[MessagingV2RcsComplianceCountryResponse]] = UNSET
    """A list of country-specific compliance details."""


class MessagingV2RcsComplianceResponseDict(TypedDict):
    registration_sid: str
    countries: NotRequired[list[MessagingV2RcsComplianceCountryResponse | MessagingV2RcsComplianceCountryResponseDict]]
