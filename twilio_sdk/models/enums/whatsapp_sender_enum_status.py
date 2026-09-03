from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WhatsappSenderEnumStatus(str, Enum):
    """The status of the sender. Configuring: We are in the process of registering the sender. If your sender stays in
    this state for a long period of time it is possible that there is an issue with parameters you provided;
    PendingVerification: We have successfully registered the sender with WhatsApp and you should receive a code from
    their services; Configured: The sender has been successfully verified with WhatsApp and is all set to start sending
    messages; ConfigurationError - If configuration fails due to below possibilities: parameters provided were
    incorrect, Twilio account suspended or deleted, whatsapp api failed, Twilio internal error. VerificationError - If
    verification api fails, please check error_message for more details"""

    CONFIGURING = "Configuring"
    PENDING_VERIFICATION = "PendingVerification"
    CONFIGURED = "Configured"
    CONFIGURATION_ERROR = "ConfigurationError"
    VERIFICATION_ERROR = "VerificationError"

    __str__ = str.__str__


WhatsappSenderEnumStatusOrStr: TypeAlias = Annotated[
    WhatsappSenderEnumStatus | str, open_enum_validator(WhatsappSenderEnumStatus)
]
