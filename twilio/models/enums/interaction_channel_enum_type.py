from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InteractionChannelEnumType(str, Enum):
    """The Interaction Channel's type. Can be: ``sms``, ``email``, ``chat``, ``whatsapp``, ``web``, ``messenger``, or
    ``gbm``.
     **Note:** These can be different from the task channel type specified in the Routing attributes. Task channel type
        corresponds to channel capacity while this channel type is the actual media type"""

    VOICE = "voice"
    SMS = "sms"
    EMAIL = "email"
    WEB = "web"
    WHATSAPP = "whatsapp"
    CHAT = "chat"
    MESSENGER = "messenger"
    GBM = "gbm"

    __str__ = str.__str__


InteractionChannelEnumTypeOrStr: TypeAlias = Annotated[
    InteractionChannelEnumType | str, open_enum_validator(InteractionChannelEnumType)
]
