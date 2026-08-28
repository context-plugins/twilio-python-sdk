from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from .enums.service_enum_scan_message_content import ServiceEnumScanMessageContentOrStr


class MessagingV1Service(SdkBaseModel):
    sid: OptionalNullable[str] = UNSET
    """The unique string that we created to identify the Service resource."""

    account_sid: OptionalNullable[str] = UNSET
    """The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the Service resource."""

    friendly_name: OptionalNullable[str] = UNSET
    """The string that you assigned to describe the resource."""

    date_created: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was created specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    date_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time in GMT when the resource was last updated specified in `ISO 8601
    <https://en.wikipedia.org/wiki/ISO_8601>`__ format."""

    inbound_request_url: OptionalNullable[str] = UNSET
    """The URL we call using ``inbound_method`` when a message is received by any phone number or short code in the
    Service. When this property is ``null``, receiving inbound messages is disabled. All messages sent to the Twilio
    phone number or short code will not be logged and received on the Account. If the ``use_inbound_webhook_on_number``
    field is enabled then the webhook url defined on the phone number will override the ``inbound_request_url`` defined
    for the Messaging Service."""

    inbound_method: OptionalNullable[AmdStatusCallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``inbound_request_url``. Can be ``GET`` or ``POST``."""

    fallback_url: OptionalNullable[str] = UNSET
    """The URL that we call using ``fallback_method`` if an error occurs while retrieving or executing the TwiML from
    the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on
    the phone number will override the ``fallback_url`` defined for the Messaging Service."""

    fallback_method: OptionalNullable[AmdStatusCallbackMethodOrStr] = UNSET
    """The HTTP method we use to call ``fallback_url``. Can be: ``GET`` or ``POST``."""

    status_callback: OptionalNullable[str] = UNSET
    """The URL we call to `pass status updates
    <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery."""

    sticky_sender: OptionalNullable[bool] = UNSET
    """Whether to enable `Sticky Sender <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service
    instance."""

    mms_converter: OptionalNullable[bool] = UNSET
    """Whether to enable the `MMS Converter <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for
    messages sent through the Service instance."""

    smart_encoding: OptionalNullable[bool] = UNSET
    """Whether to enable `Smart Encoding <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages
    sent through the Service instance."""

    scan_message_content: Optional[ServiceEnumScanMessageContentOrStr] = UNSET
    """Reserved."""

    fallback_to_long_code: OptionalNullable[bool] = UNSET
    """[OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures."""

    area_code_geomatch: OptionalNullable[bool] = UNSET
    """Whether to enable `Area Code Geomatch <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on
    the Service Instance."""

    synchronous_validation: OptionalNullable[bool] = UNSET
    """Reserved."""

    validity_period: Optional[int] = UNSET
    """How long, in seconds, messages sent from the Service are valid. Can be an integer from ``1`` to ``36,000``.
    Default value is ``36,000``."""

    url: OptionalNullable[str] = UNSET
    """The absolute URL of the Service resource."""

    links: OptionalNullable[Any] = UNSET
    """The absolute URLs of related resources."""

    usecase: OptionalNullable[str] = UNSET
    """A string that describes the scenario in which the Messaging Service will be used. Possible values are
    ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``."""

    us_app_to_person_registered: OptionalNullable[bool] = UNSET
    """Whether US A2P campaign is registered for this Service."""

    use_inbound_webhook_on_number: OptionalNullable[bool] = UNSET
    """A boolean value that indicates either the webhook url configured on the phone number will be used or
    ``inbound_request_url``/``fallback_url`` url will be called when a message is received from the phone number. If
    this field is enabled then the webhook url defined on the phone number will override the
    ``inbound_request_url``/``fallback_url`` defined for the Messaging Service."""


class MessagingV1ServiceDict(TypedDict):
    sid: NotRequired[str | None]
    account_sid: NotRequired[str | None]
    friendly_name: NotRequired[str | None]
    date_created: NotRequired[RFC3339DateTime | None]
    date_updated: NotRequired[RFC3339DateTime | None]
    inbound_request_url: NotRequired[str | None]
    inbound_method: NotRequired[AmdStatusCallbackMethodOrStr | None]
    fallback_url: NotRequired[str | None]
    fallback_method: NotRequired[AmdStatusCallbackMethodOrStr | None]
    status_callback: NotRequired[str | None]
    sticky_sender: NotRequired[bool | None]
    mms_converter: NotRequired[bool | None]
    smart_encoding: NotRequired[bool | None]
    scan_message_content: NotRequired[ServiceEnumScanMessageContentOrStr]
    fallback_to_long_code: NotRequired[bool | None]
    area_code_geomatch: NotRequired[bool | None]
    synchronous_validation: NotRequired[bool | None]
    validity_period: NotRequired[int]
    url: NotRequired[str | None]
    links: NotRequired[Any | None]
    usecase: NotRequired[str | None]
    us_app_to_person_registered: NotRequired[bool | None]
    use_inbound_webhook_on_number: NotRequired[bool | None]
