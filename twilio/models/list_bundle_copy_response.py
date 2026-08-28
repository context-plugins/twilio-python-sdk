from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_bundle_bundle_copy import (
    NumbersV2RegulatoryComplianceBundleBundleCopy,
    NumbersV2RegulatoryComplianceBundleBundleCopyDict,
)


class ListBundleCopyResponse(SdkBaseModel):
    results: Optional[list[NumbersV2RegulatoryComplianceBundleBundleCopy]] = UNSET
    meta: Optional[Meta] = UNSET


class ListBundleCopyResponseDict(TypedDict):
    results: NotRequired[
        list[NumbersV2RegulatoryComplianceBundleBundleCopy | NumbersV2RegulatoryComplianceBundleBundleCopyDict]
    ]
    meta: NotRequired[Meta | MetaDict]
