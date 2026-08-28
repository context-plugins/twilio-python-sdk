from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class VerifyV2VerificationAttemptsSummary(SdkBaseModel):
    total_attempts: Optional[int] = UNSET
    """Total of attempts made according to the provided filters"""

    total_converted: Optional[int] = UNSET
    """Total of attempts made that were confirmed by the end user, according to the provided filters."""

    total_unconverted: Optional[int] = UNSET
    """Total of attempts made that were not confirmed by the end user, according to the provided filters."""

    conversion_rate_percentage: OptionalNullable[str] = UNSET
    """Percentage of the confirmed messages over the total, defined by (total_converted/total_attempts)*100."""

    url: OptionalNullable[AnyUrl] = UNSET


class VerifyV2VerificationAttemptsSummaryDict(TypedDict):
    total_attempts: NotRequired[int]
    total_converted: NotRequired[int]
    total_unconverted: NotRequired[int]
    conversion_rate_percentage: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
