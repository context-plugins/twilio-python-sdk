from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_bundle_evaluation import (
    NumbersV2RegulatoryComplianceBundleEvaluation,
    NumbersV2RegulatoryComplianceBundleEvaluationDict,
)


class ListEvaluationResponse(SdkBaseModel):
    results: Optional[list[NumbersV2RegulatoryComplianceBundleEvaluation]] = UNSET
    meta: Optional[Meta] = UNSET


class ListEvaluationResponseDict(TypedDict):
    results: NotRequired[
        list[NumbersV2RegulatoryComplianceBundleEvaluation | NumbersV2RegulatoryComplianceBundleEvaluationDict]
    ]
    meta: NotRequired[Meta | MetaDict]
