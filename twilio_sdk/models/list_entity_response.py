from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_service_entity import VerifyV2ServiceEntity, VerifyV2ServiceEntityDict


class ListEntityResponse(SdkBaseModel):
    entities: Optional[list[VerifyV2ServiceEntity]] = UNSET
    meta: Optional[Meta] = UNSET


class ListEntityResponseDict(TypedDict):
    entities: NotRequired[list[VerifyV2ServiceEntity | VerifyV2ServiceEntityDict]]
    meta: NotRequired[Meta | MetaDict]
