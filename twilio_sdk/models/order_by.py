from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bundle_enum_sort_direction import BundleEnumSortDirectionOrStr


class OrderBy(SdkBaseModel):
    field: Optional[str] = UNSET
    """Dimension or measure to order by"""

    direction: Optional[BundleEnumSortDirectionOrStr] = UNSET
    """Sort order direction, ascending or descending"""


class OrderByDict(TypedDict):
    field: NotRequired[str]
    direction: NotRequired[BundleEnumSortDirectionOrStr]
