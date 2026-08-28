from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallCount(SdkBaseModel):
    """Total number of calls for each STIR/SHAKEN attestation category."""

    stsh_a: Optional[int] = UNSET
    """Total number of calls for Stir Shaken category A."""

    stsh_b: Optional[int] = UNSET
    """Total number of calls for Stir Shaken category B."""

    stsh_c: Optional[int] = UNSET
    """Total number of calls for Stir Shaken category C."""


class CallCountDict(TypedDict):
    stsh_a: NotRequired[int]
    stsh_b: NotRequired[int]
    stsh_c: NotRequired[int]
