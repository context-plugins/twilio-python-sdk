from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersV1EmbeddedSession(SdkBaseModel):
    session_id: str = Field(alias="sessionId")
    """Session ID for the compliance embeddable."""

    session_token: str = Field(alias="sessionToken")
    """Ephemeral session token for the compliance embeddable."""


class NumbersV1EmbeddedSessionDict(TypedDict):
    session_id: str
    session_token: str
