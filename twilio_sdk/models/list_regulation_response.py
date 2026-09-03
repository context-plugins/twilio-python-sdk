from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_regulation import (
    NumbersV2RegulatoryComplianceRegulation,
    NumbersV2RegulatoryComplianceRegulationDict,
)


class ListRegulationResponse(SdkBaseModel):
    results: Optional[list[NumbersV2RegulatoryComplianceRegulation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListRegulationResponseDict(TypedDict):
    results: NotRequired[list[NumbersV2RegulatoryComplianceRegulation | NumbersV2RegulatoryComplianceRegulationDict]]
    meta: NotRequired[Meta | MetaDict]
