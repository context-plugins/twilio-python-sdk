from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OverriddenLineType(str, Enum):
    """The new line type after the override"""

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


OverriddenLineTypeOrStr: TypeAlias = Annotated[OverriddenLineType | str, open_enum_validator(OverriddenLineType)]
