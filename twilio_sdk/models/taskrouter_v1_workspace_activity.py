from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceActivity(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Activity resource."""

    available: OptionalNullable[bool] = UNSET
    """Whether the Worker is eligible to receive a Task when it occupies the Activity. A value of ``true``, ``1``, or
    ``yes`` indicates the Activity is available. All other values indicate that it is not. The value cannot be changed
    after the Activity is created."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the Activity resource."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Activity resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Activity."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Activity resource."""

    links: OptionalNullable[Any] = UNSET


class TaskrouterV1WorkspaceActivityDict(TypedDict):
    account_sid: NotRequired[str | None]
    available: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    friendly_name: NotRequired[str | None]
    sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
