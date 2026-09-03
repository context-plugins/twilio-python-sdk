from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FlexFlowEnumChannelType(str, Enum):
    """The channel type. One of ``web``, ``facebook``, ``sms``, ``whatsapp``, ``line`` or ``custom``. By default,
    Studio’s Send to Flex widget passes it on to the Task attributes for Tasks created based on this Flex Flow. The Task
    attributes will be used by the Flex UI to render the respective Task as appropriate (applying channel-specific
    design and length limits). If ``channelType`` is ``facebook``, ``whatsapp`` or ``line``, the Send to Flex widget
    should set the Task Channel to Programmable Chat."""

    WEB = "web"
    SMS = "sms"
    FACEBOOK = "facebook"
    WHATSAPP = "whatsapp"
    LINE = "line"
    CUSTOM = "custom"

    __str__ = str.__str__


FlexFlowEnumChannelTypeOrStr: TypeAlias = Annotated[
    FlexFlowEnumChannelType | str, open_enum_validator(FlexFlowEnumChannelType)
]
