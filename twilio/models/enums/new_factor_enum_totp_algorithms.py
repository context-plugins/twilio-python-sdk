from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NewFactorEnumTotpAlgorithms(str, Enum):
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"

    __str__ = str.__str__


NewFactorEnumTotpAlgorithmsOrStr: TypeAlias = Annotated[
    NewFactorEnumTotpAlgorithms | str, open_enum_validator(NewFactorEnumTotpAlgorithms)
]
