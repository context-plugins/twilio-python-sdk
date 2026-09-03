from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResumeInquiryResponse(SdkBaseModel):
    inquiry_id: str
    """Persona inquiry ID (existing or new)"""

    inquiry_session_token: str
    """Persona session token (always new, expires in 24 hours)"""

    bundle_sid: str
    """Bundle SID"""


class ResumeInquiryResponseDict(TypedDict):
    inquiry_id: str
    inquiry_session_token: str
    bundle_sid: str
