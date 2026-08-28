from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .branded_calling import BrandedCalling, BrandedCallingDict
from .county_carrier_value import CountyCarrierValue, CountyCarrierValueDict
from .stir_shaken import StirShaken, StirShakenDict
from .voice_integrity import VoiceIntegrity, VoiceIntegrityDict


class OutboundCarrierCalling(SdkBaseModel):
    """KYT metrics for outbound carrier calling."""

    unique_calling_numbers: Optional[int] = UNSET
    """Number of unique PSTN calling numbers to non-Twilio numbers during the report period."""

    unique_called_numbers: Optional[int] = UNSET
    """Number of unique non-Twilio PSTN called numbers during the report period."""

    blocked_calls_by_carrier: Optional[list[CountyCarrierValue]] = UNSET
    """Percentage of blocked calls by carrier per country."""

    short_duration_calls_percentage: Optional[float] = UNSET
    """Percentage of completed outbound calls under 10 seconds (PSTN Short call tags); More than 15% is typically low
    trust measured."""

    long_duration_calls_percentage: Optional[float] = UNSET
    """Percentage of long duration calls ( >= 60 seconds)"""

    potential_robocalls_percentage: Optional[float] = UNSET
    """Percentage of completed outbound calls to unassigned or unallocated phone numbers."""

    branded_calling: Optional[BrandedCalling] = UNSET
    """Metrics related to Branded Calling bundled calls including CTIA for the report period."""

    voice_integrity: Optional[VoiceIntegrity] = UNSET
    """Metrics related to Voice Integrity enabled calls for the report period."""

    stir_shaken: Optional[StirShaken] = UNSET
    """Metrics related to STIR/SHAKEN attestation A, B, and C for the report period."""


class OutboundCarrierCallingDict(TypedDict):
    unique_calling_numbers: NotRequired[int]
    unique_called_numbers: NotRequired[int]
    blocked_calls_by_carrier: NotRequired[list[CountyCarrierValue | CountyCarrierValueDict]]
    short_duration_calls_percentage: NotRequired[float]
    long_duration_calls_percentage: NotRequired[float]
    potential_robocalls_percentage: NotRequired[float]
    branded_calling: NotRequired[BrandedCalling | BrandedCallingDict]
    voice_integrity: NotRequired[VoiceIntegrity | VoiceIntegrityDict]
    stir_shaken: NotRequired[StirShaken | StirShakenDict]
