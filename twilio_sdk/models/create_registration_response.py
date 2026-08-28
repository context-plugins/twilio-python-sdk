from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateRegistrationResponse(SdkBaseModel):
    bundle_sid: str
    """Bundle SID (same as bundle_sid in KYC Orchestration)"""

    inquiry_id: str
    """Persona inquiry ID"""

    inquiry_session_token: str
    """Persona session token for embedding Persona UI"""


class CreateRegistrationResponseDict(TypedDict):
    bundle_sid: str
    inquiry_id: str
    inquiry_session_token: str
