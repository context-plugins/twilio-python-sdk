from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1FlexTeamMembers(SdkBaseModel):
    flex_user_sid: OptionalNullable[str] = UNSET
    friendly_name: OptionalNullable[str] = UNSET
    email: OptionalNullable[str] = UNSET
    worker_sid: OptionalNullable[str] = UNSET
    team_sid: OptionalNullable[str] = UNSET
    instance_sid: OptionalNullable[str] = UNSET
    account_sid: OptionalNullable[str] = UNSET


class FlexV1FlexTeamMembersDict(TypedDict):
    flex_user_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    email: NotRequired[str | None]
    worker_sid: NotRequired[str | None]
    team_sid: NotRequired[str | None]
    instance_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
