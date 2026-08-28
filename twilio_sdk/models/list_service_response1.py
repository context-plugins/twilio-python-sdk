from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_service import VerifyV2Service, VerifyV2ServiceDict


class ListServiceResponse1(SdkBaseModel):
    services: Optional[list[VerifyV2Service]] = UNSET
    meta: Optional[Meta] = UNSET


class ListServiceResponse1Dict(TypedDict):
    services: NotRequired[list[VerifyV2Service | VerifyV2ServiceDict]]
    meta: NotRequired[Meta | MetaDict]
