from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dimension import Dimension, DimensionDict
from .measure import Measure, MeasureDict


class Cube(SdkBaseModel):
    name: str
    """Name of the cube, used as a reference in queries"""

    description: Optional[str] = UNSET
    """Human-readable description of what the cube represents"""

    measures: list[Measure]
    """List of measures available in the cube, representing quantitative values that can be aggregated"""

    dimensions: list[Dimension]
    """List of dimensions available in the cube, representing categorical attributes for grouping data"""


class CubeDict(TypedDict):
    name: str
    description: NotRequired[str]
    measures: list[Measure | MeasureDict]
    dimensions: list[Dimension | DimensionDict]
