from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TollfreeVerificationEnumUseCaseCategory(str, Enum):
    TWO_FACTOR_AUTHENTICATION = "TWO_FACTOR_AUTHENTICATION"
    ACCOUNT_NOTIFICATIONS = "ACCOUNT_NOTIFICATIONS"
    CUSTOMER_CARE = "CUSTOMER_CARE"
    CHARITY_NONPROFIT = "CHARITY_NONPROFIT"
    DELIVERY_NOTIFICATIONS = "DELIVERY_NOTIFICATIONS"
    FRAUD_ALERT_MESSAGING = "FRAUD_ALERT_MESSAGING"
    EVENTS = "EVENTS"
    HIGHER_EDUCATION = "HIGHER_EDUCATION"
    K12 = "K12"
    MARKETING = "MARKETING"
    POLLING_AND_VOTING_NON_POLITICAL = "POLLING_AND_VOTING_NON_POLITICAL"
    POLITICAL_ELECTION_CAMPAIGNS = "POLITICAL_ELECTION_CAMPAIGNS"
    PUBLIC_SERVICE_ANNOUNCEMENT = "PUBLIC_SERVICE_ANNOUNCEMENT"
    SECURITY_ALERT = "SECURITY_ALERT"

    __str__ = str.__str__


TollfreeVerificationEnumUseCaseCategoryOrStr: TypeAlias = Annotated[
    TollfreeVerificationEnumUseCaseCategory | str, open_enum_validator(TollfreeVerificationEnumUseCaseCategory)
]
