from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class StudioV1FlowExecutionExecutionStep(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the ExecutionStep resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the ExecutionStep
    resource."""

    flow_sid: OptionalNullable[str] = UNSET
    """The SID of the Flow."""

    execution_sid: OptionalNullable[str] = UNSET
    """The SID of the Step's Execution resource."""

    parent_step_sid: OptionalNullable[str] = UNSET
    """This field shows the Step SID of the Widget in the parent Flow that started the Subflow. If this Step is not part
    of a Subflow execution, the value is null."""

    name: OptionalNullable[str] = UNSET
    """The event that caused the Flow to transition to the Step."""

    context: OptionalNullable[Any] = UNSET
    """The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data
    that your widgets can access as variables in configuration fields or in text areas as variable substitution."""

    transitioned_from: OptionalNullable[str] = UNSET
    """The Widget that preceded the Widget for the Step."""

    transitioned_to: OptionalNullable[str] = UNSET
    """The Widget that will follow the Widget for the Step."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the widget that was executed."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""

    links: OptionalNullable[Any] = UNSET
    """The URLs of related resources."""


class StudioV1FlowExecutionExecutionStepDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    flow_sid: NotRequired[str | None]
    execution_sid: NotRequired[str | None]
    parent_step_sid: NotRequired[str | None]
    name: NotRequired[str | None]
    context: NotRequired[Any | None]
    transitioned_from: NotRequired[str | None]
    transitioned_to: NotRequired[str | None]
    type_: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[AnyUrl | None]
    links: NotRequired[Any | None]
