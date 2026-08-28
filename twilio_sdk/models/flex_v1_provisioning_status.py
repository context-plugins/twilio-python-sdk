from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.provisioning_status_enum_status import ProvisioningStatusEnumStatusOrStr


class FlexV1ProvisioningStatus(SdkBaseModel):
    status: Optional[ProvisioningStatusEnumStatusOrStr] = UNSET
    """Email Provisioning Status"""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the resource."""


class FlexV1ProvisioningStatusDict(TypedDict):
    status: NotRequired[ProvisioningStatusEnumStatusOrStr]
    url: NotRequired[AnyUrl | None]
