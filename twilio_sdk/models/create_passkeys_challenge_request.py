from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreatePasskeysChallengeRequest(SdkBaseModel):
    identity: Optional[str] = UNSET
    factor_sid: Optional[str] = UNSET


class CreatePasskeysChallengeRequestDict(TypedDict):
    identity: NotRequired[str]
    factor_sid: NotRequired[str]
