from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountEnumStatus(str, Enum):
    """The status of this account. Usually ``active``, but can be ``suspended`` or ``closed``."""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    CLOSED = "closed"

    __str__ = str.__str__


AccountEnumStatusOrStr: TypeAlias = Annotated[AccountEnumStatus | str, open_enum_validator(AccountEnumStatus)]
