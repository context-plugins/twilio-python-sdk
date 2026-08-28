from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MessagingV1ServiceUsAppToPersonUsecase(SdkBaseModel):
    us_app_to_person_usecases: Optional[list[Any | None]] = UNSET
    """Human readable name, code, description and post_approval_required (indicates whether or not post approval is
    required for this Use Case) of A2P Campaign Use Cases."""


class MessagingV1ServiceUsAppToPersonUsecaseDict(TypedDict):
    us_app_to_person_usecases: NotRequired[list[Any | None]]
