from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .branded_use_case_detail import BrandedUseCaseDetail, BrandedUseCaseDetailDict


class BrandedCalling(SdkBaseModel):
    """Metrics related to Branded Calling bundled calls including CTIA for the report period."""

    total_branded_calls: Optional[int] = UNSET
    """Total number of Branded bundled calls."""

    percent_branded_calls: Optional[float] = UNSET
    """Percentage of Branded bundled calls over total outbound calls."""

    answer_rate: Optional[float] = UNSET
    """Answer rate for Branded bundled calls."""

    human_answer_rate: Optional[float] = UNSET
    """Rate of Branded bundled calls that were answered by Human."""

    engagement_rate: Optional[float] = UNSET
    """Engagement Rate for Branded bundled calls where its call length is longer than 60 seconds."""

    by_use_case: Optional[list[BrandedUseCaseDetail]] = UNSET
    """Details of branded calls by use case."""


class BrandedCallingDict(TypedDict):
    total_branded_calls: NotRequired[int]
    percent_branded_calls: NotRequired[float]
    answer_rate: NotRequired[float]
    human_answer_rate: NotRequired[float]
    engagement_rate: NotRequired[float]
    by_use_case: NotRequired[list[BrandedUseCaseDetail | BrandedUseCaseDetailDict]]
