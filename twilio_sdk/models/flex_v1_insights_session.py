from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1InsightsSession(SdkBaseModel):
    workspace_id: OptionalNullable[str] = UNSET
    """Unique ID to identify the user's workspace"""

    session_expiry: OptionalNullable[str] = UNSET
    """The session expiry date and time, given in ISO 8601 format."""

    session_id: OptionalNullable[str] = UNSET
    """The unique ID for the session"""

    base_url: OptionalNullable[str] = UNSET
    """The base URL to fetch reports and dashboards"""

    url: OptionalNullable[str] = UNSET
    """The URL of this resource."""


class FlexV1InsightsSessionDict(TypedDict):
    workspace_id: NotRequired[str | None]
    session_expiry: NotRequired[str | None]
    session_id: NotRequired[str | None]
    base_url: NotRequired[str | None]
    url: NotRequired[str | None]
