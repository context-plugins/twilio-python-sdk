from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v2_outbound_phone_number_report import (
    InsightsV2OutboundPhoneNumberReport,
    InsightsV2OutboundPhoneNumberReportDict,
)
from .meta import Meta, MetaDict


class ListOutboundPhoneNumbersReports(SdkBaseModel):
    reports: Optional[list[InsightsV2OutboundPhoneNumberReport]] = UNSET
    meta: Optional[Meta] = UNSET


class ListOutboundPhoneNumbersReportsDict(TypedDict):
    reports: NotRequired[list[InsightsV2OutboundPhoneNumberReport | InsightsV2OutboundPhoneNumberReportDict]]
    meta: NotRequired[Meta | MetaDict]
