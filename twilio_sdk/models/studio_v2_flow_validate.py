from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class StudioV2FlowValidate(SdkBaseModel):
    valid: OptionalNullable[bool] = UNSET
    """Boolean if the flow definition is valid."""


class StudioV2FlowValidateDict(TypedDict):
    valid: NotRequired[bool | None]
