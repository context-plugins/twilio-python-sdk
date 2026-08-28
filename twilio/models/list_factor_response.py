from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_service_entity_factor import VerifyV2ServiceEntityFactor, VerifyV2ServiceEntityFactorDict


class ListFactorResponse(SdkBaseModel):
    factors: Optional[list[VerifyV2ServiceEntityFactor]] = UNSET
    meta: Optional[Meta] = UNSET


class ListFactorResponseDict(TypedDict):
    factors: NotRequired[list[VerifyV2ServiceEntityFactor | VerifyV2ServiceEntityFactorDict]]
    meta: NotRequired[Meta | MetaDict]
