from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthorizationDocumentEnumStatus(str, Enum):
    """The status of the authorization document. Can be: ``opened``, ``signing``, ``signed``, ``canceled``, or
    ``failed``., Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4.
    canceled, 5. failed. See the section entitled `Status Values
    <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values>`__
    for more information on each of these statuses."""

    OPENED = "opened"
    SIGNING = "signing"
    SIGNED = "signed"
    CANCELED = "canceled"
    FAILED = "failed"

    __str__ = str.__str__


AuthorizationDocumentEnumStatusOrStr: TypeAlias = Annotated[
    AuthorizationDocumentEnumStatus | str, open_enum_validator(AuthorizationDocumentEnumStatus)
]
