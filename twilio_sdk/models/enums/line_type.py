from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LineType(str, Enum):
    """The new line type to override the original line type"""

    MOBILE = "mobile"
    LANDLINE = "landline"
    TOLL_FREE = "tollFree"
    FIXED_VOIP = "fixedVoip"
    NON_FIXED_VOIP = "nonFixedVoip"
    PERSONAL = "personal"
    PREMIUM = "premium"
    VOICEMAIL = "voicemail"
    SHARED_COST = "sharedCost"
    UAN = "uan"
    PAGER = "pager"
    UNKNOWN = "unknown"

    __str__ = str.__str__


LineTypeOrStr: TypeAlias = Annotated[LineType | str, open_enum_validator(LineType)]
