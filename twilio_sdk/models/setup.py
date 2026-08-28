from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Setup(SdkBaseModel):
    charges_apply: bool


class SetupDict(TypedDict):
    charges_apply: bool
