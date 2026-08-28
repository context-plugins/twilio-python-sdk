from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class NumbersV2RegulatoryComplianceSupportingDocumentType(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the Supporting Document Type resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human-readable description of the Supporting Document Type resource."""

    machine_name: OptionalNullable[str] = UNSET
    """The machine-readable description of the Supporting Document Type resource."""

    fields: Optional[list[Any | None]] = UNSET
    """The required information for creating a Supporting Document. The required fields will change as regulatory needs
    change and will differ for businesses and individuals."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Supporting Document Type resource."""


class NumbersV2RegulatoryComplianceSupportingDocumentTypeDict(TypedDict):
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    machine_name: NotRequired[str | None]
    fields: NotRequired[list[Any | None]]
    url: NotRequired[AnyUrl | None]
