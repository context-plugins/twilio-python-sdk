from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersV1CreateEmbeddedSessionResponse(SdkBaseModel):
    id: str
    """Registration identifier (BU-prefixed)."""

    session_id: str = Field(alias="sessionId")
    """Session ID for the compliance embeddable."""

    session_token: str = Field(alias="sessionToken")
    """Ephemeral session token for the compliance embeddable."""


class NumbersV1CreateEmbeddedSessionResponseDict(TypedDict):
    id: str
    session_id: str
    session_token: str
