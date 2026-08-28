from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class MessagingV1DomainConfig(SdkBaseModel):
    domain_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Domain resource."""

    config_sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Domain config (prefix ZK)."""

    fallback_url: OptionalNullable[str] = UNSET
    """Any requests we receive to this domain that do not match an existing shortened message will be redirected to the
    fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping."""

    callback_url: OptionalNullable[str] = UNSET
    """URL to receive click events to your webhook whenever the recipients click on the shortened links."""

    continue_on_failure: OptionalNullable[bool] = UNSET
    """Boolean field to set customer delivery preference when there is a failure in linkShortening service"""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """Date this Domain Config was created."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """Date that this Domain Config was last updated."""

    url: OptionalNullable[str] = UNSET
    disable_https: OptionalNullable[bool] = UNSET
    """Customer's choice to send links with/without "https://" attached to shortened url. If true, messages will not be
    sent with https:// at the beginning of the url. If false, messages will be sent with https:// at the beginning of
    the url. False is the default behavior if it is not specified."""


class MessagingV1DomainConfigDict(TypedDict):
    domain_sid: NotRequired[str | None]
    config_sid: NotRequired[str | None]
    fallback_url: NotRequired[str | None]
    callback_url: NotRequired[str | None]
    continue_on_failure: NotRequired[bool | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    url: NotRequired[str | None]
    disable_https: NotRequired[bool | None]
