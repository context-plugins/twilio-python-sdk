from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MessagingV1Usecase(SdkBaseModel):
    usecases: Optional[list[Any | None]] = UNSET
    """Human readable use case details (usecase, description and purpose) of Messaging Service Use Cases."""


class MessagingV1UsecaseDict(TypedDict):
    usecases: NotRequired[list[Any | None]]
