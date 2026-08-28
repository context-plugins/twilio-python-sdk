from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComplianceRegistrationEnumPhoneNumberType(str, Enum):
    """The type of phone number of the Bundle's ownership request. Can be ``local``, ``mobile``, ``national``, or
    ``toll-free``."""

    LOCAL = "local"
    NATIONAL = "national"
    MOBILE = "mobile"
    TOLL_FREE = "toll-free"

    __str__ = str.__str__


ComplianceRegistrationEnumPhoneNumberTypeOrStr: TypeAlias = Annotated[
    ComplianceRegistrationEnumPhoneNumberType | str, open_enum_validator(ComplianceRegistrationEnumPhoneNumberType)
]
