from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VoiceIntegrityCallsPerBundle(SdkBaseModel):
    bundle_sid: Optional[str] = UNSET
    """Voice Integrity Approved Profile Sid."""

    enabled_phonenumbers: Optional[int] = UNSET
    """The number of Voice Integrity enabled and registered phone numbers per Bundle Sid."""

    total_calls: Optional[int] = UNSET
    """The number of outbound calls on Voice Integrity enabled and registered number per Bundle Sid."""

    answer_rate: Optional[float] = UNSET
    """Answer rate for calls on Voice Integrity enabled and registered number per Bundle Sid."""

    human_answer_rate: Optional[float] = UNSET
    """Rate for calls on Voice Integrity enabled and registered number per Bundle Sid that were answered by Human per
    each use case for Branded bundled calls."""


class VoiceIntegrityCallsPerBundleDict(TypedDict):
    bundle_sid: NotRequired[str]
    enabled_phonenumbers: NotRequired[int]
    total_calls: NotRequired[int]
    answer_rate: NotRequired[float]
    human_answer_rate: NotRequired[float]
