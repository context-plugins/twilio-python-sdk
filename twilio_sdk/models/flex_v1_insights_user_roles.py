from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FlexV1InsightsUserRoles(SdkBaseModel):
    roles: Optional[list[str | None]] = UNSET
    """Flex Insights roles for the user"""

    url: OptionalNullable[str] = UNSET


class FlexV1InsightsUserRolesDict(TypedDict):
    roles: NotRequired[list[str | None]]
    url: NotRequired[str | None]
