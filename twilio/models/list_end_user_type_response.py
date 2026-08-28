from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .numbers_v2_regulatory_compliance_end_user_type import (
    NumbersV2RegulatoryComplianceEndUserType,
    NumbersV2RegulatoryComplianceEndUserTypeDict,
)


class ListEndUserTypeResponse(SdkBaseModel):
    end_user_types: Optional[list[NumbersV2RegulatoryComplianceEndUserType]] = UNSET
    meta: Optional[Meta] = UNSET


class ListEndUserTypeResponseDict(TypedDict):
    end_user_types: NotRequired[
        list[NumbersV2RegulatoryComplianceEndUserType | NumbersV2RegulatoryComplianceEndUserTypeDict]
    ]
    meta: NotRequired[Meta | MetaDict]
