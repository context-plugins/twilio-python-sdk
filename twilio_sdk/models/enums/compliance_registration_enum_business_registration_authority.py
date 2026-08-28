from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComplianceRegistrationEnumBusinessRegistrationAuthority(str, Enum):
    """The authority that registered the business"""

    UK_CRN = "UK:CRN"
    US_EIN = "US:EIN"
    CA_CBN = "CA:CBN"
    AU_ACN = "AU:ACN"
    OTHER = "Other"

    __str__ = str.__str__


ComplianceRegistrationEnumBusinessRegistrationAuthorityOrStr: TypeAlias = Annotated[
    ComplianceRegistrationEnumBusinessRegistrationAuthority | str,
    open_enum_validator(ComplianceRegistrationEnumBusinessRegistrationAuthority),
]
