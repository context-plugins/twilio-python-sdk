from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AnswerRate(SdkBaseModel):
    """Answer rate for each STIR/SHAKEN attestation category."""

    stsh_a: Optional[float] = UNSET
    """Answer rate for Stir Shaken category A."""

    stsh_b: Optional[float] = UNSET
    """Answer rate for Stir Shaken category B."""

    stsh_c: Optional[float] = UNSET
    """Answer rate for Stir Shaken category C."""


class AnswerRateDict(TypedDict):
    stsh_a: NotRequired[float]
    stsh_b: NotRequired[float]
    stsh_c: NotRequired[float]
