from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType(str, Enum):
    """The account type for ISV Account Type Migration. Set to 'ISV' or 'ISVSubAccount' to configure, empty string to
    clear, or omit to preserve the existing value."""

    ISV = "ISV"
    ISV_SUB_ACCOUNT = "ISVSubAccount"

    __str__ = str.__str__


AccountTypeOrStr: TypeAlias = Annotated[AccountType | str, open_enum_validator(AccountType)]
