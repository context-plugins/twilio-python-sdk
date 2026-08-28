from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NumbersV1CreateEmbeddedSessionRequest(SdkBaseModel):
    theme_set_id: Optional[str] = Field(default=UNSET, alias="themeSetId")
    """Theme ID for the Compliance Embeddable UI. Overrides the theme set during registration creation."""


class NumbersV1CreateEmbeddedSessionRequestDict(TypedDict):
    theme_set_id: NotRequired[str]
