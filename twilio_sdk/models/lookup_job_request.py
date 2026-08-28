from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .job_thresholds import JobThresholds, JobThresholdsDict


class LookupJobRequest(SdkBaseModel):
    friendly_name: OptionalNullable[str] = UNSET
    description: OptionalNullable[str] = UNSET
    thresholds: Optional[JobThresholds] = UNSET


class LookupJobRequestDict(TypedDict):
    friendly_name: NotRequired[str | None]
    description: NotRequired[str | None]
    thresholds: NotRequired[JobThresholds | JobThresholdsDict]
