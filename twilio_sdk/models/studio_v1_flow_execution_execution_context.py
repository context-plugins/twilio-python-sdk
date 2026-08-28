from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class StudioV1FlowExecutionExecutionContext(SdkBaseModel):
    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the ExecutionContext
    resource."""

    context: OptionalNullable[Any] = UNSET
    """The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data
    that your widgets can access as variables in configuration fields or in text areas as variable substitution."""

    flow_sid: OptionalNullable[str] = UNSET
    """The SID of the Flow."""

    execution_sid: OptionalNullable[str] = UNSET
    """The SID of the context's Execution resource."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""


class StudioV1FlowExecutionExecutionContextDict(TypedDict):
    account_sid: NotRequired[str | None]
    context: NotRequired[Any | None]
    flow_sid: NotRequired[str | None]
    execution_sid: NotRequired[str | None]
    url: NotRequired[AnyUrl | None]
