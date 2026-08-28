from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TollfreeVerificationEnumBusinessRegistrationAuthority(str, Enum):
    """The organizational authority for business registrations. Required for all business types except
    SOLE_PROPRIETOR."""

    EIN = "EIN"
    CBN = "CBN"
    CRN = "CRN"
    PROVINCIAL_NUMBER = "PROVINCIAL_NUMBER"
    VAT = "VAT"
    ACN = "ACN"
    ABN = "ABN"
    BRN = "BRN"
    SIREN = "SIREN"
    SIRET = "SIRET"
    NZBN = "NZBN"
    U_ST_ID_NR = "USt-IdNr"
    CIF = "CIF"
    NIF = "NIF"
    CNPJ = "CNPJ"
    UID = "UID"
    NEQ = "NEQ"
    OTHER = "OTHER"

    __str__ = str.__str__


TollfreeVerificationEnumBusinessRegistrationAuthorityOrStr: TypeAlias = Annotated[
    TollfreeVerificationEnumBusinessRegistrationAuthority | str,
    open_enum_validator(TollfreeVerificationEnumBusinessRegistrationAuthority),
]
