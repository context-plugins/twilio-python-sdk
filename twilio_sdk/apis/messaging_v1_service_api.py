from __future__ import annotations

from pydantic import AnyUrl

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from ..models.enums.service_enum_scan_message_content import ServiceEnumScanMessageContentOrStr
from ..models.list_service_response import ListServiceResponse
from ..models.messaging_v1_service import MessagingV1Service
from ..server.server import Server


class MessagingV1ServiceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1ServiceApiWithRawResponse(client, server, auth)

    def create_service(
        self,
        friendly_name: str,
        *,
        inbound_request_url: AnyUrl | None = None,
        inbound_method: AmdStatusCallbackMethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        sticky_sender: bool | None = None,
        mms_converter: bool | None = None,
        smart_encoding: bool | None = None,
        scan_message_content: ServiceEnumScanMessageContentOrStr | None = None,
        fallback_to_long_code: bool | None = None,
        area_code_geomatch: bool | None = None,
        validity_period: int | None = None,
        synchronous_validation: bool | None = None,
        usecase: str | None = None,
        use_inbound_webhook_on_number: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1Service:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            inbound_request_url: The URL we call using ``inbound_method`` when a message is received by any phone number
                or short code in the Service. When this property is ``null``, receiving inbound messages is disabled.
                All messages sent to the Twilio phone number or short code will not be logged and received on the
                Account. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on the
                phone number will override the ``inbound_request_url`` defined for the Messaging Service.
            inbound_method: The HTTP method we should use to call ``inbound_request_url``. Can be ``GET`` or ``POST``
                and the default is ``POST``.
            fallback_url: The URL that we call using ``fallback_method`` if an error occurs while retrieving or
                executing the TwiML from the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is
                enabled then the webhook url defined on the phone number will override the ``fallback_url`` defined for
                the Messaging Service.
            fallback_method: The HTTP method we should use to call ``fallback_url``. Can be: ``GET`` or ``POST``.
            status_callback: The URL we should call to `pass status updates
                <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery.
            sticky_sender: Whether to enable `Sticky Sender
                <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service instance.
            mms_converter: Whether to enable the `MMS Converter
                <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for messages sent through the Service
                instance.
            smart_encoding: Whether to enable `Smart Encoding
                <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages sent through the Service
                instance.
            scan_message_content: Reserved.
            fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short
                code message failures.
            area_code_geomatch: Whether to enable `Area Code Geomatch
                <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on the Service Instance.
            validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from
                ``1`` to ``36,000``. Default value is ``36,000``.
            synchronous_validation: Reserved.
            usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values
                are ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``.
            use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone
                number will be used or ``inbound_request_url``/``fallback_url`` url will be called when a message is
                received from the phone number. If this field is enabled then the webhook url defined on the phone
                number will override the ``inbound_request_url``/``fallback_url`` defined for the Messaging Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service(
            friendly_name,
            inbound_request_url=inbound_request_url,
            inbound_method=inbound_method,
            fallback_url=fallback_url,
            fallback_method=fallback_method,
            status_callback=status_callback,
            sticky_sender=sticky_sender,
            mms_converter=mms_converter,
            smart_encoding=smart_encoding,
            scan_message_content=scan_message_content,
            fallback_to_long_code=fallback_to_long_code,
            area_code_geomatch=area_code_geomatch,
            validity_period=validity_period,
            synchronous_validation=synchronous_validation,
            usecase=usecase,
            use_inbound_webhook_on_number=use_inbound_webhook_on_number,
            request_options=request_options,
        ).unwrap()

    def delete_service(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service(sid, request_options=request_options).unwrap()

    def fetch_service(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> MessagingV1Service:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service(sid, request_options=request_options).unwrap()

    def list_service(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_service(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        inbound_request_url: AnyUrl | None = None,
        inbound_method: AmdStatusCallbackMethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        sticky_sender: bool | None = None,
        mms_converter: bool | None = None,
        smart_encoding: bool | None = None,
        scan_message_content: ServiceEnumScanMessageContentOrStr | None = None,
        fallback_to_long_code: bool | None = None,
        area_code_geomatch: bool | None = None,
        validity_period: int | None = None,
        synchronous_validation: bool | None = None,
        usecase: str | None = None,
        use_inbound_webhook_on_number: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1Service:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            inbound_request_url: The URL we call using ``inbound_method`` when a message is received by any phone number
                or short code in the Service. When this property is ``null``, receiving inbound messages is disabled.
                All messages sent to the Twilio phone number or short code will not be logged and received on the
                Account. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on the
                phone number will override the ``inbound_request_url`` defined for the Messaging Service.
            inbound_method: The HTTP method we should use to call ``inbound_request_url``. Can be ``GET`` or ``POST``
                and the default is ``POST``.
            fallback_url: The URL that we call using ``fallback_method`` if an error occurs while retrieving or
                executing the TwiML from the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is
                enabled then the webhook url defined on the phone number will override the ``fallback_url`` defined for
                the Messaging Service.
            fallback_method: The HTTP method we should use to call ``fallback_url``. Can be: ``GET`` or ``POST``.
            status_callback: The URL we should call to `pass status updates
                <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery.
            sticky_sender: Whether to enable `Sticky Sender
                <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service instance.
            mms_converter: Whether to enable the `MMS Converter
                <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for messages sent through the Service
                instance.
            smart_encoding: Whether to enable `Smart Encoding
                <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages sent through the Service
                instance.
            scan_message_content: Reserved.
            fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short
                code message failures.
            area_code_geomatch: Whether to enable `Area Code Geomatch
                <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on the Service Instance.
            validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from
                ``1`` to ``36,000``. Default value is ``36,000``.
            synchronous_validation: Reserved.
            usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values
                are ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``.
            use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone
                number will be used or ``inbound_request_url``/``fallback_url`` url will be called when a message is
                received from the phone number. If this field is enabled then the webhook url defined on the phone
                number will override the ``inbound_request_url``/``fallback_url`` defined for the Messaging Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service(
            sid,
            friendly_name=friendly_name,
            inbound_request_url=inbound_request_url,
            inbound_method=inbound_method,
            fallback_url=fallback_url,
            fallback_method=fallback_method,
            status_callback=status_callback,
            sticky_sender=sticky_sender,
            mms_converter=mms_converter,
            smart_encoding=smart_encoding,
            scan_message_content=scan_message_content,
            fallback_to_long_code=fallback_to_long_code,
            area_code_geomatch=area_code_geomatch,
            validity_period=validity_period,
            synchronous_validation=synchronous_validation,
            usecase=usecase,
            use_inbound_webhook_on_number=use_inbound_webhook_on_number,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1ServiceApiWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1ServiceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1ServiceApiWithRawResponse(client, server, auth)

    async def create_service(
        self,
        friendly_name: str,
        *,
        inbound_request_url: AnyUrl | None = None,
        inbound_method: AmdStatusCallbackMethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        sticky_sender: bool | None = None,
        mms_converter: bool | None = None,
        smart_encoding: bool | None = None,
        scan_message_content: ServiceEnumScanMessageContentOrStr | None = None,
        fallback_to_long_code: bool | None = None,
        area_code_geomatch: bool | None = None,
        validity_period: int | None = None,
        synchronous_validation: bool | None = None,
        usecase: str | None = None,
        use_inbound_webhook_on_number: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1Service:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            inbound_request_url: The URL we call using ``inbound_method`` when a message is received by any phone number
                or short code in the Service. When this property is ``null``, receiving inbound messages is disabled.
                All messages sent to the Twilio phone number or short code will not be logged and received on the
                Account. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on the
                phone number will override the ``inbound_request_url`` defined for the Messaging Service.
            inbound_method: The HTTP method we should use to call ``inbound_request_url``. Can be ``GET`` or ``POST``
                and the default is ``POST``.
            fallback_url: The URL that we call using ``fallback_method`` if an error occurs while retrieving or
                executing the TwiML from the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is
                enabled then the webhook url defined on the phone number will override the ``fallback_url`` defined for
                the Messaging Service.
            fallback_method: The HTTP method we should use to call ``fallback_url``. Can be: ``GET`` or ``POST``.
            status_callback: The URL we should call to `pass status updates
                <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery.
            sticky_sender: Whether to enable `Sticky Sender
                <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service instance.
            mms_converter: Whether to enable the `MMS Converter
                <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for messages sent through the Service
                instance.
            smart_encoding: Whether to enable `Smart Encoding
                <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages sent through the Service
                instance.
            scan_message_content: Reserved.
            fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short
                code message failures.
            area_code_geomatch: Whether to enable `Area Code Geomatch
                <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on the Service Instance.
            validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from
                ``1`` to ``36,000``. Default value is ``36,000``.
            synchronous_validation: Reserved.
            usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values
                are ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``.
            use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone
                number will be used or ``inbound_request_url``/``fallback_url`` url will be called when a message is
                received from the phone number. If this field is enabled then the webhook url defined on the phone
                number will override the ``inbound_request_url``/``fallback_url`` defined for the Messaging Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service(
                friendly_name,
                inbound_request_url=inbound_request_url,
                inbound_method=inbound_method,
                fallback_url=fallback_url,
                fallback_method=fallback_method,
                status_callback=status_callback,
                sticky_sender=sticky_sender,
                mms_converter=mms_converter,
                smart_encoding=smart_encoding,
                scan_message_content=scan_message_content,
                fallback_to_long_code=fallback_to_long_code,
                area_code_geomatch=area_code_geomatch,
                validity_period=validity_period,
                synchronous_validation=synchronous_validation,
                usecase=usecase,
                use_inbound_webhook_on_number=use_inbound_webhook_on_number,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_service(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_service(sid, request_options=request_options)).unwrap()

    async def fetch_service(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MessagingV1Service:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_service(sid, request_options=request_options)).unwrap()

    async def list_service(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceResponse:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_service(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        inbound_request_url: AnyUrl | None = None,
        inbound_method: AmdStatusCallbackMethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        sticky_sender: bool | None = None,
        mms_converter: bool | None = None,
        smart_encoding: bool | None = None,
        scan_message_content: ServiceEnumScanMessageContentOrStr | None = None,
        fallback_to_long_code: bool | None = None,
        area_code_geomatch: bool | None = None,
        validity_period: int | None = None,
        synchronous_validation: bool | None = None,
        usecase: str | None = None,
        use_inbound_webhook_on_number: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MessagingV1Service:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            inbound_request_url: The URL we call using ``inbound_method`` when a message is received by any phone number
                or short code in the Service. When this property is ``null``, receiving inbound messages is disabled.
                All messages sent to the Twilio phone number or short code will not be logged and received on the
                Account. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on the
                phone number will override the ``inbound_request_url`` defined for the Messaging Service.
            inbound_method: The HTTP method we should use to call ``inbound_request_url``. Can be ``GET`` or ``POST``
                and the default is ``POST``.
            fallback_url: The URL that we call using ``fallback_method`` if an error occurs while retrieving or
                executing the TwiML from the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is
                enabled then the webhook url defined on the phone number will override the ``fallback_url`` defined for
                the Messaging Service.
            fallback_method: The HTTP method we should use to call ``fallback_url``. Can be: ``GET`` or ``POST``.
            status_callback: The URL we should call to `pass status updates
                <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery.
            sticky_sender: Whether to enable `Sticky Sender
                <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service instance.
            mms_converter: Whether to enable the `MMS Converter
                <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for messages sent through the Service
                instance.
            smart_encoding: Whether to enable `Smart Encoding
                <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages sent through the Service
                instance.
            scan_message_content: Reserved.
            fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short
                code message failures.
            area_code_geomatch: Whether to enable `Area Code Geomatch
                <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on the Service Instance.
            validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from
                ``1`` to ``36,000``. Default value is ``36,000``.
            synchronous_validation: Reserved.
            usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values
                are ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``.
            use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone
                number will be used or ``inbound_request_url``/``fallback_url`` url will be called when a message is
                received from the phone number. If this field is enabled then the webhook url defined on the phone
                number will override the ``inbound_request_url``/``fallback_url`` defined for the Messaging Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service(
                sid,
                friendly_name=friendly_name,
                inbound_request_url=inbound_request_url,
                inbound_method=inbound_method,
                fallback_url=fallback_url,
                fallback_method=fallback_method,
                status_callback=status_callback,
                sticky_sender=sticky_sender,
                mms_converter=mms_converter,
                smart_encoding=smart_encoding,
                scan_message_content=scan_message_content,
                fallback_to_long_code=fallback_to_long_code,
                area_code_geomatch=area_code_geomatch,
                validity_period=validity_period,
                synchronous_validation=synchronous_validation,
                usecase=usecase,
                use_inbound_webhook_on_number=use_inbound_webhook_on_number,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1ServiceApiWithRawResponse:
        return self._with_raw_response


class MessagingV1ServiceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_service(
        self,
        friendly_name: str,
        *,
        inbound_request_url: AnyUrl | None = None,
        inbound_method: AmdStatusCallbackMethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        sticky_sender: bool | None = None,
        mms_converter: bool | None = None,
        smart_encoding: bool | None = None,
        scan_message_content: ServiceEnumScanMessageContentOrStr | None = None,
        fallback_to_long_code: bool | None = None,
        area_code_geomatch: bool | None = None,
        validity_period: int | None = None,
        synchronous_validation: bool | None = None,
        usecase: str | None = None,
        use_inbound_webhook_on_number: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1Service, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            inbound_request_url: The URL we call using ``inbound_method`` when a message is received by any phone number
                or short code in the Service. When this property is ``null``, receiving inbound messages is disabled.
                All messages sent to the Twilio phone number or short code will not be logged and received on the
                Account. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on the
                phone number will override the ``inbound_request_url`` defined for the Messaging Service.
            inbound_method: The HTTP method we should use to call ``inbound_request_url``. Can be ``GET`` or ``POST``
                and the default is ``POST``.
            fallback_url: The URL that we call using ``fallback_method`` if an error occurs while retrieving or
                executing the TwiML from the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is
                enabled then the webhook url defined on the phone number will override the ``fallback_url`` defined for
                the Messaging Service.
            fallback_method: The HTTP method we should use to call ``fallback_url``. Can be: ``GET`` or ``POST``.
            status_callback: The URL we should call to `pass status updates
                <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery.
            sticky_sender: Whether to enable `Sticky Sender
                <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service instance.
            mms_converter: Whether to enable the `MMS Converter
                <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for messages sent through the Service
                instance.
            smart_encoding: Whether to enable `Smart Encoding
                <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages sent through the Service
                instance.
            scan_message_content: Reserved.
            fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short
                code message failures.
            area_code_geomatch: Whether to enable `Area Code Geomatch
                <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on the Service Instance.
            validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from
                ``1`` to ``36,000``. Default value is ``36,000``.
            synchronous_validation: Reserved.
            usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values
                are ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``.
            use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone
                number will be used or ``inbound_request_url``/``fallback_url`` url will be called when a message is
                received from the phone number. If this field is enabled then the webhook url defined on the phone
                number will override the ``inbound_request_url``/``fallback_url`` defined for the Messaging Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[AnyUrl | None]("InboundRequestUrl", inbound_request_url),
                    param[AmdStatusCallbackMethodOrStr | None]("InboundMethod", inbound_method),
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("FallbackMethod", fallback_method),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[bool | None]("StickySender", sticky_sender),
                    param[bool | None]("MmsConverter", mms_converter),
                    param[bool | None]("SmartEncoding", smart_encoding),
                    param[ServiceEnumScanMessageContentOrStr | None]("ScanMessageContent", scan_message_content),
                    param[bool | None]("FallbackToLongCode", fallback_to_long_code),
                    param[bool | None]("AreaCodeGeomatch", area_code_geomatch),
                    param[int | None]("ValidityPeriod", validity_period),
                    param[bool | None]("SynchronousValidation", synchronous_validation),
                    param[str | None]("Usecase", usecase),
                    param[bool | None]("UseInboundWebhookOnNumber", use_inbound_webhook_on_number),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1Service, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        inbound_request_url: AnyUrl | None = None,
        inbound_method: AmdStatusCallbackMethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        sticky_sender: bool | None = None,
        mms_converter: bool | None = None,
        smart_encoding: bool | None = None,
        scan_message_content: ServiceEnumScanMessageContentOrStr | None = None,
        fallback_to_long_code: bool | None = None,
        area_code_geomatch: bool | None = None,
        validity_period: int | None = None,
        synchronous_validation: bool | None = None,
        usecase: str | None = None,
        use_inbound_webhook_on_number: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1Service, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            inbound_request_url: The URL we call using ``inbound_method`` when a message is received by any phone number
                or short code in the Service. When this property is ``null``, receiving inbound messages is disabled.
                All messages sent to the Twilio phone number or short code will not be logged and received on the
                Account. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on the
                phone number will override the ``inbound_request_url`` defined for the Messaging Service.
            inbound_method: The HTTP method we should use to call ``inbound_request_url``. Can be ``GET`` or ``POST``
                and the default is ``POST``.
            fallback_url: The URL that we call using ``fallback_method`` if an error occurs while retrieving or
                executing the TwiML from the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is
                enabled then the webhook url defined on the phone number will override the ``fallback_url`` defined for
                the Messaging Service.
            fallback_method: The HTTP method we should use to call ``fallback_url``. Can be: ``GET`` or ``POST``.
            status_callback: The URL we should call to `pass status updates
                <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery.
            sticky_sender: Whether to enable `Sticky Sender
                <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service instance.
            mms_converter: Whether to enable the `MMS Converter
                <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for messages sent through the Service
                instance.
            smart_encoding: Whether to enable `Smart Encoding
                <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages sent through the Service
                instance.
            scan_message_content: Reserved.
            fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short
                code message failures.
            area_code_geomatch: Whether to enable `Area Code Geomatch
                <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on the Service Instance.
            validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from
                ``1`` to ``36,000``. Default value is ``36,000``.
            synchronous_validation: Reserved.
            usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values
                are ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``.
            use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone
                number will be used or ``inbound_request_url``/``fallback_url`` url will be called when a message is
                received from the phone number. If this field is enabled then the webhook url defined on the phone
                number will override the ``inbound_request_url``/``fallback_url`` defined for the Messaging Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[AnyUrl | None]("InboundRequestUrl", inbound_request_url),
                    param[AmdStatusCallbackMethodOrStr | None]("InboundMethod", inbound_method),
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("FallbackMethod", fallback_method),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[bool | None]("StickySender", sticky_sender),
                    param[bool | None]("MmsConverter", mms_converter),
                    param[bool | None]("SmartEncoding", smart_encoding),
                    param[ServiceEnumScanMessageContentOrStr | None]("ScanMessageContent", scan_message_content),
                    param[bool | None]("FallbackToLongCode", fallback_to_long_code),
                    param[bool | None]("AreaCodeGeomatch", area_code_geomatch),
                    param[int | None]("ValidityPeriod", validity_period),
                    param[bool | None]("SynchronousValidation", synchronous_validation),
                    param[str | None]("Usecase", usecase),
                    param[bool | None]("UseInboundWebhookOnNumber", use_inbound_webhook_on_number),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1ServiceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_service(
        self,
        friendly_name: str,
        *,
        inbound_request_url: AnyUrl | None = None,
        inbound_method: AmdStatusCallbackMethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        sticky_sender: bool | None = None,
        mms_converter: bool | None = None,
        smart_encoding: bool | None = None,
        scan_message_content: ServiceEnumScanMessageContentOrStr | None = None,
        fallback_to_long_code: bool | None = None,
        area_code_geomatch: bool | None = None,
        validity_period: int | None = None,
        synchronous_validation: bool | None = None,
        usecase: str | None = None,
        use_inbound_webhook_on_number: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1Service, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            inbound_request_url: The URL we call using ``inbound_method`` when a message is received by any phone number
                or short code in the Service. When this property is ``null``, receiving inbound messages is disabled.
                All messages sent to the Twilio phone number or short code will not be logged and received on the
                Account. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on the
                phone number will override the ``inbound_request_url`` defined for the Messaging Service.
            inbound_method: The HTTP method we should use to call ``inbound_request_url``. Can be ``GET`` or ``POST``
                and the default is ``POST``.
            fallback_url: The URL that we call using ``fallback_method`` if an error occurs while retrieving or
                executing the TwiML from the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is
                enabled then the webhook url defined on the phone number will override the ``fallback_url`` defined for
                the Messaging Service.
            fallback_method: The HTTP method we should use to call ``fallback_url``. Can be: ``GET`` or ``POST``.
            status_callback: The URL we should call to `pass status updates
                <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery.
            sticky_sender: Whether to enable `Sticky Sender
                <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service instance.
            mms_converter: Whether to enable the `MMS Converter
                <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for messages sent through the Service
                instance.
            smart_encoding: Whether to enable `Smart Encoding
                <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages sent through the Service
                instance.
            scan_message_content: Reserved.
            fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short
                code message failures.
            area_code_geomatch: Whether to enable `Area Code Geomatch
                <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on the Service Instance.
            validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from
                ``1`` to ``36,000``. Default value is ``36,000``.
            synchronous_validation: Reserved.
            usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values
                are ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``.
            use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone
                number will be used or ``inbound_request_url``/``fallback_url`` url will be called when a message is
                received from the phone number. If this field is enabled then the webhook url defined on the phone
                number will override the ``inbound_request_url``/``fallback_url`` defined for the Messaging Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services"),
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[AnyUrl | None]("InboundRequestUrl", inbound_request_url),
                    param[AmdStatusCallbackMethodOrStr | None]("InboundMethod", inbound_method),
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("FallbackMethod", fallback_method),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[bool | None]("StickySender", sticky_sender),
                    param[bool | None]("MmsConverter", mms_converter),
                    param[bool | None]("SmartEncoding", smart_encoding),
                    param[ServiceEnumScanMessageContentOrStr | None]("ScanMessageContent", scan_message_content),
                    param[bool | None]("FallbackToLongCode", fallback_to_long_code),
                    param[bool | None]("AreaCodeGeomatch", area_code_geomatch),
                    param[int | None]("ValidityPeriod", validity_period),
                    param[bool | None]("SynchronousValidation", synchronous_validation),
                    param[str | None]("Usecase", usecase),
                    param[bool | None]("UseInboundWebhookOnNumber", use_inbound_webhook_on_number),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1Service, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceResponse, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service(
        self,
        sid: str,
        *,
        friendly_name: str | None = None,
        inbound_request_url: AnyUrl | None = None,
        inbound_method: AmdStatusCallbackMethodOrStr | None = None,
        fallback_url: AnyUrl | None = None,
        fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback: AnyUrl | None = None,
        sticky_sender: bool | None = None,
        mms_converter: bool | None = None,
        smart_encoding: bool | None = None,
        scan_message_content: ServiceEnumScanMessageContentOrStr | None = None,
        fallback_to_long_code: bool | None = None,
        area_code_geomatch: bool | None = None,
        validity_period: int | None = None,
        synchronous_validation: bool | None = None,
        usecase: str | None = None,
        use_inbound_webhook_on_number: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MessagingV1Service, RawError]:
        """A Messaging Service resource to create, fetch, update, delete or add/remove senders from Messaging Services.

        Args:
            sid: The SID of the Service resource to update.
            friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters
                long.
            inbound_request_url: The URL we call using ``inbound_method`` when a message is received by any phone number
                or short code in the Service. When this property is ``null``, receiving inbound messages is disabled.
                All messages sent to the Twilio phone number or short code will not be logged and received on the
                Account. If the ``use_inbound_webhook_on_number`` field is enabled then the webhook url defined on the
                phone number will override the ``inbound_request_url`` defined for the Messaging Service.
            inbound_method: The HTTP method we should use to call ``inbound_request_url``. Can be ``GET`` or ``POST``
                and the default is ``POST``.
            fallback_url: The URL that we call using ``fallback_method`` if an error occurs while retrieving or
                executing the TwiML from the Inbound Request URL. If the ``use_inbound_webhook_on_number`` field is
                enabled then the webhook url defined on the phone number will override the ``fallback_url`` defined for
                the Messaging Service.
            fallback_method: The HTTP method we should use to call ``fallback_url``. Can be: ``GET`` or ``POST``.
            status_callback: The URL we should call to `pass status updates
                <https://www.twilio.com/docs/sms/api/message-resource#message-status-values>`__ about message delivery.
            sticky_sender: Whether to enable `Sticky Sender
                <https://www.twilio.com/docs/messaging/services#sticky-sender>`__ on the Service instance.
            mms_converter: Whether to enable the `MMS Converter
                <https://www.twilio.com/docs/messaging/services#mms-converter>`__ for messages sent through the Service
                instance.
            smart_encoding: Whether to enable `Smart Encoding
                <https://www.twilio.com/docs/messaging/services#smart-encoding>`__ for messages sent through the Service
                instance.
            scan_message_content: Reserved.
            fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short
                code message failures.
            area_code_geomatch: Whether to enable `Area Code Geomatch
                <https://www.twilio.com/docs/messaging/services#area-code-geomatch>`__ on the Service Instance.
            validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from
                ``1`` to ``36,000``. Default value is ``36,000``.
            synchronous_validation: Reserved.
            usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values
                are ``notifications``, ``marketing``, ``verification``, ``discussion``, ``poll``, ``undeclared``.
            use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone
                number will be used or ``inbound_request_url``/``fallback_url`` url will be called when a message is
                received from the phone number. If this field is enabled then the webhook url defined on the phone
                number will override the ``inbound_request_url``/``fallback_url`` defined for the Messaging Service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v1/Services/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[AnyUrl | None]("InboundRequestUrl", inbound_request_url),
                    param[AmdStatusCallbackMethodOrStr | None]("InboundMethod", inbound_method),
                    param[AnyUrl | None]("FallbackUrl", fallback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("FallbackMethod", fallback_method),
                    param[AnyUrl | None]("StatusCallback", status_callback),
                    param[bool | None]("StickySender", sticky_sender),
                    param[bool | None]("MmsConverter", mms_converter),
                    param[bool | None]("SmartEncoding", smart_encoding),
                    param[ServiceEnumScanMessageContentOrStr | None]("ScanMessageContent", scan_message_content),
                    param[bool | None]("FallbackToLongCode", fallback_to_long_code),
                    param[bool | None]("AreaCodeGeomatch", area_code_geomatch),
                    param[int | None]("ValidityPeriod", validity_period),
                    param[bool | None]("SynchronousValidation", synchronous_validation),
                    param[str | None]("Usecase", usecase),
                    param[bool | None]("UseInboundWebhookOnNumber", use_inbound_webhook_on_number),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1Service],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
