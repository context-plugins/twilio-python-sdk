from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .meta import Meta, MetaDict
from .verify_v2_verification_template import VerifyV2VerificationTemplate, VerifyV2VerificationTemplateDict


class ListVerificationTemplateResponse(SdkBaseModel):
    templates: Optional[list[VerifyV2VerificationTemplate]] = UNSET
    meta: Optional[Meta] = UNSET


class ListVerificationTemplateResponseDict(TypedDict):
    templates: NotRequired[list[VerifyV2VerificationTemplate | VerifyV2VerificationTemplateDict]]
    meta: NotRequired[Meta | MetaDict]
