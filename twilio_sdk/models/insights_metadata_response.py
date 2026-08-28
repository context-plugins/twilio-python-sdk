from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cube import Cube, CubeDict


class InsightsMetadataResponse(SdkBaseModel):
    """Response containing metadata about available cubes, measures, and dimensions for a domain"""

    domain: Optional[str] = UNSET
    """The business domain name for which metadata is being provided"""

    cubes: Optional[list[Cube]] = UNSET
    """List of data cubes available in the domain, each containing measures and dimensions"""


class InsightsMetadataResponseDict(TypedDict):
    domain: NotRequired[str]
    cubes: NotRequired[list[Cube | CubeDict]]
