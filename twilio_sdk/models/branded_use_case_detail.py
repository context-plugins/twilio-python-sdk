from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BrandedUseCaseDetail(SdkBaseModel):
    """Associated metrics for Branded calls grouped by each use case."""

    use_case: Optional[str] = UNSET
    """The name of supported use case for Branded calls."""

    enabled_phonenumbers: Optional[int] = UNSET
    """The number of phone numbers enabled Branded calls."""

    total_calls: Optional[int] = UNSET
    """The number of total outbound calls for the use case."""

    answer_rate: Optional[float] = UNSET
    """Answer rate per each use case for Branded bundled calls."""

    human_answer_rate: Optional[float] = UNSET
    """Rate of Branded bundled calls that were answered by Human per each use case for Branded bundled calls."""

    engagement_rate: Optional[float] = UNSET
    """Engagement Rate for Branded bundled calls where its call length is longer than 60 seconds per each use case for
    Branded bundled calls."""


class BrandedUseCaseDetailDict(TypedDict):
    use_case: NotRequired[str]
    enabled_phonenumbers: NotRequired[int]
    total_calls: NotRequired[int]
    answer_rate: NotRequired[float]
    human_answer_rate: NotRequired[float]
    engagement_rate: NotRequired[float]
