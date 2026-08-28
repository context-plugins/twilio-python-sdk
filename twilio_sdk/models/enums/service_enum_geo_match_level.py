from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceEnumGeoMatchLevel(str, Enum):
    """Where a proxy number must be located relative to the participant identifier. Can be: ``country``, ``area-code``,
    or ``extended-area-code``. The default value is ``country`` and more specific areas than ``country`` are only
    available in North America."""

    AREA_CODE = "area-code"
    OVERLAY = "overlay"
    RADIUS = "radius"
    COUNTRY = "country"

    __str__ = str.__str__


ServiceEnumGeoMatchLevelOrStr: TypeAlias = Annotated[
    ServiceEnumGeoMatchLevel | str, open_enum_validator(ServiceEnumGeoMatchLevel)
]
