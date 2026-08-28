from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceEnumNumberSelectionBehavior(str, Enum):
    """The preference for Proxy Number selection in the Service instance. Can be: ``prefer-sticky`` or ``avoid-sticky``.
    ``prefer-sticky`` means that we will try and select the same Proxy Number for a given participant if they have
    previous `Sessions <https://www.twilio.com/docs/proxy/api/session>`__, but we will not fail if that Proxy Number
    cannot be used. ``avoid-sticky`` means that we will try to use different Proxy Numbers as long as that is possible
    within a given pool rather than try and use a previously assigned number."""

    AVOID_STICKY = "avoid-sticky"
    PREFER_STICKY = "prefer-sticky"

    __str__ = str.__str__


ServiceEnumNumberSelectionBehaviorOrStr: TypeAlias = Annotated[
    ServiceEnumNumberSelectionBehavior | str, open_enum_validator(ServiceEnumNumberSelectionBehavior)
]
