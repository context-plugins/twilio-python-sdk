from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WhatsappTemplateEnumCategory(str, Enum):
    """The Category of this WhatsApp Template. One of ``ACCOUNT_UPDATE``, ``ALERT_UPDATE``, ``APPOINTMENT_UPDATE``,
    ``AUTO_REPLY``, ``ISSUE_RESOLUTION``, ``PAYMENT_UPDATE``, ``PERSONAL_FINANCE_UPDATE``, ``RESERVATION_UPDATE``,
    ``SHIPPING_UPDATE``, ``TICKET_UPDATE``, ``TRANSPORTATION_UPDATE``, ``MARKETING``, ``AUTHENTICATION``, ``UTILITY``,
    ``OTP`` or ``TRANSACTIONAL``."""

    ACCOUNT_UPDATE = "ACCOUNT_UPDATE"
    ALERT_UPDATE = "ALERT_UPDATE"
    AUTO_REPLY = "AUTO_REPLY"
    APPOINTMENT_UPDATE = "APPOINTMENT_UPDATE"
    ISSUE_RESOLUTION = "ISSUE_RESOLUTION"
    PAYMENT_UPDATE = "PAYMENT_UPDATE"
    PERSONAL_FINANCE_UPDATE = "PERSONAL_FINANCE_UPDATE"
    RESERVATION_UPDATE = "RESERVATION_UPDATE"
    SHIPPING_UPDATE = "SHIPPING_UPDATE"
    TICKET_UPDATE = "TICKET_UPDATE"
    TRANSPORTATION_UPDATE = "TRANSPORTATION_UPDATE"
    MARKETING = "MARKETING"
    OTP = "OTP"
    TRANSACTIONAL = "TRANSACTIONAL"
    AUTHENTICATION = "AUTHENTICATION"
    UTILITY = "UTILITY"

    __str__ = str.__str__


WhatsappTemplateEnumCategoryOrStr: TypeAlias = Annotated[
    WhatsappTemplateEnumCategory | str, open_enum_validator(WhatsappTemplateEnumCategory)
]
