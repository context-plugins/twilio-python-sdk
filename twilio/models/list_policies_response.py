from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .trusthub_v1_policies import TrusthubV1Policies, TrusthubV1PoliciesDict


class ListPoliciesResponse(SdkBaseModel):
    results: Optional[list[TrusthubV1Policies]] = UNSET
    meta: Optional[Meta] = UNSET


class ListPoliciesResponseDict(TypedDict):
    results: NotRequired[list[TrusthubV1Policies | TrusthubV1PoliciesDict]]
    meta: NotRequired[Meta | MetaDict]
