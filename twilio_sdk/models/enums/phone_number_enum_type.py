from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PhoneNumberEnumType(str, Enum):
    LANDLINE = "landline"
    MOBILE = "mobile"
    VOIP = "voip"

    __str__ = str.__str__


PhoneNumberEnumTypeOrStr: TypeAlias = Annotated[PhoneNumberEnumType | str, open_enum_validator(PhoneNumberEnumType)]
