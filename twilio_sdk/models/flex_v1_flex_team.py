from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV1FlexTeam(SdkBaseModel):
    team_sid: OptionalNullable[str] = UNSET
    friendly_name: OptionalNullable[str] = UNSET
    member_count: Optional[int] = UNSET
    description: OptionalNullable[str] = UNSET
    level: Optional[int] = UNSET
    parent_team_sid: OptionalNullable[str] = UNSET
    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    version: Optional[int] = UNSET
    account_sid: OptionalNullable[str] = UNSET
    instance_sid: OptionalNullable[str] = UNSET
    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1FlexTeamDict(TypedDict):
    team_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    member_count: NotRequired[int]
    description: NotRequired[str | None]
    level: NotRequired[int]
    parent_team_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    version: NotRequired[int]
    account_sid: NotRequired[str | None]
    instance_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
