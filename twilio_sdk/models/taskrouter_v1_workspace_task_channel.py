from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceTaskChannel(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Task Channel
    resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Task Channel resource."""

    unique_name: OptionalNullable[str] = UNSET
    """An application-defined string that uniquely identifies the Task Channel, such as ``voice`` or ``sms``."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Task Channel."""

    channel_optimized_routing: OptionalNullable[bool] = UNSET
    """Whether the Task Channel will prioritize Workers that have been idle. When ``true``, Workers that have been idle
    the longest are prioritized."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Task Channel resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class TaskrouterV1WorkspaceTaskChannelDict(TypedDict):
    account_sid: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    friendly_name: NotRequired[str | None]
    sid: NotRequired[str | None]
    unique_name: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    channel_optimized_routing: NotRequired[bool | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
