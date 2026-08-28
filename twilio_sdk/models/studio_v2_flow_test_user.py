from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class StudioV2FlowTestUser(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """Unique identifier of the flow."""

    test_users: Optional[list[str | None]] = UNSET
    """List of test user identities that can test draft versions of the flow."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The URL of this resource."""


class StudioV2FlowTestUserDict(TypedDict):
    sid: NotRequired[str | None]
    test_users: NotRequired[list[str | None]]
    url: NotRequired[AnyUrl | None]
