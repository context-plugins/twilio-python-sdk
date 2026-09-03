from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .voice_integrity_calls_per_bundle import VoiceIntegrityCallsPerBundle, VoiceIntegrityCallsPerBundleDict


class VoiceIntegrity(SdkBaseModel):
    """Metrics related to Voice Integrity enabled calls for the report period."""

    enabled_calls: Optional[int] = UNSET
    """Total number of calls with Voice Integrity enabled."""

    enabled_percentage: Optional[float] = UNSET
    """Percentage of calls with Voice Integrity enabled."""

    calls_per_bundle: Optional[list[VoiceIntegrityCallsPerBundle]] = UNSET
    """Number of calls per Voice Integrity enabled Bundle Sid."""


class VoiceIntegrityDict(TypedDict):
    enabled_calls: NotRequired[int]
    enabled_percentage: NotRequired[float]
    calls_per_bundle: NotRequired[list[VoiceIntegrityCallsPerBundle | VoiceIntegrityCallsPerBundleDict]]
