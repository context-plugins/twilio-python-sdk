from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProvisioningStatusEnumStatus(str, Enum):
    """Email Provisioning Status"""

    ACTIVE = "active"
    IN_PROGRESS = "in-progress"
    NOT_CONFIGURED = "not-configured"
    FAILED = "failed"

    __str__ = str.__str__


ProvisioningStatusEnumStatusOrStr: TypeAlias = Annotated[
    ProvisioningStatusEnumStatus | str, open_enum_validator(ProvisioningStatusEnumStatus)
]
