from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FlexV1FlexTeamOwners(SdkBaseModel):
    flex_user_sid: OptionalNullable[str] = UNSET
    friendly_name: OptionalNullable[str] = UNSET
    email: OptionalNullable[str] = UNSET
    worker_sid: OptionalNullable[str] = UNSET
    team_sid: OptionalNullable[str] = UNSET
    instance_sid: OptionalNullable[str] = UNSET
    account_sid: OptionalNullable[str] = UNSET
    url: OptionalNullable[AnyUrl] = UNSET


class FlexV1FlexTeamOwnersDict(TypedDict):
    flex_user_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    email: NotRequired[str | None]
    worker_sid: NotRequired[str | None]
    team_sid: NotRequired[str | None]
    instance_sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
