from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComplianceRegistrationEnumBusinessIdentityType(str, Enum):
    """The type of business identity. Can be ``direct customer`` or ``ISV``."""

    DIRECT_CUSTOMER = "direct_customer"
    ISV_RESELLER_OR_PARTNER = "isv_reseller_or_partner"
    UNKNOWN = "unknown"

    __str__ = str.__str__


ComplianceRegistrationEnumBusinessIdentityTypeOrStr: TypeAlias = Annotated[
    ComplianceRegistrationEnumBusinessIdentityType | str,
    open_enum_validator(ComplianceRegistrationEnumBusinessIdentityType),
]
