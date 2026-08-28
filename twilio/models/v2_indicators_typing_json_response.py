from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V2IndicatorsTypingJsonResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    """Indicates if the typing indicator was sent successfully."""


class V2IndicatorsTypingJsonResponseDict(TypedDict):
    success: NotRequired[bool]
