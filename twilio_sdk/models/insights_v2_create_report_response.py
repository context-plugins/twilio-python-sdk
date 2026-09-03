from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.report_status import ReportStatusOrStr
from .report_metadata import ReportMetadata, ReportMetadataDict


class InsightsV2CreateReportResponse(SdkBaseModel):
    account_sid: Optional[str] = UNSET
    """The unique SID identifier of the Account."""

    report_id: Optional[str] = UNSET
    """The report identifier as Voice Insights Report TTID."""

    status: Optional[ReportStatusOrStr] = UNSET
    """The status of the report."""

    request_meta: Optional[ReportMetadata] = UNSET
    url: OptionalNullable[str] = UNSET
    """The URL of this resource."""


class InsightsV2CreateReportResponseDict(TypedDict):
    account_sid: NotRequired[str]
    report_id: NotRequired[str]
    status: NotRequired[ReportStatusOrStr]
    request_meta: NotRequired[ReportMetadata | ReportMetadataDict]
    url: NotRequired[str | None]
