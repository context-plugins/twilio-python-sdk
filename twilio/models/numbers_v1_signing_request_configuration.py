from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class NumbersV1SigningRequestConfiguration(SdkBaseModel):
    logo_sid: OptionalNullable[str] = UNSET
    """The SID of the document that includes the logo that will appear in the LOA. To upload documents follow the
    following guide:
    https://www.twilio.com/docs/phone-numbers/regulatory/getting-started/create-new-bundle-public-rest-apis#supporting-document-create"""

    friendly_name: OptionalNullable[str] = UNSET
    """This is the string that you assigned as a friendly name for describing the creation of the configuration."""

    product: OptionalNullable[str] = UNSET
    """The product or service for which is requesting the signature."""

    country: OptionalNullable[str] = UNSET
    """The country ISO code to apply the configuration."""

    email_subject: OptionalNullable[str] = UNSET
    """Subject of the email that the end client will receive ex: “Twilio Hosting Request”, maximum length of 255
    characters."""

    email_message: OptionalNullable[str] = UNSET
    """Content of the email that the end client will receive ex: “This is a Hosting request from Twilio, please check
    the document and sign it”, maximum length of 5,000 characters."""

    url_redirection: OptionalNullable[str] = UNSET
    """Url the end client will be redirected after signing a document."""

    url: OptionalNullable[str] = UNSET


class NumbersV1SigningRequestConfigurationDict(TypedDict):
    logo_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    product: NotRequired[str | None]
    country: NotRequired[str | None]
    email_subject: NotRequired[str | None]
    email_message: NotRequired[str | None]
    url_redirection: NotRequired[str | None]
    url: NotRequired[str | None]
