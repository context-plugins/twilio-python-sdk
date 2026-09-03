from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .messaging_v1_tollfree_verification import MessagingV1TollfreeVerification, MessagingV1TollfreeVerificationDict
from .meta import Meta, MetaDict


class ListTollfreeVerificationResponse(SdkBaseModel):
    verifications: Optional[list[MessagingV1TollfreeVerification]] = UNSET
    meta: Optional[Meta] = UNSET


class ListTollfreeVerificationResponseDict(TypedDict):
    verifications: NotRequired[list[MessagingV1TollfreeVerification | MessagingV1TollfreeVerificationDict]]
    meta: NotRequired[Meta | MetaDict]
