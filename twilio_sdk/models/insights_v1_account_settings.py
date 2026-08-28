from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class InsightsV1AccountSettings(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Account."""

    advanced_features: OptionalNullable[bool] = UNSET
    """A boolean flag indicating whether Advanced Features for Voice Insights are enabled."""

    voice_trace: OptionalNullable[bool] = UNSET
    """A boolean flag indicating whether Voice Trace is enabled."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""


class InsightsV1AccountSettingsDict(TypedDict):
    account_sid: NotRequired[str | None]
    advanced_features: NotRequired[bool | None]
    voice_trace: NotRequired[bool | None]
    url: NotRequired[AnyUrl | None]
