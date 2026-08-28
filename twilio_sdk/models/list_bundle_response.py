from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_bundle import (
    NumbersV2RegulatoryComplianceBundle,
    NumbersV2RegulatoryComplianceBundleDict,
)


class ListBundleResponse(SdkBaseModel):
    results: Optional[list[NumbersV2RegulatoryComplianceBundle]] = UNSET
    meta: Optional[Meta] = UNSET


class ListBundleResponseDict(TypedDict):
    results: NotRequired[list[NumbersV2RegulatoryComplianceBundle | NumbersV2RegulatoryComplianceBundleDict]]
    meta: NotRequired[Meta | MetaDict]
