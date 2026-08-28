from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CaptureRule(SdkBaseModel):
    from_: str = Field(alias="from")
    """The from address. Use '*' for wildcard."""

    to: str
    """The to address. Use '*' for wildcard."""

    metadata: Optional[dict[str, str]] = UNSET


class CaptureRuleDict(TypedDict):
    from_: str
    to: str
    metadata: NotRequired[dict[str, str]]
