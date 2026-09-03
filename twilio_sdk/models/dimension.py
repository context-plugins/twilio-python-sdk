from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Dimension(SdkBaseModel):
    name: str
    """Identifier used to reference this dimension in queries"""

    description: Optional[str] = UNSET
    """Detailed explanation of what this dimension represents"""

    type_: str = Field(alias="type")
    """Data type of the dimension (e.g., string, number, boolean, date)"""


class DimensionDict(TypedDict):
    name: str
    description: NotRequired[str]
    type_: str
