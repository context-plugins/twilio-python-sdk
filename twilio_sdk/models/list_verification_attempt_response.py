from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_verification_attempt import VerifyV2VerificationAttempt, VerifyV2VerificationAttemptDict


class ListVerificationAttemptResponse(SdkBaseModel):
    attempts: Optional[list[VerifyV2VerificationAttempt]] = UNSET
    meta: Optional[Meta] = UNSET


class ListVerificationAttemptResponseDict(TypedDict):
    attempts: NotRequired[list[VerifyV2VerificationAttempt | VerifyV2VerificationAttemptDict]]
    meta: NotRequired[Meta | MetaDict]
