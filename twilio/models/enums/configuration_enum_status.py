from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConfigurationEnumStatus(str, Enum):
    """The status of the Flex onboarding. Can be: ``ok``, ``inprogress``,``notstarted``."""

    OK = "ok"
    INPROGRESS = "inprogress"
    NOTSTARTED = "notstarted"

    __str__ = str.__str__


ConfigurationEnumStatusOrStr: TypeAlias = Annotated[
    ConfigurationEnumStatus | str, open_enum_validator(ConfigurationEnumStatus)
]
