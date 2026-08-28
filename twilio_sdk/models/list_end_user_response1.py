from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_end_user import TrusthubV1EndUser, TrusthubV1EndUserDict


class ListEndUserResponse1(SdkBaseModel):
    results: Optional[list[TrusthubV1EndUser]] = UNSET
    meta: Optional[Meta] = UNSET


class ListEndUserResponse1Dict(TypedDict):
    results: NotRequired[list[TrusthubV1EndUser | TrusthubV1EndUserDict]]
    meta: NotRequired[Meta | MetaDict]
