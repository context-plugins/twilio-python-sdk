from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FlexMeetingCallbackEventsEnumWebhookType(str, Enum):
    GLOBAL = "global"
    INTERACTION = "interaction"

    __str__ = str.__str__


FlexMeetingCallbackEventsEnumWebhookTypeOrStr: TypeAlias = Annotated[
    FlexMeetingCallbackEventsEnumWebhookType | str, open_enum_validator(FlexMeetingCallbackEventsEnumWebhookType)
]
