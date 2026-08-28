from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationWebhookEnumTarget(str, Enum):
    """The routing target of the webhook. Can be ordinary or route internally to Flex"""

    WEBHOOK = "webhook"
    FLEX = "flex"

    __str__ = str.__str__


ConversationWebhookEnumTargetOrStr: TypeAlias = Annotated[
    ConversationWebhookEnumTarget | str, open_enum_validator(ConversationWebhookEnumTarget)
]
