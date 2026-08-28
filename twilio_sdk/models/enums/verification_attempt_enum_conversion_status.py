from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationAttemptEnumConversionStatus(str, Enum):
    """A string specifying the conversion status of the verification. A conversion happens when the user is able to
    provide the correct code. Possible values are ``CONVERTED`` and ``UNCONVERTED``."""

    CONVERTED = "converted"
    UNCONVERTED = "unconverted"

    __str__ = str.__str__


VerificationAttemptEnumConversionStatusOrStr: TypeAlias = Annotated[
    VerificationAttemptEnumConversionStatus | str, open_enum_validator(VerificationAttemptEnumConversionStatus)
]
