from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ApiV2010AccountCallCallEvent(SdkBaseModel):
    request: OptionalNullable[Any] = UNSET
    """Contains a dictionary representing the request of the call."""

    response: OptionalNullable[Any] = UNSET
    """Contains a dictionary representing the call response, including a list of the call events."""


class ApiV2010AccountCallCallEventDict(TypedDict):
    request: NotRequired[Any | None]
    response: NotRequired[Any | None]
