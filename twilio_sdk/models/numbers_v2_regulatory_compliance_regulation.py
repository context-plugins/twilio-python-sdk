from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.regulation_enum_end_user_type import RegulationEnumEndUserTypeOrStr


class NumbersV2RegulatoryComplianceRegulation(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that identifies the Regulation resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """A human-readable description that is assigned to describe the Regulation resource. Examples can include Germany:
    Mobile - Business."""

    iso_country: OptionalNullable[str] = UNSET
    """The ISO country code of the phone number's country."""

    number_type: OptionalNullable[str] = UNSET
    """The type of phone number restricted by the regulatory requirement. For example, Germany mobile phone numbers
    provisioned by businesses require a business name with commercial register proof from the Handelsregisterauszug and
    a proof of address from Handelsregisterauszug or a trade license by Gewerbeanmeldung."""

    end_user_type: Optional[RegulationEnumEndUserTypeOrStr] = UNSET
    """The type of End User the regulation requires - can be ``individual`` or ``business``."""

    requirements: OptionalNullable[Any] = UNSET
    """The SID of an object that holds the regulatory information of the phone number country, phone number type, and
    end user type."""

    url: OptionalNullable[AnyUrl] = UNSET
    """The absolute URL of the Regulation resource."""


class NumbersV2RegulatoryComplianceRegulationDict(TypedDict):
    sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    iso_country: NotRequired[str | None]
    number_type: NotRequired[str | None]
    end_user_type: NotRequired[RegulationEnumEndUserTypeOrStr]
    requirements: NotRequired[Any | None]
    url: NotRequired[AnyUrl | None]
