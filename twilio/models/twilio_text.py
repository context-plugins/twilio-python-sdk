from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TwilioText(SdkBaseModel):
    """Type containing only plain text-based content"""

    body: str


class TwilioTextDict(TypedDict):
    body: str
