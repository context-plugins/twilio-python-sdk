from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConfigurationAddressEnumType(str, Enum):
    """Type of Address, value can be ``whatsapp`` or ``sms``."""

    SMS = "sms"
    WHATSAPP = "whatsapp"
    MESSENGER = "messenger"
    GBM = "gbm"
    EMAIL = "email"
    RCS = "rcs"
    APPLE = "apple"
    CHAT = "chat"

    __str__ = str.__str__


ConfigurationAddressEnumTypeOrStr: TypeAlias = Annotated[
    ConfigurationAddressEnumType | str, open_enum_validator(ConfigurationAddressEnumType)
]
