from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api_v2010_account_message import ApiV2010AccountMessage
from ..models.enums.message_enum_address_retention import MessageEnumAddressRetentionOrStr
from ..models.enums.message_enum_content_retention import MessageEnumContentRetentionOrStr
from ..models.enums.message_enum_risk_check import MessageEnumRiskCheckOrStr
from ..models.enums.message_enum_schedule_type import MessageEnumScheduleTypeOrStr
from ..models.enums.message_enum_traffic_type import MessageEnumTrafficTypeOrStr
from ..models.enums.message_enum_update_status import MessageEnumUpdateStatusOrStr
from ..models.list_message_response import ListMessageResponse
from ..server.server import Server


class Api20100401Message:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401MessageWithRawResponse(client, server, auth)

    def create_message(
        self,
        account_sid: str,
        to: str,
        *,
        status_callback: str | None = None,
        application_sid: str | None = None,
        max_price: float | None = None,
        provide_feedback: bool | None = None,
        attempt: int | None = None,
        validity_period: int | None = None,
        force_delivery: bool | None = None,
        content_retention: MessageEnumContentRetentionOrStr | None = None,
        address_retention: MessageEnumAddressRetentionOrStr | None = None,
        smart_encoded: bool | None = None,
        persistent_action: list[str] | None = None,
        traffic_type: MessageEnumTrafficTypeOrStr | None = None,
        shorten_urls: bool | None = None,
        schedule_type: MessageEnumScheduleTypeOrStr | None = None,
        send_at: RFC3339DateTime | None = None,
        send_as_mms: bool | None = None,
        content_variables: str | None = None,
        risk_check: MessageEnumRiskCheckOrStr | None = None,
        from_: str | None = None,
        fallback_from: str | None = None,
        messaging_service_sid: str | None = None,
        body: str | None = None,
        media_url: list[str] | None = None,
        content_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountMessage:
        """Send a message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ creating the Message
                resource.
            to: The recipient's phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (for
                SMS/MMS) or `channel address <https://www.twilio.com/docs/messaging/channels>`__, e.g.
                ``whatsapp:+15552229999``.
            status_callback: The URL of the endpoint to which Twilio sends `Message status callback requests
                <https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url>`__. URL
                must contain a valid hostname and underscores are not allowed. If you include this parameter with the
                ``messaging_service_sid``, Twilio uses this URL instead of the Status Callback URL of the `Messaging
                Service <https://www.twilio.com/docs/messaging/api/service-resource>`__.
            application_sid: The SID of the associated `TwiML Application
                <https://www.twilio.com/docs/usage/api/applications>`__. `Message status callback requests
                <https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url>`__ are
                sent to the TwiML App's ``message_status_callback`` URL. Note that the ``status_callback`` parameter of
                a request takes priority over the ``application_sid`` parameter; if both are included
                ``application_sid`` is ignored.
            max_price: [OBSOLETE] This parameter will no longer have any effect as of 2024-06-03.
            provide_feedback: Boolean indicating whether or not you intend to provide delivery confirmation feedback to
                Twilio (used in conjunction with the `Message Feedback subresource
                <https://www.twilio.com/docs/sms/api/message-feedback-resource>`__). Default value is ``false``.
            attempt: Total number of attempts made (including this request) to send the message regardless of the
                provider used
            validity_period: The maximum length in seconds that the Message can remain in Twilio's outgoing message
                queue. If a queued Message exceeds the ``validity_period``, the Message is not sent. Accepted values are
                integers from ``1`` to ``36000``. Default value is ``36000``. A ``validity_period`` greater than ``5``
                is recommended. `Learn more about the validity period
                <https://www.twilio.com/blog/take-more-control-of-outbound-messages-using-validity-period-html>`__
            force_delivery: Reserved
            content_retention: Determines if the message content can be stored or redacted based on privacy settings
            address_retention: Determines if the address can be stored or obfuscated based on privacy settings
            smart_encoded: Whether to detect Unicode characters that have a similar GSM-7 character and replace them.
                Can be: ``true`` or ``false``.
            persistent_action: Rich actions for non-SMS/MMS channels. Used for `sending location in WhatsApp messages
                <https://www.twilio.com/docs/whatsapp/message-features#location-messages-with-whatsapp>`__.
            traffic_type: Value sent with the request.
            shorten_urls: For Messaging Services with `Link Shortening configured
                <https://www.twilio.com/docs/messaging/features/link-shortening>`__ only: A Boolean indicating whether
                or not Twilio should shorten links in the ``body`` of the Message. Default value is ``false``. If
                ``true``, the ``messaging_service_sid`` parameter must also be provided.
            schedule_type: For Messaging Services only: Include this parameter with a value of ``fixed`` in conjuction
                with the ``send_time`` parameter in order to `schedule a Message
                <https://www.twilio.com/docs/messaging/features/message-scheduling>`__.
            send_at: The time that Twilio will send the message. Must be in ISO 8601 format.
            send_as_mms: If set to ``true``, Twilio delivers the message as a single MMS message, regardless of the
                presence of media.
            content_variables: For `Content Editor/API <https://www.twilio.com/docs/content>`__ only: Key-value pairs of
                `Template variables <https://www.twilio.com/docs/content/using-variables-with-content-api>`__ and their
                substitution values. ``content_sid`` parameter must also be provided. If values are not defined in the
                ``content_variables`` parameter, the `Template's default placeholder values
                <https://www.twilio.com/docs/content/content-api-resources#create-templates>`__ are used.
            risk_check: Include this parameter with a value of ``disable`` to skip any kind of risk check on the
                respective message request.
            from_: The sender's Twilio phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format),
                `alphanumeric sender ID <https://www.twilio.com/docs/sms/quickstart>`__, `Wireless SIM
                <https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands>`__,
                `short code <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, or `channel address
                <https://www.twilio.com/docs/messaging/channels>`__ (e.g., ``whatsapp:+15554449999``). The value of the
                ``from`` parameter must be a sender that is hosted within Twilio and belongs to the Account creating the
                Message. If you are using ``messaging_service_sid``, this parameter can be empty (Twilio assigns a
                ``from`` value from the Messaging Service's Sender Pool) or you can provide a specific sender from your
                Sender Pool.
            fallback_from: A fallback SMS sender to use when the recipient cannot be reached over RCS. This parameter
                may only be used when also providing a `Messaging Service
                <https://twilio.com/docs/messaging/services>`__ containing an RCS sender. The fallback SMS sender must
                be either a Twilio phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format),
                `alphanumeric sender ID <https://www.twilio.com/docs/sms/quickstart>`__, or `short code
                <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, hosted within Twilio and belong to
                the Account creating the Message.
            messaging_service_sid: The SID of the `Messaging Service <https://www.twilio.com/docs/messaging/services>`__
                you want to associate with the Message. When this parameter is provided and the ``from`` parameter is
                omitted, Twilio selects the optimal sender from the Messaging Service's Sender Pool. You may also
                provide a ``from`` parameter if you want to use a specific Sender from the Sender Pool.
            body: The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the
                ``body`` contains more than 160 `GSM-7
                <https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding>`__ characters (or 70 `UCS-2
                <https://www.twilio.com/docs/glossary/what-is-ucs-2-character-encoding>`__ characters), the message is
                segmented and charged accordingly. For long ``body`` text, consider using the `send_as_mms parameter
                <https://www.twilio.com/blog/mms-for-long-text-messages>`__.
            media_url: The URL of media to include in the Message content. ``jpeg``, ``jpg``, ``gif``, and ``png`` file
                types are fully supported by Twilio and content is formatted for delivery on destination devices. The
                media size limit is 5 MB for supported file types (``jpeg``, ``jpg``, ``png``, ``gif``) and 500 KB for
                `other types <https://www.twilio.com/docs/messaging/guides/accepted-mime-types>`__ of accepted media. To
                send more than one image in the message, provide multiple ``media_url`` parameters in the POST request.
                You can include up to ten ``media_url`` parameters per message. `International
                <https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages>`__ and
                `carrier
                <https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada->`__
                limits apply.
            content_sid: For `Content Editor/API <https://www.twilio.com/docs/content>`__ only: The SID of the Content
                Template to be used with the Message, e.g., ``HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX``. If this parameter is not
                provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For
                Content API users, the SID is found in Twilio's response when `creating the Template
                <https://www.twilio.com/docs/content/content-api-resources#create-templates>`__ or by `fetching your
                Templates <https://www.twilio.com/docs/content/content-api-resources#fetch-all-content-resources>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_message(
            account_sid,
            to,
            status_callback=status_callback,
            application_sid=application_sid,
            max_price=max_price,
            provide_feedback=provide_feedback,
            attempt=attempt,
            validity_period=validity_period,
            force_delivery=force_delivery,
            content_retention=content_retention,
            address_retention=address_retention,
            smart_encoded=smart_encoded,
            persistent_action=persistent_action,
            traffic_type=traffic_type,
            shorten_urls=shorten_urls,
            schedule_type=schedule_type,
            send_at=send_at,
            send_as_mms=send_as_mms,
            content_variables=content_variables,
            risk_check=risk_check,
            from_=from_,
            fallback_from=fallback_from,
            messaging_service_sid=messaging_service_sid,
            body=body,
            media_url=media_url,
            content_sid=content_sid,
            request_options=request_options,
        ).unwrap()

    def delete_message(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a Message resource from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource
            sid: The SID of the Message resource you wish to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_message(account_sid, sid, request_options=request_options).unwrap()

    def fetch_message(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountMessage:
        """Fetch a specific Message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource
            sid: The SID of the Message resource to be fetched
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_message(account_sid, sid, request_options=request_options).unwrap()

    def list_message(
        self,
        account_sid: str,
        *,
        to: str | None = None,
        from_: str | None = None,
        date_sent: RFC3339DateTime | None = None,
        date_sent_query: RFC3339DateTime | None = None,
        date_sent_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMessageResponse:
        """Retrieve a list of Message resources associated with a Twilio Account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resources.
            to: Filter by recipient. For example: Set this parameter to ``+15558881111`` to retrieve a list of Message
                resources sent to ``+15558881111``.
            from_: Filter by sender. For example: Set this parameter to ``+15552229999`` to retrieve a list of Message
                resources sent by ``+15552229999``.
            date_sent: Filter by Message ``sent_date``. Accepts GMT dates in the following formats: ``YYYY-MM-DD`` (to
                find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with ``sent_date``s on
                and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with ``sent_dates`` on and after a
                specific date).
            date_sent_query: Filter by Message ``sent_date``. Accepts GMT dates in the following formats: ``YYYY-MM-DD``
                (to find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with ``sent_date``s
                on and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with ``sent_dates`` on and after
                a specific date).
            date_sent_query_query: Filter by Message ``sent_date``. Accepts GMT dates in the following formats:
                ``YYYY-MM-DD`` (to find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with
                ``sent_date``s on and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with
                ``sent_dates`` on and after a specific date).
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_message(
            account_sid,
            to=to,
            from_=from_,
            date_sent=date_sent,
            date_sent_query=date_sent_query,
            date_sent_query_query=date_sent_query_query,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_message(
        self,
        account_sid: str,
        sid: str,
        *,
        body: str | None = None,
        status: MessageEnumUpdateStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountMessage:
        """Update a Message resource (used to redact Message ``body`` text and to cancel not-yet-sent messages)

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Message resources to update.
            sid: The SID of the Message resource to be updated
            body: The new ``body`` of the Message resource. To redact the text content of a Message, this parameter's
                value must be an empty string
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_message(
            account_sid, sid, body=body, status=status, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401MessageWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Message:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401MessageWithRawResponse(client, server, auth)

    async def create_message(
        self,
        account_sid: str,
        to: str,
        *,
        status_callback: str | None = None,
        application_sid: str | None = None,
        max_price: float | None = None,
        provide_feedback: bool | None = None,
        attempt: int | None = None,
        validity_period: int | None = None,
        force_delivery: bool | None = None,
        content_retention: MessageEnumContentRetentionOrStr | None = None,
        address_retention: MessageEnumAddressRetentionOrStr | None = None,
        smart_encoded: bool | None = None,
        persistent_action: list[str] | None = None,
        traffic_type: MessageEnumTrafficTypeOrStr | None = None,
        shorten_urls: bool | None = None,
        schedule_type: MessageEnumScheduleTypeOrStr | None = None,
        send_at: RFC3339DateTime | None = None,
        send_as_mms: bool | None = None,
        content_variables: str | None = None,
        risk_check: MessageEnumRiskCheckOrStr | None = None,
        from_: str | None = None,
        fallback_from: str | None = None,
        messaging_service_sid: str | None = None,
        body: str | None = None,
        media_url: list[str] | None = None,
        content_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountMessage:
        """Send a message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ creating the Message
                resource.
            to: The recipient's phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (for
                SMS/MMS) or `channel address <https://www.twilio.com/docs/messaging/channels>`__, e.g.
                ``whatsapp:+15552229999``.
            status_callback: The URL of the endpoint to which Twilio sends `Message status callback requests
                <https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url>`__. URL
                must contain a valid hostname and underscores are not allowed. If you include this parameter with the
                ``messaging_service_sid``, Twilio uses this URL instead of the Status Callback URL of the `Messaging
                Service <https://www.twilio.com/docs/messaging/api/service-resource>`__.
            application_sid: The SID of the associated `TwiML Application
                <https://www.twilio.com/docs/usage/api/applications>`__. `Message status callback requests
                <https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url>`__ are
                sent to the TwiML App's ``message_status_callback`` URL. Note that the ``status_callback`` parameter of
                a request takes priority over the ``application_sid`` parameter; if both are included
                ``application_sid`` is ignored.
            max_price: [OBSOLETE] This parameter will no longer have any effect as of 2024-06-03.
            provide_feedback: Boolean indicating whether or not you intend to provide delivery confirmation feedback to
                Twilio (used in conjunction with the `Message Feedback subresource
                <https://www.twilio.com/docs/sms/api/message-feedback-resource>`__). Default value is ``false``.
            attempt: Total number of attempts made (including this request) to send the message regardless of the
                provider used
            validity_period: The maximum length in seconds that the Message can remain in Twilio's outgoing message
                queue. If a queued Message exceeds the ``validity_period``, the Message is not sent. Accepted values are
                integers from ``1`` to ``36000``. Default value is ``36000``. A ``validity_period`` greater than ``5``
                is recommended. `Learn more about the validity period
                <https://www.twilio.com/blog/take-more-control-of-outbound-messages-using-validity-period-html>`__
            force_delivery: Reserved
            content_retention: Determines if the message content can be stored or redacted based on privacy settings
            address_retention: Determines if the address can be stored or obfuscated based on privacy settings
            smart_encoded: Whether to detect Unicode characters that have a similar GSM-7 character and replace them.
                Can be: ``true`` or ``false``.
            persistent_action: Rich actions for non-SMS/MMS channels. Used for `sending location in WhatsApp messages
                <https://www.twilio.com/docs/whatsapp/message-features#location-messages-with-whatsapp>`__.
            traffic_type: Value sent with the request.
            shorten_urls: For Messaging Services with `Link Shortening configured
                <https://www.twilio.com/docs/messaging/features/link-shortening>`__ only: A Boolean indicating whether
                or not Twilio should shorten links in the ``body`` of the Message. Default value is ``false``. If
                ``true``, the ``messaging_service_sid`` parameter must also be provided.
            schedule_type: For Messaging Services only: Include this parameter with a value of ``fixed`` in conjuction
                with the ``send_time`` parameter in order to `schedule a Message
                <https://www.twilio.com/docs/messaging/features/message-scheduling>`__.
            send_at: The time that Twilio will send the message. Must be in ISO 8601 format.
            send_as_mms: If set to ``true``, Twilio delivers the message as a single MMS message, regardless of the
                presence of media.
            content_variables: For `Content Editor/API <https://www.twilio.com/docs/content>`__ only: Key-value pairs of
                `Template variables <https://www.twilio.com/docs/content/using-variables-with-content-api>`__ and their
                substitution values. ``content_sid`` parameter must also be provided. If values are not defined in the
                ``content_variables`` parameter, the `Template's default placeholder values
                <https://www.twilio.com/docs/content/content-api-resources#create-templates>`__ are used.
            risk_check: Include this parameter with a value of ``disable`` to skip any kind of risk check on the
                respective message request.
            from_: The sender's Twilio phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format),
                `alphanumeric sender ID <https://www.twilio.com/docs/sms/quickstart>`__, `Wireless SIM
                <https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands>`__,
                `short code <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, or `channel address
                <https://www.twilio.com/docs/messaging/channels>`__ (e.g., ``whatsapp:+15554449999``). The value of the
                ``from`` parameter must be a sender that is hosted within Twilio and belongs to the Account creating the
                Message. If you are using ``messaging_service_sid``, this parameter can be empty (Twilio assigns a
                ``from`` value from the Messaging Service's Sender Pool) or you can provide a specific sender from your
                Sender Pool.
            fallback_from: A fallback SMS sender to use when the recipient cannot be reached over RCS. This parameter
                may only be used when also providing a `Messaging Service
                <https://twilio.com/docs/messaging/services>`__ containing an RCS sender. The fallback SMS sender must
                be either a Twilio phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format),
                `alphanumeric sender ID <https://www.twilio.com/docs/sms/quickstart>`__, or `short code
                <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, hosted within Twilio and belong to
                the Account creating the Message.
            messaging_service_sid: The SID of the `Messaging Service <https://www.twilio.com/docs/messaging/services>`__
                you want to associate with the Message. When this parameter is provided and the ``from`` parameter is
                omitted, Twilio selects the optimal sender from the Messaging Service's Sender Pool. You may also
                provide a ``from`` parameter if you want to use a specific Sender from the Sender Pool.
            body: The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the
                ``body`` contains more than 160 `GSM-7
                <https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding>`__ characters (or 70 `UCS-2
                <https://www.twilio.com/docs/glossary/what-is-ucs-2-character-encoding>`__ characters), the message is
                segmented and charged accordingly. For long ``body`` text, consider using the `send_as_mms parameter
                <https://www.twilio.com/blog/mms-for-long-text-messages>`__.
            media_url: The URL of media to include in the Message content. ``jpeg``, ``jpg``, ``gif``, and ``png`` file
                types are fully supported by Twilio and content is formatted for delivery on destination devices. The
                media size limit is 5 MB for supported file types (``jpeg``, ``jpg``, ``png``, ``gif``) and 500 KB for
                `other types <https://www.twilio.com/docs/messaging/guides/accepted-mime-types>`__ of accepted media. To
                send more than one image in the message, provide multiple ``media_url`` parameters in the POST request.
                You can include up to ten ``media_url`` parameters per message. `International
                <https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages>`__ and
                `carrier
                <https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada->`__
                limits apply.
            content_sid: For `Content Editor/API <https://www.twilio.com/docs/content>`__ only: The SID of the Content
                Template to be used with the Message, e.g., ``HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX``. If this parameter is not
                provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For
                Content API users, the SID is found in Twilio's response when `creating the Template
                <https://www.twilio.com/docs/content/content-api-resources#create-templates>`__ or by `fetching your
                Templates <https://www.twilio.com/docs/content/content-api-resources#fetch-all-content-resources>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_message(
                account_sid,
                to,
                status_callback=status_callback,
                application_sid=application_sid,
                max_price=max_price,
                provide_feedback=provide_feedback,
                attempt=attempt,
                validity_period=validity_period,
                force_delivery=force_delivery,
                content_retention=content_retention,
                address_retention=address_retention,
                smart_encoded=smart_encoded,
                persistent_action=persistent_action,
                traffic_type=traffic_type,
                shorten_urls=shorten_urls,
                schedule_type=schedule_type,
                send_at=send_at,
                send_as_mms=send_as_mms,
                content_variables=content_variables,
                risk_check=risk_check,
                from_=from_,
                fallback_from=fallback_from,
                messaging_service_sid=messaging_service_sid,
                body=body,
                media_url=media_url,
                content_sid=content_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_message(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a Message resource from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource
            sid: The SID of the Message resource you wish to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_message(account_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_message(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountMessage:
        """Fetch a specific Message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource
            sid: The SID of the Message resource to be fetched
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_message(account_sid, sid, request_options=request_options)).unwrap()

    async def list_message(
        self,
        account_sid: str,
        *,
        to: str | None = None,
        from_: str | None = None,
        date_sent: RFC3339DateTime | None = None,
        date_sent_query: RFC3339DateTime | None = None,
        date_sent_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMessageResponse:
        """Retrieve a list of Message resources associated with a Twilio Account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resources.
            to: Filter by recipient. For example: Set this parameter to ``+15558881111`` to retrieve a list of Message
                resources sent to ``+15558881111``.
            from_: Filter by sender. For example: Set this parameter to ``+15552229999`` to retrieve a list of Message
                resources sent by ``+15552229999``.
            date_sent: Filter by Message ``sent_date``. Accepts GMT dates in the following formats: ``YYYY-MM-DD`` (to
                find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with ``sent_date``s on
                and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with ``sent_dates`` on and after a
                specific date).
            date_sent_query: Filter by Message ``sent_date``. Accepts GMT dates in the following formats: ``YYYY-MM-DD``
                (to find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with ``sent_date``s
                on and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with ``sent_dates`` on and after
                a specific date).
            date_sent_query_query: Filter by Message ``sent_date``. Accepts GMT dates in the following formats:
                ``YYYY-MM-DD`` (to find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with
                ``sent_date``s on and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with
                ``sent_dates`` on and after a specific date).
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_message(
                account_sid,
                to=to,
                from_=from_,
                date_sent=date_sent,
                date_sent_query=date_sent_query,
                date_sent_query_query=date_sent_query_query,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_message(
        self,
        account_sid: str,
        sid: str,
        *,
        body: str | None = None,
        status: MessageEnumUpdateStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountMessage:
        """Update a Message resource (used to redact Message ``body`` text and to cancel not-yet-sent messages)

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Message resources to update.
            sid: The SID of the Message resource to be updated
            body: The new ``body`` of the Message resource. To redact the text content of a Message, this parameter's
                value must be an empty string
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_message(
                account_sid, sid, body=body, status=status, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401MessageWithRawResponse:
        return self._with_raw_response


class Api20100401MessageWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_message(
        self,
        account_sid: str,
        to: str,
        *,
        status_callback: str | None = None,
        application_sid: str | None = None,
        max_price: float | None = None,
        provide_feedback: bool | None = None,
        attempt: int | None = None,
        validity_period: int | None = None,
        force_delivery: bool | None = None,
        content_retention: MessageEnumContentRetentionOrStr | None = None,
        address_retention: MessageEnumAddressRetentionOrStr | None = None,
        smart_encoded: bool | None = None,
        persistent_action: list[str] | None = None,
        traffic_type: MessageEnumTrafficTypeOrStr | None = None,
        shorten_urls: bool | None = None,
        schedule_type: MessageEnumScheduleTypeOrStr | None = None,
        send_at: RFC3339DateTime | None = None,
        send_as_mms: bool | None = None,
        content_variables: str | None = None,
        risk_check: MessageEnumRiskCheckOrStr | None = None,
        from_: str | None = None,
        fallback_from: str | None = None,
        messaging_service_sid: str | None = None,
        body: str | None = None,
        media_url: list[str] | None = None,
        content_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountMessage, RawError]:
        """Send a message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ creating the Message
                resource.
            to: The recipient's phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (for
                SMS/MMS) or `channel address <https://www.twilio.com/docs/messaging/channels>`__, e.g.
                ``whatsapp:+15552229999``.
            status_callback: The URL of the endpoint to which Twilio sends `Message status callback requests
                <https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url>`__. URL
                must contain a valid hostname and underscores are not allowed. If you include this parameter with the
                ``messaging_service_sid``, Twilio uses this URL instead of the Status Callback URL of the `Messaging
                Service <https://www.twilio.com/docs/messaging/api/service-resource>`__.
            application_sid: The SID of the associated `TwiML Application
                <https://www.twilio.com/docs/usage/api/applications>`__. `Message status callback requests
                <https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url>`__ are
                sent to the TwiML App's ``message_status_callback`` URL. Note that the ``status_callback`` parameter of
                a request takes priority over the ``application_sid`` parameter; if both are included
                ``application_sid`` is ignored.
            max_price: [OBSOLETE] This parameter will no longer have any effect as of 2024-06-03.
            provide_feedback: Boolean indicating whether or not you intend to provide delivery confirmation feedback to
                Twilio (used in conjunction with the `Message Feedback subresource
                <https://www.twilio.com/docs/sms/api/message-feedback-resource>`__). Default value is ``false``.
            attempt: Total number of attempts made (including this request) to send the message regardless of the
                provider used
            validity_period: The maximum length in seconds that the Message can remain in Twilio's outgoing message
                queue. If a queued Message exceeds the ``validity_period``, the Message is not sent. Accepted values are
                integers from ``1`` to ``36000``. Default value is ``36000``. A ``validity_period`` greater than ``5``
                is recommended. `Learn more about the validity period
                <https://www.twilio.com/blog/take-more-control-of-outbound-messages-using-validity-period-html>`__
            force_delivery: Reserved
            content_retention: Determines if the message content can be stored or redacted based on privacy settings
            address_retention: Determines if the address can be stored or obfuscated based on privacy settings
            smart_encoded: Whether to detect Unicode characters that have a similar GSM-7 character and replace them.
                Can be: ``true`` or ``false``.
            persistent_action: Rich actions for non-SMS/MMS channels. Used for `sending location in WhatsApp messages
                <https://www.twilio.com/docs/whatsapp/message-features#location-messages-with-whatsapp>`__.
            traffic_type: Value sent with the request.
            shorten_urls: For Messaging Services with `Link Shortening configured
                <https://www.twilio.com/docs/messaging/features/link-shortening>`__ only: A Boolean indicating whether
                or not Twilio should shorten links in the ``body`` of the Message. Default value is ``false``. If
                ``true``, the ``messaging_service_sid`` parameter must also be provided.
            schedule_type: For Messaging Services only: Include this parameter with a value of ``fixed`` in conjuction
                with the ``send_time`` parameter in order to `schedule a Message
                <https://www.twilio.com/docs/messaging/features/message-scheduling>`__.
            send_at: The time that Twilio will send the message. Must be in ISO 8601 format.
            send_as_mms: If set to ``true``, Twilio delivers the message as a single MMS message, regardless of the
                presence of media.
            content_variables: For `Content Editor/API <https://www.twilio.com/docs/content>`__ only: Key-value pairs of
                `Template variables <https://www.twilio.com/docs/content/using-variables-with-content-api>`__ and their
                substitution values. ``content_sid`` parameter must also be provided. If values are not defined in the
                ``content_variables`` parameter, the `Template's default placeholder values
                <https://www.twilio.com/docs/content/content-api-resources#create-templates>`__ are used.
            risk_check: Include this parameter with a value of ``disable`` to skip any kind of risk check on the
                respective message request.
            from_: The sender's Twilio phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format),
                `alphanumeric sender ID <https://www.twilio.com/docs/sms/quickstart>`__, `Wireless SIM
                <https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands>`__,
                `short code <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, or `channel address
                <https://www.twilio.com/docs/messaging/channels>`__ (e.g., ``whatsapp:+15554449999``). The value of the
                ``from`` parameter must be a sender that is hosted within Twilio and belongs to the Account creating the
                Message. If you are using ``messaging_service_sid``, this parameter can be empty (Twilio assigns a
                ``from`` value from the Messaging Service's Sender Pool) or you can provide a specific sender from your
                Sender Pool.
            fallback_from: A fallback SMS sender to use when the recipient cannot be reached over RCS. This parameter
                may only be used when also providing a `Messaging Service
                <https://twilio.com/docs/messaging/services>`__ containing an RCS sender. The fallback SMS sender must
                be either a Twilio phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format),
                `alphanumeric sender ID <https://www.twilio.com/docs/sms/quickstart>`__, or `short code
                <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, hosted within Twilio and belong to
                the Account creating the Message.
            messaging_service_sid: The SID of the `Messaging Service <https://www.twilio.com/docs/messaging/services>`__
                you want to associate with the Message. When this parameter is provided and the ``from`` parameter is
                omitted, Twilio selects the optimal sender from the Messaging Service's Sender Pool. You may also
                provide a ``from`` parameter if you want to use a specific Sender from the Sender Pool.
            body: The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the
                ``body`` contains more than 160 `GSM-7
                <https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding>`__ characters (or 70 `UCS-2
                <https://www.twilio.com/docs/glossary/what-is-ucs-2-character-encoding>`__ characters), the message is
                segmented and charged accordingly. For long ``body`` text, consider using the `send_as_mms parameter
                <https://www.twilio.com/blog/mms-for-long-text-messages>`__.
            media_url: The URL of media to include in the Message content. ``jpeg``, ``jpg``, ``gif``, and ``png`` file
                types are fully supported by Twilio and content is formatted for delivery on destination devices. The
                media size limit is 5 MB for supported file types (``jpeg``, ``jpg``, ``png``, ``gif``) and 500 KB for
                `other types <https://www.twilio.com/docs/messaging/guides/accepted-mime-types>`__ of accepted media. To
                send more than one image in the message, provide multiple ``media_url`` parameters in the POST request.
                You can include up to ten ``media_url`` parameters per message. `International
                <https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages>`__ and
                `carrier
                <https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada->`__
                limits apply.
            content_sid: For `Content Editor/API <https://www.twilio.com/docs/content>`__ only: The SID of the Content
                Template to be used with the Message, e.g., ``HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX``. If this parameter is not
                provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For
                Content API users, the SID is found in Twilio's response when `creating the Template
                <https://www.twilio.com/docs/content/content-api-resources#create-templates>`__ or by `fetching your
                Templates <https://www.twilio.com/docs/content/content-api-resources#fetch-all-content-resources>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("To", to),
                    param[str | None]("StatusCallback", status_callback),
                    param[str | None]("ApplicationSid", application_sid),
                    param[float | None]("MaxPrice", max_price),
                    param[bool | None]("ProvideFeedback", provide_feedback),
                    param[int | None]("Attempt", attempt),
                    param[int | None]("ValidityPeriod", validity_period),
                    param[bool | None]("ForceDelivery", force_delivery),
                    param[MessageEnumContentRetentionOrStr | None]("ContentRetention", content_retention),
                    param[MessageEnumAddressRetentionOrStr | None]("AddressRetention", address_retention),
                    param[bool | None]("SmartEncoded", smart_encoded),
                    param[list[str] | None]("PersistentAction", persistent_action),
                    param[MessageEnumTrafficTypeOrStr | None]("TrafficType", traffic_type),
                    param[bool | None]("ShortenUrls", shorten_urls),
                    param[MessageEnumScheduleTypeOrStr | None]("ScheduleType", schedule_type),
                    param[RFC3339DateTime | None]("SendAt", send_at),
                    param[bool | None]("SendAsMms", send_as_mms),
                    param[str | None]("ContentVariables", content_variables),
                    param[MessageEnumRiskCheckOrStr | None]("RiskCheck", risk_check),
                    param[str | None]("From", from_),
                    param[str | None]("FallbackFrom", fallback_from),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[str | None]("Body", body),
                    param[list[str] | None]("MediaUrl", media_url),
                    param[str | None]("ContentSid", content_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_message(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a Message resource from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource
            sid: The SID of the Message resource you wish to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_message(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountMessage, RawError]:
        """Fetch a specific Message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource
            sid: The SID of the Message resource to be fetched
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_message(
        self,
        account_sid: str,
        *,
        to: str | None = None,
        from_: str | None = None,
        date_sent: RFC3339DateTime | None = None,
        date_sent_query: RFC3339DateTime | None = None,
        date_sent_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMessageResponse, RawError]:
        """Retrieve a list of Message resources associated with a Twilio Account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resources.
            to: Filter by recipient. For example: Set this parameter to ``+15558881111`` to retrieve a list of Message
                resources sent to ``+15558881111``.
            from_: Filter by sender. For example: Set this parameter to ``+15552229999`` to retrieve a list of Message
                resources sent by ``+15552229999``.
            date_sent: Filter by Message ``sent_date``. Accepts GMT dates in the following formats: ``YYYY-MM-DD`` (to
                find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with ``sent_date``s on
                and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with ``sent_dates`` on and after a
                specific date).
            date_sent_query: Filter by Message ``sent_date``. Accepts GMT dates in the following formats: ``YYYY-MM-DD``
                (to find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with ``sent_date``s
                on and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with ``sent_dates`` on and after
                a specific date).
            date_sent_query_query: Filter by Message ``sent_date``. Accepts GMT dates in the following formats:
                ``YYYY-MM-DD`` (to find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with
                ``sent_date``s on and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with
                ``sent_dates`` on and after a specific date).
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("To", to),
                param[str | None]("From", from_),
                param[RFC3339DateTime | None]("DateSent", date_sent),
                param[RFC3339DateTime | None]("DateSent<", date_sent_query),
                param[RFC3339DateTime | None]("DateSent>", date_sent_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMessageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_message(
        self,
        account_sid: str,
        sid: str,
        *,
        body: str | None = None,
        status: MessageEnumUpdateStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountMessage, RawError]:
        """Update a Message resource (used to redact Message ``body`` text and to cancel not-yet-sent messages)

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Message resources to update.
            sid: The SID of the Message resource to be updated
            body: The new ``body`` of the Message resource. To redact the text content of a Message, this parameter's
                value must be an empty string
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str | None]("Body", body), param[MessageEnumUpdateStatusOrStr | None]("Status", status)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401MessageWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_message(
        self,
        account_sid: str,
        to: str,
        *,
        status_callback: str | None = None,
        application_sid: str | None = None,
        max_price: float | None = None,
        provide_feedback: bool | None = None,
        attempt: int | None = None,
        validity_period: int | None = None,
        force_delivery: bool | None = None,
        content_retention: MessageEnumContentRetentionOrStr | None = None,
        address_retention: MessageEnumAddressRetentionOrStr | None = None,
        smart_encoded: bool | None = None,
        persistent_action: list[str] | None = None,
        traffic_type: MessageEnumTrafficTypeOrStr | None = None,
        shorten_urls: bool | None = None,
        schedule_type: MessageEnumScheduleTypeOrStr | None = None,
        send_at: RFC3339DateTime | None = None,
        send_as_mms: bool | None = None,
        content_variables: str | None = None,
        risk_check: MessageEnumRiskCheckOrStr | None = None,
        from_: str | None = None,
        fallback_from: str | None = None,
        messaging_service_sid: str | None = None,
        body: str | None = None,
        media_url: list[str] | None = None,
        content_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountMessage, RawError]:
        """Send a message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ creating the Message
                resource.
            to: The recipient's phone number in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__ format (for
                SMS/MMS) or `channel address <https://www.twilio.com/docs/messaging/channels>`__, e.g.
                ``whatsapp:+15552229999``.
            status_callback: The URL of the endpoint to which Twilio sends `Message status callback requests
                <https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url>`__. URL
                must contain a valid hostname and underscores are not allowed. If you include this parameter with the
                ``messaging_service_sid``, Twilio uses this URL instead of the Status Callback URL of the `Messaging
                Service <https://www.twilio.com/docs/messaging/api/service-resource>`__.
            application_sid: The SID of the associated `TwiML Application
                <https://www.twilio.com/docs/usage/api/applications>`__. `Message status callback requests
                <https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url>`__ are
                sent to the TwiML App's ``message_status_callback`` URL. Note that the ``status_callback`` parameter of
                a request takes priority over the ``application_sid`` parameter; if both are included
                ``application_sid`` is ignored.
            max_price: [OBSOLETE] This parameter will no longer have any effect as of 2024-06-03.
            provide_feedback: Boolean indicating whether or not you intend to provide delivery confirmation feedback to
                Twilio (used in conjunction with the `Message Feedback subresource
                <https://www.twilio.com/docs/sms/api/message-feedback-resource>`__). Default value is ``false``.
            attempt: Total number of attempts made (including this request) to send the message regardless of the
                provider used
            validity_period: The maximum length in seconds that the Message can remain in Twilio's outgoing message
                queue. If a queued Message exceeds the ``validity_period``, the Message is not sent. Accepted values are
                integers from ``1`` to ``36000``. Default value is ``36000``. A ``validity_period`` greater than ``5``
                is recommended. `Learn more about the validity period
                <https://www.twilio.com/blog/take-more-control-of-outbound-messages-using-validity-period-html>`__
            force_delivery: Reserved
            content_retention: Determines if the message content can be stored or redacted based on privacy settings
            address_retention: Determines if the address can be stored or obfuscated based on privacy settings
            smart_encoded: Whether to detect Unicode characters that have a similar GSM-7 character and replace them.
                Can be: ``true`` or ``false``.
            persistent_action: Rich actions for non-SMS/MMS channels. Used for `sending location in WhatsApp messages
                <https://www.twilio.com/docs/whatsapp/message-features#location-messages-with-whatsapp>`__.
            traffic_type: Value sent with the request.
            shorten_urls: For Messaging Services with `Link Shortening configured
                <https://www.twilio.com/docs/messaging/features/link-shortening>`__ only: A Boolean indicating whether
                or not Twilio should shorten links in the ``body`` of the Message. Default value is ``false``. If
                ``true``, the ``messaging_service_sid`` parameter must also be provided.
            schedule_type: For Messaging Services only: Include this parameter with a value of ``fixed`` in conjuction
                with the ``send_time`` parameter in order to `schedule a Message
                <https://www.twilio.com/docs/messaging/features/message-scheduling>`__.
            send_at: The time that Twilio will send the message. Must be in ISO 8601 format.
            send_as_mms: If set to ``true``, Twilio delivers the message as a single MMS message, regardless of the
                presence of media.
            content_variables: For `Content Editor/API <https://www.twilio.com/docs/content>`__ only: Key-value pairs of
                `Template variables <https://www.twilio.com/docs/content/using-variables-with-content-api>`__ and their
                substitution values. ``content_sid`` parameter must also be provided. If values are not defined in the
                ``content_variables`` parameter, the `Template's default placeholder values
                <https://www.twilio.com/docs/content/content-api-resources#create-templates>`__ are used.
            risk_check: Include this parameter with a value of ``disable`` to skip any kind of risk check on the
                respective message request.
            from_: The sender's Twilio phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format),
                `alphanumeric sender ID <https://www.twilio.com/docs/sms/quickstart>`__, `Wireless SIM
                <https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands>`__,
                `short code <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, or `channel address
                <https://www.twilio.com/docs/messaging/channels>`__ (e.g., ``whatsapp:+15554449999``). The value of the
                ``from`` parameter must be a sender that is hosted within Twilio and belongs to the Account creating the
                Message. If you are using ``messaging_service_sid``, this parameter can be empty (Twilio assigns a
                ``from`` value from the Messaging Service's Sender Pool) or you can provide a specific sender from your
                Sender Pool.
            fallback_from: A fallback SMS sender to use when the recipient cannot be reached over RCS. This parameter
                may only be used when also providing a `Messaging Service
                <https://twilio.com/docs/messaging/services>`__ containing an RCS sender. The fallback SMS sender must
                be either a Twilio phone number (in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format),
                `alphanumeric sender ID <https://www.twilio.com/docs/sms/quickstart>`__, or `short code
                <https://www.twilio.com/en-us/messaging/channels/sms/short-codes>`__, hosted within Twilio and belong to
                the Account creating the Message.
            messaging_service_sid: The SID of the `Messaging Service <https://www.twilio.com/docs/messaging/services>`__
                you want to associate with the Message. When this parameter is provided and the ``from`` parameter is
                omitted, Twilio selects the optimal sender from the Messaging Service's Sender Pool. You may also
                provide a ``from`` parameter if you want to use a specific Sender from the Sender Pool.
            body: The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the
                ``body`` contains more than 160 `GSM-7
                <https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding>`__ characters (or 70 `UCS-2
                <https://www.twilio.com/docs/glossary/what-is-ucs-2-character-encoding>`__ characters), the message is
                segmented and charged accordingly. For long ``body`` text, consider using the `send_as_mms parameter
                <https://www.twilio.com/blog/mms-for-long-text-messages>`__.
            media_url: The URL of media to include in the Message content. ``jpeg``, ``jpg``, ``gif``, and ``png`` file
                types are fully supported by Twilio and content is formatted for delivery on destination devices. The
                media size limit is 5 MB for supported file types (``jpeg``, ``jpg``, ``png``, ``gif``) and 500 KB for
                `other types <https://www.twilio.com/docs/messaging/guides/accepted-mime-types>`__ of accepted media. To
                send more than one image in the message, provide multiple ``media_url`` parameters in the POST request.
                You can include up to ten ``media_url`` parameters per message. `International
                <https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages>`__ and
                `carrier
                <https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada->`__
                limits apply.
            content_sid: For `Content Editor/API <https://www.twilio.com/docs/content>`__ only: The SID of the Content
                Template to be used with the Message, e.g., ``HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX``. If this parameter is not
                provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For
                Content API users, the SID is found in Twilio's response when `creating the Template
                <https://www.twilio.com/docs/content/content-api-resources#create-templates>`__ or by `fetching your
                Templates <https://www.twilio.com/docs/content/content-api-resources#fetch-all-content-resources>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("To", to),
                    param[str | None]("StatusCallback", status_callback),
                    param[str | None]("ApplicationSid", application_sid),
                    param[float | None]("MaxPrice", max_price),
                    param[bool | None]("ProvideFeedback", provide_feedback),
                    param[int | None]("Attempt", attempt),
                    param[int | None]("ValidityPeriod", validity_period),
                    param[bool | None]("ForceDelivery", force_delivery),
                    param[MessageEnumContentRetentionOrStr | None]("ContentRetention", content_retention),
                    param[MessageEnumAddressRetentionOrStr | None]("AddressRetention", address_retention),
                    param[bool | None]("SmartEncoded", smart_encoded),
                    param[list[str] | None]("PersistentAction", persistent_action),
                    param[MessageEnumTrafficTypeOrStr | None]("TrafficType", traffic_type),
                    param[bool | None]("ShortenUrls", shorten_urls),
                    param[MessageEnumScheduleTypeOrStr | None]("ScheduleType", schedule_type),
                    param[RFC3339DateTime | None]("SendAt", send_at),
                    param[bool | None]("SendAsMms", send_as_mms),
                    param[str | None]("ContentVariables", content_variables),
                    param[MessageEnumRiskCheckOrStr | None]("RiskCheck", risk_check),
                    param[str | None]("From", from_),
                    param[str | None]("FallbackFrom", fallback_from),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[str | None]("Body", body),
                    param[list[str] | None]("MediaUrl", media_url),
                    param[str | None]("ContentSid", content_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_message(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a Message resource from your account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource
            sid: The SID of the Message resource you wish to delete
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_message(
        self, account_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountMessage, RawError]:
        """Fetch a specific Message

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resource
            sid: The SID of the Message resource to be fetched
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_message(
        self,
        account_sid: str,
        *,
        to: str | None = None,
        from_: str | None = None,
        date_sent: RFC3339DateTime | None = None,
        date_sent_query: RFC3339DateTime | None = None,
        date_sent_query_query: RFC3339DateTime | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMessageResponse, RawError]:
        """Retrieve a list of Message resources associated with a Twilio Account

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ associated with the
                Message resources.
            to: Filter by recipient. For example: Set this parameter to ``+15558881111`` to retrieve a list of Message
                resources sent to ``+15558881111``.
            from_: Filter by sender. For example: Set this parameter to ``+15552229999`` to retrieve a list of Message
                resources sent by ``+15552229999``.
            date_sent: Filter by Message ``sent_date``. Accepts GMT dates in the following formats: ``YYYY-MM-DD`` (to
                find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with ``sent_date``s on
                and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with ``sent_dates`` on and after a
                specific date).
            date_sent_query: Filter by Message ``sent_date``. Accepts GMT dates in the following formats: ``YYYY-MM-DD``
                (to find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with ``sent_date``s
                on and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with ``sent_dates`` on and after
                a specific date).
            date_sent_query_query: Filter by Message ``sent_date``. Accepts GMT dates in the following formats:
                ``YYYY-MM-DD`` (to find Messages with a specific ``sent_date``), ``<=YYYY-MM-DD`` (to find Messages with
                ``sent_date``s on and before a specific date), and ``>=YYYY-MM-DD`` (to find Messages with
                ``sent_dates`` on and after a specific date).
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            query_params=[
                param[str | None]("To", to),
                param[str | None]("From", from_),
                param[RFC3339DateTime | None]("DateSent", date_sent),
                param[RFC3339DateTime | None]("DateSent<", date_sent_query),
                param[RFC3339DateTime | None]("DateSent>", date_sent_query_query),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListMessageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_message(
        self,
        account_sid: str,
        sid: str,
        *,
        body: str | None = None,
        status: MessageEnumUpdateStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountMessage, RawError]:
        """Update a Message resource (used to redact Message ``body`` text and to cancel not-yet-sent messages)

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that created the
                Message resources to update.
            sid: The SID of the Message resource to be updated
            body: The new ``body`` of the Message resource. To redact the text content of a Message, this parameter's
                value must be an empty string
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json"),
            path_params=[param[str]("AccountSid", account_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [param[str | None]("Body", body), param[MessageEnumUpdateStatusOrStr | None]("Status", status)]
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
