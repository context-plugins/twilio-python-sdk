from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FactorEnumTotpAlgorithms(str, Enum):
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"

    __str__ = str.__str__


FactorEnumTotpAlgorithmsOrStr: TypeAlias = Annotated[
    FactorEnumTotpAlgorithms | str, open_enum_validator(FactorEnumTotpAlgorithms)
]
