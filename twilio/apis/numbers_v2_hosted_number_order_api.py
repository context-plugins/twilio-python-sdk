from __future__ import annotations

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
from ..models.enums.dependent_order_enum_status import DependentOrderEnumStatusOrStr
from ..models.list_hosted_number_order_response import ListHostedNumberOrderResponse
from ..models.numbers_v2_hosted_number_order import NumbersV2HostedNumberOrder
from ..server.server import Server


class NumbersV2HostedNumberOrderApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV2HostedNumberOrderApiWithRawResponse(client, server, auth)

    def create_hosted_number_order(
        self,
        phone_number: str,
        contact_phone_number: str,
        address_sid: str,
        email: str,
        *,
        account_sid: str | None = None,
        friendly_name: str | None = None,
        cc_emails: list[str] | None = None,
        sms_url: str | None = None,
        sms_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_capability: bool | None = None,
        sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_application_sid: str | None = None,
        contact_title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2HostedNumberOrder:
        """Host a phone number's capability on Twilio's platform.

        Args:
            phone_number: The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format
            contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
            address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents
                the address of the owner of this phone number.
            email: Optional. Email of the owner of this phone number that is being hosted.
            account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to
                specify a subaccount to add the HostedNumberOrder to.
            friendly_name: A 128 character string that is a human readable text that describes this resource.
            cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied
                to.
            sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be
                copied onto the IncomingPhoneNumber resource.
            sms_method: The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``.
                This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML
                defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
            sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
            sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either
                ``GET`` or ``POST``. This will be copied onto the IncomingPhoneNumber resource.
            status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
            status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
            sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS
                messages sent to this number. If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS
                urls above and use those set on the application.
            contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_hosted_number_order(
            phone_number,
            contact_phone_number,
            address_sid,
            email,
            account_sid=account_sid,
            friendly_name=friendly_name,
            cc_emails=cc_emails,
            sms_url=sms_url,
            sms_method=sms_method,
            sms_fallback_url=sms_fallback_url,
            sms_capability=sms_capability,
            sms_fallback_method=sms_fallback_method,
            status_callback_url=status_callback_url,
            status_callback_method=status_callback_method,
            sms_application_sid=sms_application_sid,
            contact_title=contact_title,
            request_options=request_options,
        ).unwrap()

    def delete_hosted_number_order(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Cancel the HostedNumberOrder (only available when the status is in ``received``).

        Args:
            sid: A 34 character string that uniquely identifies this HostedNumberOrder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_hosted_number_order(sid, request_options=request_options).unwrap()

    def fetch_hosted_number_order(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2HostedNumberOrder:
        """Fetch a specific HostedNumberOrder.

        Args:
            sid: A 34 character string that uniquely identifies this HostedNumberOrder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_hosted_number_order(sid, request_options=request_options).unwrap()

    def list_hosted_number_order(
        self,
        *,
        status: DependentOrderEnumStatusOrStr | None = None,
        sms_capability: bool | None = None,
        phone_number: str | None = None,
        incoming_phone_number_sid: str | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListHostedNumberOrderResponse:
        """Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

        Args:
            status: The Status of this HostedNumberOrder. One of ``received``, ``pending-verification``, ``verified``,
                ``pending-loa``, ``carrier-processing``, ``testing``, ``completed``, ``failed``, or ``action-required``.
            sms_capability: Whether the SMS capability will be hosted on our platform. Can be ``true`` of ``false``.
            phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
            incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource
                created by this HostedNumberOrder.
            friendly_name: A human readable description of this resource, up to 128 characters.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_hosted_number_order(
            status=status,
            sms_capability=sms_capability,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_hosted_number_order(
        self,
        sid: str,
        status: DependentOrderEnumStatusOrStr,
        *,
        verification_call_delay: int | None = None,
        verification_call_extension: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2HostedNumberOrder:
        """Updates a specific HostedNumberOrder.

        Args:
            sid: The SID of the HostedNumberOrder resource to update.
            status: Status of this resource. It can hold one of the values: 1. Twilio Processing 2. Received, 3. Pending
                LOA, 4. Carrier Processing, 5. Completed, 6. Action Required, 7. Failed. See the `HostedNumberOrders
                Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values>`__
                section for more information on each of these statuses.
            verification_call_delay: The number of seconds to wait before initiating the ownership verification call.
                Can be a value between 0 and 60, inclusive.
            verification_call_extension: The numerical extension to dial when making the ownership verification call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_hosted_number_order(
            sid,
            status,
            verification_call_delay=verification_call_delay,
            verification_call_extension=verification_call_extension,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV2HostedNumberOrderApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV2HostedNumberOrderApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV2HostedNumberOrderApiWithRawResponse(client, server, auth)

    async def create_hosted_number_order(
        self,
        phone_number: str,
        contact_phone_number: str,
        address_sid: str,
        email: str,
        *,
        account_sid: str | None = None,
        friendly_name: str | None = None,
        cc_emails: list[str] | None = None,
        sms_url: str | None = None,
        sms_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_capability: bool | None = None,
        sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_application_sid: str | None = None,
        contact_title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2HostedNumberOrder:
        """Host a phone number's capability on Twilio's platform.

        Args:
            phone_number: The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format
            contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
            address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents
                the address of the owner of this phone number.
            email: Optional. Email of the owner of this phone number that is being hosted.
            account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to
                specify a subaccount to add the HostedNumberOrder to.
            friendly_name: A 128 character string that is a human readable text that describes this resource.
            cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied
                to.
            sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be
                copied onto the IncomingPhoneNumber resource.
            sms_method: The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``.
                This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML
                defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
            sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
            sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either
                ``GET`` or ``POST``. This will be copied onto the IncomingPhoneNumber resource.
            status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
            status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
            sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS
                messages sent to this number. If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS
                urls above and use those set on the application.
            contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_hosted_number_order(
                phone_number,
                contact_phone_number,
                address_sid,
                email,
                account_sid=account_sid,
                friendly_name=friendly_name,
                cc_emails=cc_emails,
                sms_url=sms_url,
                sms_method=sms_method,
                sms_fallback_url=sms_fallback_url,
                sms_capability=sms_capability,
                sms_fallback_method=sms_fallback_method,
                status_callback_url=status_callback_url,
                status_callback_method=status_callback_method,
                sms_application_sid=sms_application_sid,
                contact_title=contact_title,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_hosted_number_order(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Cancel the HostedNumberOrder (only available when the status is in ``received``).

        Args:
            sid: A 34 character string that uniquely identifies this HostedNumberOrder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_hosted_number_order(sid, request_options=request_options)).unwrap()

    async def fetch_hosted_number_order(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV2HostedNumberOrder:
        """Fetch a specific HostedNumberOrder.

        Args:
            sid: A 34 character string that uniquely identifies this HostedNumberOrder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_hosted_number_order(sid, request_options=request_options)).unwrap()

    async def list_hosted_number_order(
        self,
        *,
        status: DependentOrderEnumStatusOrStr | None = None,
        sms_capability: bool | None = None,
        phone_number: str | None = None,
        incoming_phone_number_sid: str | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListHostedNumberOrderResponse:
        """Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

        Args:
            status: The Status of this HostedNumberOrder. One of ``received``, ``pending-verification``, ``verified``,
                ``pending-loa``, ``carrier-processing``, ``testing``, ``completed``, ``failed``, or ``action-required``.
            sms_capability: Whether the SMS capability will be hosted on our platform. Can be ``true`` of ``false``.
            phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
            incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource
                created by this HostedNumberOrder.
            friendly_name: A human readable description of this resource, up to 128 characters.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_hosted_number_order(
                status=status,
                sms_capability=sms_capability,
                phone_number=phone_number,
                incoming_phone_number_sid=incoming_phone_number_sid,
                friendly_name=friendly_name,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_hosted_number_order(
        self,
        sid: str,
        status: DependentOrderEnumStatusOrStr,
        *,
        verification_call_delay: int | None = None,
        verification_call_extension: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV2HostedNumberOrder:
        """Updates a specific HostedNumberOrder.

        Args:
            sid: The SID of the HostedNumberOrder resource to update.
            status: Status of this resource. It can hold one of the values: 1. Twilio Processing 2. Received, 3. Pending
                LOA, 4. Carrier Processing, 5. Completed, 6. Action Required, 7. Failed. See the `HostedNumberOrders
                Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values>`__
                section for more information on each of these statuses.
            verification_call_delay: The number of seconds to wait before initiating the ownership verification call.
                Can be a value between 0 and 60, inclusive.
            verification_call_extension: The numerical extension to dial when making the ownership verification call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_hosted_number_order(
                sid,
                status,
                verification_call_delay=verification_call_delay,
                verification_call_extension=verification_call_extension,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV2HostedNumberOrderApiWithRawResponse:
        return self._with_raw_response


class NumbersV2HostedNumberOrderApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_hosted_number_order(
        self,
        phone_number: str,
        contact_phone_number: str,
        address_sid: str,
        email: str,
        *,
        account_sid: str | None = None,
        friendly_name: str | None = None,
        cc_emails: list[str] | None = None,
        sms_url: str | None = None,
        sms_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_capability: bool | None = None,
        sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_application_sid: str | None = None,
        contact_title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2HostedNumberOrder, RawError]:
        """Host a phone number's capability on Twilio's platform.

        Args:
            phone_number: The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format
            contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
            address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents
                the address of the owner of this phone number.
            email: Optional. Email of the owner of this phone number that is being hosted.
            account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to
                specify a subaccount to add the HostedNumberOrder to.
            friendly_name: A 128 character string that is a human readable text that describes this resource.
            cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied
                to.
            sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be
                copied onto the IncomingPhoneNumber resource.
            sms_method: The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``.
                This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML
                defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
            sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
            sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either
                ``GET`` or ``POST``. This will be copied onto the IncomingPhoneNumber resource.
            status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
            status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
            sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS
                messages sent to this number. If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS
                urls above and use those set on the application.
            contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/HostedNumber/Orders"),
            body=form_body(
                [
                    param[str]("PhoneNumber", phone_number),
                    param[str]("ContactPhoneNumber", contact_phone_number),
                    param[str]("AddressSid", address_sid),
                    param[str]("Email", email),
                    param[str | None]("AccountSid", account_sid),
                    param[str | None]("FriendlyName", friendly_name),
                    param[list[str] | None]("CcEmails", cc_emails),
                    param[str | None]("SmsUrl", sms_url),
                    param[AmdStatusCallbackMethodOrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[bool | None]("SmsCapability", sms_capability),
                    param[AmdStatusCallbackMethodOrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("StatusCallbackUrl", status_callback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("SmsApplicationSid", sms_application_sid),
                    param[str | None]("ContactTitle", contact_title),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2HostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_hosted_number_order(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Cancel the HostedNumberOrder (only available when the status is in ``received``).

        Args:
            sid: A 34 character string that uniquely identifies this HostedNumberOrder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/HostedNumber/Orders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_hosted_number_order(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2HostedNumberOrder, RawError]:
        """Fetch a specific HostedNumberOrder.

        Args:
            sid: A 34 character string that uniquely identifies this HostedNumberOrder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/Orders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2HostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_hosted_number_order(
        self,
        *,
        status: DependentOrderEnumStatusOrStr | None = None,
        sms_capability: bool | None = None,
        phone_number: str | None = None,
        incoming_phone_number_sid: str | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListHostedNumberOrderResponse, RawError]:
        """Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

        Args:
            status: The Status of this HostedNumberOrder. One of ``received``, ``pending-verification``, ``verified``,
                ``pending-loa``, ``carrier-processing``, ``testing``, ``completed``, ``failed``, or ``action-required``.
            sms_capability: Whether the SMS capability will be hosted on our platform. Can be ``true`` of ``false``.
            phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
            incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource
                created by this HostedNumberOrder.
            friendly_name: A human readable description of this resource, up to 128 characters.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/Orders"),
            query_params=[
                param[DependentOrderEnumStatusOrStr | None]("Status", status),
                param[bool | None]("SmsCapability", sms_capability),
                param[str | None]("PhoneNumber", phone_number),
                param[str | None]("IncomingPhoneNumberSid", incoming_phone_number_sid),
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListHostedNumberOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_hosted_number_order(
        self,
        sid: str,
        status: DependentOrderEnumStatusOrStr,
        *,
        verification_call_delay: int | None = None,
        verification_call_extension: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2HostedNumberOrder, RawError]:
        """Updates a specific HostedNumberOrder.

        Args:
            sid: The SID of the HostedNumberOrder resource to update.
            status: Status of this resource. It can hold one of the values: 1. Twilio Processing 2. Received, 3. Pending
                LOA, 4. Carrier Processing, 5. Completed, 6. Action Required, 7. Failed. See the `HostedNumberOrders
                Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values>`__
                section for more information on each of these statuses.
            verification_call_delay: The number of seconds to wait before initiating the ownership verification call.
                Can be a value between 0 and 60, inclusive.
            verification_call_extension: The numerical extension to dial when making the ownership verification call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/HostedNumber/Orders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[DependentOrderEnumStatusOrStr]("Status", status),
                    param[int | None]("VerificationCallDelay", verification_call_delay),
                    param[str | None]("VerificationCallExtension", verification_call_extension),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2HostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV2HostedNumberOrderApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_hosted_number_order(
        self,
        phone_number: str,
        contact_phone_number: str,
        address_sid: str,
        email: str,
        *,
        account_sid: str | None = None,
        friendly_name: str | None = None,
        cc_emails: list[str] | None = None,
        sms_url: str | None = None,
        sms_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_capability: bool | None = None,
        sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_application_sid: str | None = None,
        contact_title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2HostedNumberOrder, RawError]:
        """Host a phone number's capability on Twilio's platform.

        Args:
            phone_number: The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format
            contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
            address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents
                the address of the owner of this phone number.
            email: Optional. Email of the owner of this phone number that is being hosted.
            account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to
                specify a subaccount to add the HostedNumberOrder to.
            friendly_name: A 128 character string that is a human readable text that describes this resource.
            cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied
                to.
            sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be
                copied onto the IncomingPhoneNumber resource.
            sms_method: The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``.
                This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML
                defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
            sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
            sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either
                ``GET`` or ``POST``. This will be copied onto the IncomingPhoneNumber resource.
            status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
            status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
            sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS
                messages sent to this number. If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS
                urls above and use those set on the application.
            contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/HostedNumber/Orders"),
            body=form_body(
                [
                    param[str]("PhoneNumber", phone_number),
                    param[str]("ContactPhoneNumber", contact_phone_number),
                    param[str]("AddressSid", address_sid),
                    param[str]("Email", email),
                    param[str | None]("AccountSid", account_sid),
                    param[str | None]("FriendlyName", friendly_name),
                    param[list[str] | None]("CcEmails", cc_emails),
                    param[str | None]("SmsUrl", sms_url),
                    param[AmdStatusCallbackMethodOrStr | None]("SmsMethod", sms_method),
                    param[str | None]("SmsFallbackUrl", sms_fallback_url),
                    param[bool | None]("SmsCapability", sms_capability),
                    param[AmdStatusCallbackMethodOrStr | None]("SmsFallbackMethod", sms_fallback_method),
                    param[str | None]("StatusCallbackUrl", status_callback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("StatusCallbackMethod", status_callback_method),
                    param[str | None]("SmsApplicationSid", sms_application_sid),
                    param[str | None]("ContactTitle", contact_title),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2HostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_hosted_number_order(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Cancel the HostedNumberOrder (only available when the status is in ``received``).

        Args:
            sid: A 34 character string that uniquely identifies this HostedNumberOrder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v2/HostedNumber/Orders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_hosted_number_order(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV2HostedNumberOrder, RawError]:
        """Fetch a specific HostedNumberOrder.

        Args:
            sid: A 34 character string that uniquely identifies this HostedNumberOrder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/Orders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2HostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_hosted_number_order(
        self,
        *,
        status: DependentOrderEnumStatusOrStr | None = None,
        sms_capability: bool | None = None,
        phone_number: str | None = None,
        incoming_phone_number_sid: str | None = None,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListHostedNumberOrderResponse, RawError]:
        """Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

        Args:
            status: The Status of this HostedNumberOrder. One of ``received``, ``pending-verification``, ``verified``,
                ``pending-loa``, ``carrier-processing``, ``testing``, ``completed``, ``failed``, or ``action-required``.
            sms_capability: Whether the SMS capability will be hosted on our platform. Can be ``true`` of ``false``.
            phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
            incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource
                created by this HostedNumberOrder.
            friendly_name: A human readable description of this resource, up to 128 characters.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v2/HostedNumber/Orders"),
            query_params=[
                param[DependentOrderEnumStatusOrStr | None]("Status", status),
                param[bool | None]("SmsCapability", sms_capability),
                param[str | None]("PhoneNumber", phone_number),
                param[str | None]("IncomingPhoneNumberSid", incoming_phone_number_sid),
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListHostedNumberOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_hosted_number_order(
        self,
        sid: str,
        status: DependentOrderEnumStatusOrStr,
        *,
        verification_call_delay: int | None = None,
        verification_call_extension: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV2HostedNumberOrder, RawError]:
        """Updates a specific HostedNumberOrder.

        Args:
            sid: The SID of the HostedNumberOrder resource to update.
            status: Status of this resource. It can hold one of the values: 1. Twilio Processing 2. Received, 3. Pending
                LOA, 4. Carrier Processing, 5. Completed, 6. Action Required, 7. Failed. See the `HostedNumberOrders
                Status Values
                <https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values>`__
                section for more information on each of these statuses.
            verification_call_delay: The number of seconds to wait before initiating the ownership verification call.
                Can be a value between 0 and 60, inclusive.
            verification_call_extension: The numerical extension to dial when making the ownership verification call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v2/HostedNumber/Orders/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            body=form_body(
                [
                    param[DependentOrderEnumStatusOrStr]("Status", status),
                    param[int | None]("VerificationCallDelay", verification_call_delay),
                    param[str | None]("VerificationCallExtension", verification_call_extension),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV2HostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
