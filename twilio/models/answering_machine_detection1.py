from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AnsweringMachineDetection1(SdkBaseModel):
    """Number of calls made in answering machine detection (AMD) enabled."""

    total_calls: Optional[int] = UNSET
    """Total number of calls with answering machine detection (AMD) enabled."""

    answered_by_human_percentage: Optional[float] = UNSET
    """Percentage of calls marked as answered by human."""

    answered_by_machine_percentage: Optional[float] = UNSET
    """Percentage of calls marked as answered by machined related like the following: ``machine_start``,
    ``machine_end_beep``, ``machine_end_silence``, ``machine_end_other``, ``fax``"""


class AnsweringMachineDetection1Dict(TypedDict):
    total_calls: NotRequired[int]
    answered_by_human_percentage: NotRequired[float]
    answered_by_machine_percentage: NotRequired[float]
