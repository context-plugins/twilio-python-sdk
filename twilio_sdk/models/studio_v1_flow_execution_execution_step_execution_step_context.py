from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class StudioV1FlowExecutionExecutionStepExecutionStepContext(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the ExecutionStepContext
    resource."""

    context: OptionalNullable[Any] = UNSET
    """The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data
    that your widgets can access as variables in configuration fields or in text areas as variable substitution."""

    execution_sid: OptionalNullable[str] = UNSET
    """The SID of the context's Execution resource."""

    flow_sid: OptionalNullable[str] = UNSET
    """The SID of the Flow."""

    step_sid: OptionalNullable[str] = UNSET
    """The SID of the Step that the context is associated with."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""


class StudioV1FlowExecutionExecutionStepExecutionStepContextDict(TypedDict):
    account_sid: NotRequired[str | None]
    context: NotRequired[Any | None]
    execution_sid: NotRequired[str | None]
    flow_sid: NotRequired[str | None]
    step_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
