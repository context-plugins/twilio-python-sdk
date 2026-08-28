from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Measure(SdkBaseModel):
    name: str
    """Identifier used to reference this measure in queries"""

    description: Optional[str] = UNSET
    """Detailed explanation of what this measure represents"""

    type_: str = Field(alias="type")
    """Type of the measure"""

    aggregation: Optional[str] = UNSET
    """Aggregation type for the measure (e.g., sum, count, average)"""


class MeasureDict(TypedDict):
    name: str
    description: NotRequired[str]
    type_: str
    aggregation: NotRequired[str]
