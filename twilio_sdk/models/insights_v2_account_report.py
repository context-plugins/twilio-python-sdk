from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .account_report import AccountReport, AccountReportDict
from .enums.report_status import ReportStatusOrStr
from .report_metadata import ReportMetadata, ReportMetadataDict


class InsightsV2AccountReport(SdkBaseModel):
    account_sid: Optional[str] = UNSET
    """The unique SID identifier of the Account."""

    report_id: Optional[str] = UNSET
    """The account level report identifier as Voice Insights Report TTID."""

    status: Optional[ReportStatusOrStr] = UNSET
    """The status of the report."""

    request_meta: Optional[ReportMetadata] = UNSET
    report: Optional[AccountReport] = UNSET
    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""


class InsightsV2AccountReportDict(TypedDict):
    account_sid: NotRequired[str]
    report_id: NotRequired[str]
    status: NotRequired[ReportStatusOrStr]
    request_meta: NotRequired[ReportMetadata | ReportMetadataDict]
    report: NotRequired[AccountReport | AccountReportDict]
    url: NotRequired[AnyUrl | None]
