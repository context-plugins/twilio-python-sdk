from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class StudioV1FlowEngagementEngagementContext(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the Account."""

    context: OptionalNullable[Any] = UNSET
    """As your flow executes, we save the state in what's called the Flow Context. Any data in the flow context can be
    accessed by your widgets as variables, either in configuration fields or in text areas as variable substitution."""

    engagement_sid: OptionalNullable[str] = UNSET
    """The SID of the Engagement."""

    flow_sid: OptionalNullable[str] = UNSET
    """The SID of the Flow."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of the resource."""


class StudioV1FlowEngagementEngagementContextDict(TypedDict):
    account_sid: NotRequired[str | None]
    context: NotRequired[Any | None]
    engagement_sid: NotRequired[str | None]
    flow_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
