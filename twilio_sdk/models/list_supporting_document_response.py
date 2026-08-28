from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_supporting_document import (
    NumbersV2RegulatoryComplianceSupportingDocument,
    NumbersV2RegulatoryComplianceSupportingDocumentDict,
)


class ListSupportingDocumentResponse(SdkBaseModel):
    results: Optional[list[NumbersV2RegulatoryComplianceSupportingDocument]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSupportingDocumentResponseDict(TypedDict):
    results: NotRequired[
        list[NumbersV2RegulatoryComplianceSupportingDocument | NumbersV2RegulatoryComplianceSupportingDocumentDict]
    ]
    meta: NotRequired[Meta | MetaDict]
