from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConversationsV2CaptureRule(SdkBaseModel):
    """Defines a capture rule with from and to addresses. Supports wildcard ``*`` for omnidirectional matching."""

    from_: str = Field(alias="from")
    """The from address. Use ``*`` for wildcard to match any from address."""

    to: str
    """The to address. Use ``*`` for wildcard to match any to address."""

    metadata: Optional[dict[str, str]] = UNSET
    """Additional matching criteria for the capture rule. For voice calls, can include ``callType`` (``PSTN``, ``SIP``,
    and similar)."""


class ConversationsV2CaptureRuleDict(TypedDict):
    from_: str
    to: str
    metadata: NotRequired[dict[str, str]]
