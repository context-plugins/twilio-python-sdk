from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    """The valid credential types supported by the API. The values of this enumeration are used for versioning the
    ``AuthenticatorAssertion`` and ``AuthenticatorAttestation`` structures according to the type of the
    authenticator."""

    PUBLIC_KEY = "public-key"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]
