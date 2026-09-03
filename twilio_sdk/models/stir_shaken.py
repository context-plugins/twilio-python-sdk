from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .answer_rate import AnswerRate, AnswerRateDict
from .call_count import CallCount, CallCountDict
from .percentage import Percentage, PercentageDict


class StirShaken(SdkBaseModel):
    """Metrics related to STIR/SHAKEN attestation A, B, and C for the report period."""

    call_count: Optional[CallCount] = UNSET
    """Total number of calls for each STIR/SHAKEN attestation category."""

    percentage: Optional[Percentage] = UNSET
    """Percentage of calls for each STIR/SHAKEN attestation category."""

    answer_rate: Optional[AnswerRate] = UNSET
    """Answer rate for each STIR/SHAKEN attestation category."""


class StirShakenDict(TypedDict):
    call_count: NotRequired[CallCount | CallCountDict]
    percentage: NotRequired[Percentage | PercentageDict]
    answer_rate: NotRequired[AnswerRate | AnswerRateDict]
