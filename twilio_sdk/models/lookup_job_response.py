from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.job_status import JobStatusOrStr
from .job_result import JobResult, JobResultDict
from .job_thresholds import JobThresholds, JobThresholdsDict


class LookupJobResponse(SdkBaseModel):
    job_sid: Optional[str] = UNSET
    friendly_name: OptionalNullable[str] = UNSET
    description: OptionalNullable[str] = UNSET
    status: Optional[JobStatusOrStr] = UNSET
    thresholds: Optional[JobThresholds] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    completed_at: OptionalNullable[RFC3339DateTime] = UNSET
    result: Optional[JobResult] = UNSET
    twilio_error_code: OptionalNullable[int] = UNSET


class LookupJobResponseDict(TypedDict):
    job_sid: NotRequired[str]
    friendly_name: NotRequired[str | None]
    description: NotRequired[str | None]
    status: NotRequired[JobStatusOrStr]
    thresholds: NotRequired[JobThresholds | JobThresholdsDict]
    created_at: NotRequired[RFC3339DateTime]
    completed_at: NotRequired[RFC3339DateTime | None]
    result: NotRequired[JobResult | JobResultDict]
    twilio_error_code: NotRequired[int | None]
