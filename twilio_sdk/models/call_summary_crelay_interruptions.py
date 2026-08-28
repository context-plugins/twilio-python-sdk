from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallSummaryCrelayInterruptions(SdkBaseModel):
    customer_to_agent: Optional[int] = UNSET
    agent_to_customer: Optional[int] = UNSET


class CallSummaryCrelayInterruptionsDict(TypedDict):
    customer_to_agent: NotRequired[int]
    agent_to_customer: NotRequired[int]
