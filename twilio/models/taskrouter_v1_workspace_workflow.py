from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TaskrouterV1WorkspaceWorkflow(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Workflow resource."""

    assignment_callback_url: OptionalNullable[str] = UNSET
    """The URL that we call when a task managed by the Workflow is assigned to a Worker. See Assignment Callback URL for
    more information."""

    configuration: OptionalNullable[str] = UNSET
    """A JSON string that contains the Workflow's configuration. See `Configuring Workflows
    <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `RFC 2822
    <https://www.ietf.org/rfc/rfc2822.txt>`__ format."""

    document_content_type: OptionalNullable[str] = UNSET
    """The MIME type of the document."""

    fallback_assignment_callback_url: OptionalNullable[str] = UNSET
    """The URL that we call when a call to the ``assignment_callback_url`` fails."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the Workflow resource. For example, ``Customer Support`` or ``2014
    Election Campaign``."""

    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Workflow resource."""

    task_reservation_timeout: Optional[int] = UNSET
    """How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a
    Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``."""

    workspace_sid: OptionalNullable[str] = UNSET
    """The SID of the Workspace that contains the Workflow."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Workflow resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class TaskrouterV1WorkspaceWorkflowDict(TypedDict):
    account_sid: NotRequired[str | None]
    assignment_callback_url: NotRequired[str | None]
    configuration: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    document_content_type: NotRequired[str | None]
    fallback_assignment_callback_url: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    sid: NotRequired[str | None]
    task_reservation_timeout: NotRequired[int]
    workspace_sid: NotRequired[str | None]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
