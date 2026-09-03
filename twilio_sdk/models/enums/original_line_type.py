from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OriginalLineType(str, Enum):
    """The original line type"""

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


OriginalLineTypeOrStr: TypeAlias = Annotated[OriginalLineType | str, open_enum_validator(OriginalLineType)]
