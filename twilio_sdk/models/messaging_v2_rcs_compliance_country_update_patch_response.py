from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.messaging_v2_rcs_country_status import MessagingV2RcsCountryStatusOrStr


class MessagingV2RcsComplianceCountryUpdatePatchResponse(SdkBaseModel):
    country: str
    """The ISO 3166-1 alpha-2 country code."""

    registration_sid: Optional[str] = UNSET
    """The default compliance registration SID (e.g., from CR-Google) that applies to all countries unless overridden in
    the ``countries`` array."""

    status: Optional[MessagingV2RcsCountryStatusOrStr] = UNSET
    """The country-level status. Based on the aggregation of the carrier-level status."""


class MessagingV2RcsComplianceCountryUpdatePatchResponseDict(TypedDict):
    country: str
    registration_sid: NotRequired[str]
    status: NotRequired[MessagingV2RcsCountryStatusOrStr]
