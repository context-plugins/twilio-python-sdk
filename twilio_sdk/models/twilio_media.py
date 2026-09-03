from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TwilioMedia(SdkBaseModel):
    """twilio/media is used to send file attachments, or to send long text via MMS in the US and Canada. As such, the
    twilio/media type must contain at least ONE of text or media content."""

    body: Optional[str] = UNSET
    media: list[str]


class TwilioMediaDict(TypedDict):
    body: NotRequired[str]
    media: list[str]
