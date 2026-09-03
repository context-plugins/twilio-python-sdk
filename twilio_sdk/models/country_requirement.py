from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CountryRequirement(SdkBaseModel):
    iso_country: str
    """Iso country code as per ISO 3166-1 alpha-2 standard"""

    registration_required: bool
    """Whether Sender ID needs to be pre-registered for the country"""

    sla_in_days: int
    """Twilio SLA for Sender Id Registration process in business days. For countries requiring dynamic registration, it
    will be set to 0."""

    promotional_supported: Optional[bool] = UNSET
    """Whether promotional usage for Sender ID is supported"""

    promotional_sender_id_prefix: OptionalNullable[str] = UNSET
    """Mandatory prefix string for Sender ID when used for promotional purpose in the country"""

    promotional_sender_id_suffix: OptionalNullable[str] = UNSET
    """Mandatory suffix string for Sender ID when used for promotional purpose in the country"""

    pricing_scheme: OptionalNullable[str] = UNSET
    """Represents pricing requirements for country with free-flowing string format"""

    documentation_url: OptionalNullable[str] = UNSET
    """Represents public Twilio support URL which has information regarding the instructions and documents required for
    registration"""

    documentation_template_url: OptionalNullable[str] = UNSET
    """Represents the Twilio public URL for documentation template required to be filled for the Sender ID
    registration"""

    document_type_machine_names: Optional[list[str]] = UNSET
    """List of document type machine names"""

    domestic_document_type_machine_names: Optional[list[str]] = UNSET
    """List of document type machine names for Domestic traffic reach"""

    international_document_type_machine_names: Optional[list[str]] = UNSET
    """List of document type machine names for International traffic reach"""

    sender_id_registration_rules: OptionalNullable[str] = UNSET
    """Sender ID string rules for the country"""

    uso_enabled: OptionalNullable[bool] = UNSET
    """Whether USO (Unified Sender Onboarding) is enabled for this country"""


class CountryRequirementDict(TypedDict):
    iso_country: str
    registration_required: bool
    sla_in_days: int
    promotional_supported: NotRequired[bool]
    promotional_sender_id_prefix: NotRequired[str | None]
    promotional_sender_id_suffix: NotRequired[str | None]
    pricing_scheme: NotRequired[str | None]
    documentation_url: NotRequired[str | None]
    documentation_template_url: NotRequired[str | None]
    document_type_machine_names: NotRequired[list[str]]
    domestic_document_type_machine_names: NotRequired[list[str]]
    international_document_type_machine_names: NotRequired[list[str]]
    sender_id_registration_rules: NotRequired[str | None]
    uso_enabled: NotRequired[bool | None]
