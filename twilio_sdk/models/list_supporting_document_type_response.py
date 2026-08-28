from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_supporting_document_type import (
    NumbersV2RegulatoryComplianceSupportingDocumentType,
    NumbersV2RegulatoryComplianceSupportingDocumentTypeDict,
)


class ListSupportingDocumentTypeResponse(SdkBaseModel):
    supporting_document_types: Optional[list[NumbersV2RegulatoryComplianceSupportingDocumentType]] = UNSET
    meta: Optional[Meta] = UNSET


class ListSupportingDocumentTypeResponseDict(TypedDict):
    supporting_document_types: NotRequired[
        list[
            (
                NumbersV2RegulatoryComplianceSupportingDocumentType
                | NumbersV2RegulatoryComplianceSupportingDocumentTypeDict
            )
        ]
    ]
    meta: NotRequired[Meta | MetaDict]
