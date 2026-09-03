from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class NumbersV2RegulatoryComplianceEndUserType(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the End-User Type resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human-readable description that is assigned to describe the End-User Type resource. Examples can include first
    name, last name, email, business name, etc"""

    machine_name: OptionalNullable[str] = UNSET
    """A machine-readable description of the End-User Type resource. Examples can include first_name, last_name, email,
    business_name, etc."""

    fields: Optional[list[Any | None]] = UNSET
    """The required information for creating an End-User. The required fields will change as regulatory needs change and
    will differ for businesses and individuals."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the End-User Type resource."""


class NumbersV2RegulatoryComplianceEndUserTypeDict(TypedDict):
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    machine_name: NotRequired[str | None]
    fields: NotRequired[list[Any | None]]
    url: NotRequired[str | None]
