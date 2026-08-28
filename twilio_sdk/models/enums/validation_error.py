from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ValidationError(str, Enum):
    """Contains reasons why a phone number is invalid. Possible values: TOO_SHORT, TOO_LONG, INVALID_BUT_POSSIBLE,
    INVALID_COUNTRY_CODE, INVALID_LENGTH, NOT_A_NUMBER."""

    TOO_SHORT = "TOO_SHORT"
    TOO_LONG = "TOO_LONG"
    INVALID_BUT_POSSIBLE = "INVALID_BUT_POSSIBLE"
    INVALID_COUNTRY_CODE = "INVALID_COUNTRY_CODE"
    INVALID_LENGTH = "INVALID_LENGTH"
    NOT_A_NUMBER = "NOT_A_NUMBER"

    __str__ = str.__str__


ValidationErrorOrStr: TypeAlias = Annotated[ValidationError | str, open_enum_validator(ValidationError)]
