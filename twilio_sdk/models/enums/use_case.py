from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UseCase(str, Enum):
    """The messaging use case type for the RCS sender. Allowed values are ``PROMOTIONAL``, ``TRANSACTIONAL``, ``OTP``,
    ``MULTI_USE``. Defaults to ``MULTI_USE`` if not provided. Cannot be modified after launch."""

    PROMOTIONAL = "PROMOTIONAL"
    TRANSACTIONAL = "TRANSACTIONAL"
    OTP = "OTP"
    MULTI_USE = "MULTI_USE"

    __str__ = str.__str__


UseCaseOrStr: TypeAlias = Annotated[UseCase | str, open_enum_validator(UseCase)]
