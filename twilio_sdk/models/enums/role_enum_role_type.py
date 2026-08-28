from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoleEnumRoleType(str, Enum):
    """The type of role. Can be: ``conversation`` for `Conversation
    <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ roles or ``service`` for `Conversation
    Service <https://www.twilio.com/docs/conversations/api/service-resource>`__ roles."""

    CONVERSATION = "conversation"
    SERVICE = "service"

    __str__ = str.__str__


RoleEnumRoleTypeOrStr: TypeAlias = Annotated[RoleEnumRoleType | str, open_enum_validator(RoleEnumRoleType)]
