from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_end_user import (
    NumbersV2RegulatoryComplianceEndUser,
    NumbersV2RegulatoryComplianceEndUserDict,
)


class ListEndUserResponse(SdkBaseModel):
    results: Optional[list[NumbersV2RegulatoryComplianceEndUser]] = UNSET
    meta: Optional[Meta] = UNSET


class ListEndUserResponseDict(TypedDict):
    results: NotRequired[list[NumbersV2RegulatoryComplianceEndUser | NumbersV2RegulatoryComplianceEndUserDict]]
    meta: NotRequired[Meta | MetaDict]
