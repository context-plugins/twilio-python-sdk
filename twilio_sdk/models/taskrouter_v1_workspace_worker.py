from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceWorker(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Worker resource."""

    activity_name: OptionalNullable[str] = UNSET
    """The ``friendly_name`` of the Worker's current Activity."""

    activity_sid: OptionalNullable[str] = UNSET
    """The SID of the Worker's current Activity."""

    attributes: OptionalNullable[str] = UNSET
    """The JSON string that describes the Worker. For example: ``{ "email": "Bob@example.com", "phone": "+5095551234"
    }``. **Note** If this property has been assigned a value, it will only be displayed in FETCH actions that return a
    single resource. Otherwise, this property will be null, even if it has a value. This data is passed to the
    ``assignment_callback_url`` when TaskRouter assigns a Task to the Worker."""

    available: OptionalNullable[bool] = UNSET
    """Whether the Worker is available to perform tasks."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_status_changed: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT of the last change to the Worker's activity specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format. Used to calculate Workflow statistics."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource. Friendly names are case insensitive, and unique within the
    TaskRouter Workspace."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Worker resource."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Worker."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Worker resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class TaskrouterV1WorkspaceWorkerDict(TypedDict):
    account_sid: NotRequired[str | None]
    activity_name: NotRequired[str | None]
    activity_sid: NotRequired[str | None]
    attributes: NotRequired[str | None]
    available: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_status_changed: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    friendly_name: NotRequired[str | None]
    sid: NotRequired[str | None]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
