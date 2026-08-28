from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_bundle_item_assignment import (
    NumbersV2RegulatoryComplianceBundleItemAssignment,
    NumbersV2RegulatoryComplianceBundleItemAssignmentDict,
)


class ListItemAssignmentResponse(SdkBaseModel):
    results: Optional[list[NumbersV2RegulatoryComplianceBundleItemAssignment]] = UNSET
    meta: Optional[Meta] = UNSET


class ListItemAssignmentResponseDict(TypedDict):
    results: NotRequired[
        list[NumbersV2RegulatoryComplianceBundleItemAssignment | NumbersV2RegulatoryComplianceBundleItemAssignmentDict]
    ]
    meta: NotRequired[Meta | MetaDict]
