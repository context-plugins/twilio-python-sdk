from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BrandRegistrationsEnumIdentityStatus(str, Enum):
    """When a brand is registered, TCR will attempt to verify the identity of the brand based on the supplied
    information."""

    SELF_DECLARED = "SELF_DECLARED"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    VETTED_VERIFIED = "VETTED_VERIFIED"

    __str__ = str.__str__


BrandRegistrationsEnumIdentityStatusOrStr: TypeAlias = Annotated[
    BrandRegistrationsEnumIdentityStatus | str, open_enum_validator(BrandRegistrationsEnumIdentityStatus)
]
