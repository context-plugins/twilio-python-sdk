from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TollfreeVerificationEnumOptInType(str, Enum):
    """Describe how a user opts-in to text messages."""

    VERBAL = "VERBAL"
    WEB_FORM = "WEB_FORM"
    PAPER_FORM = "PAPER_FORM"
    VIA_TEXT = "VIA_TEXT"
    MOBILE_QR_CODE = "MOBILE_QR_CODE"
    IMPORT = "IMPORT"
    IMPORT_PLEASE_REPLACE = "IMPORT_PLEASE_REPLACE"

    __str__ = str.__str__


TollfreeVerificationEnumOptInTypeOrStr: TypeAlias = Annotated[
    TollfreeVerificationEnumOptInType | str, open_enum_validator(TollfreeVerificationEnumOptInType)
]
