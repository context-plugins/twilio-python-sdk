from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class FlexV2FlexUser(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The unique SID of the account that created the resource."""

    instance_sid: OptionalNullable[str] = UNSET
    """The unique ID created by Twilio to identify a Flex instance."""

    user_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Twilio Unified User."""

    flex_user_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Flex User."""

    worker_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the worker."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the workspace."""

    flex_team_sid: OptionalNullable[str] = UNSET
    """The unique SID identifier of the Flex Team."""

    username: OptionalNullable[str] = UNSET
    """Username of the User."""

    email: OptionalNullable[str] = UNSET
    """Email of the User."""

    locale: OptionalNullable[str] = UNSET
    """The locale preference of the user."""

    roles: Optional[list[str | None]] = UNSET
    """The roles of the user."""

    created_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this user was created, given in ISO 8601 format."""

    updated_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The date that this user was updated, given in ISO 8601 format."""

    version: Optional[int] = UNSET
    """The current version of the user."""

    url: OptionalNullable[AnyUrl] = UNSET


class FlexV2FlexUserDict(TypedDict):
    account_sid: NotRequired[str | None]
    instance_sid: NotRequired[str | None]
    user_sid: NotRequired[str | None]
    flex_user_sid: NotRequired[str | None]
    worker_sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    flex_team_sid: NotRequired[str | None]
    username: NotRequired[str | None]
    email: NotRequired[str | None]
    locale: NotRequired[str | None]
    roles: NotRequired[list[str | None]]
    created_date: NotRequired[RFC3339DateTime | None]
    updated_date: NotRequired[RFC3339DateTime | None]
    version: NotRequired[int]
    url: NotRequired[AnyUrl | None]
