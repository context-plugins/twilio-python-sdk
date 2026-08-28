from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceStatsConversationsRatelimitingerrorsEnumSource(str, Enum):
    """Source via which the request came from. Can be sdk, api."""

    SDK = "SDK"
    API = "API"

    __str__ = str.__str__


ServiceStatsConversationsRatelimitingerrorsEnumSourceOrStr: TypeAlias = Annotated[
    ServiceStatsConversationsRatelimitingerrorsEnumSource | str,
    open_enum_validator(ServiceStatsConversationsRatelimitingerrorsEnumSource),
]
