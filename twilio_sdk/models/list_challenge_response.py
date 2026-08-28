from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_service_entity_challenge import VerifyV2ServiceEntityChallenge, VerifyV2ServiceEntityChallengeDict


class ListChallengeResponse(SdkBaseModel):
    challenges: Optional[list[VerifyV2ServiceEntityChallenge]] = UNSET
    meta: Optional[Meta] = UNSET


class ListChallengeResponseDict(TypedDict):
    challenges: NotRequired[list[VerifyV2ServiceEntityChallenge | VerifyV2ServiceEntityChallengeDict]]
    meta: NotRequired[Meta | MetaDict]
