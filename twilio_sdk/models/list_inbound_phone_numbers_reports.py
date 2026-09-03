from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insights_v2_inbound_phone_number_report import (
    InsightsV2InboundPhoneNumberReport,
    InsightsV2InboundPhoneNumberReportDict,
)
from .meta import Meta, MetaDict


class ListInboundPhoneNumbersReports(SdkBaseModel):
    reports: Optional[list[InsightsV2InboundPhoneNumberReport]] = UNSET
    meta: Optional[Meta] = UNSET


class ListInboundPhoneNumbersReportsDict(TypedDict):
    reports: NotRequired[list[InsightsV2InboundPhoneNumberReport | InsightsV2InboundPhoneNumberReportDict]]
    meta: NotRequired[Meta | MetaDict]
