from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EligibilityEnumEligibilitySubStatus(str, Enum):
    COUNTRY_INELIGIBLE = "country-ineligible"
    NUMBER_FORMAT_INELIGIBLE = "number-format-ineligible"
    NUMBER_TYPE_INELIGIBLE = "number-type-ineligible"
    CARRIER_INELIGIBLE = "carrier-ineligible"
    ALREADY_IN_TWILIO = "already-in-twilio"
    INTERNAL_PROCESSING_ERROR = "internal-processing-error"
    INVALID_PHONE_NUMBER = "invalid-phone-number"
    INVALID_HOSTING_ACCOUNT_SID = "invalid-hosting-account-sid"
    ELIGIBLE = "eligible"

    __str__ = str.__str__


EligibilityEnumEligibilitySubStatusOrStr: TypeAlias = Annotated[
    EligibilityEnumEligibilitySubStatus | str, open_enum_validator(EligibilityEnumEligibilitySubStatus)
]
