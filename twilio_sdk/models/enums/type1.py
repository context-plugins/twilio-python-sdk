from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type1(str, Enum):
    """The valid credential types supported by the API. The values of this enumeration are used for versioning the
    ``AuthenticatorAssertion`` and ``AuthenticatorAttestation`` structures according to the type of the
    authenticator."""

    PUBLIC_KEY = "public-key"

    __str__ = str.__str__


Type1OrStr: TypeAlias = Annotated[Type1 | str, open_enum_validator(Type1)]
