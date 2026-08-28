from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.amd_status_callback_method import AmdStatusCallbackMethodOrStr
from ..models.enums.dependent_order_enum_verification_type import DependentOrderEnumVerificationTypeOrStr
from ..models.numbers_v3_hosted_numbers_hosted_number_order import NumbersV3HostedNumbersHostedNumberOrder
from ..server.server import Server


class NumbersV3HostedNumbersHostedNumberOrderApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV3HostedNumbersHostedNumberOrderApiWithRawResponse(client, server, auth)

    def create_hosted_numbers_hosted_number_order(
        self,
        phone_number: str,
        sms_capability: bool,
        *,
        account_sid: str | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        cc_emails: list[str] | None = None,
        sms_url: str | None = None,
        sms_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_application_sid: str | None = None,
        address_sid: str | None = None,
        email: str | None = None,
        verification_type: DependentOrderEnumVerificationTypeOrStr | None = None,
        verification_document_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV3HostedNumbersHostedNumberOrder:
        """Host a phone number's capability on Twilio's platform.

        Args:
            phone_number: The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format
            sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
            account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to
                specify a subaccount to add the HostedNumberOrder to.
            friendly_name: A 64 character string that is a human readable text that describes this resource.
            unique_name: Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder,
                assigned by the developer, to be optionally used in addition to SID.
            cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied
                to.
            sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be
                copied onto the IncomingPhoneNumber resource.
            sms_method: The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``.
                This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML
                defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either
                ``GET`` or ``POST``. This will be copied onto the IncomingPhoneNumber resource.
            status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
            status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
            sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS
                messages sent to this number. If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS
                urls above and use those set on the application.
            address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents
                the address of the owner of this phone number.
            email: Optional. Email of the owner of this phone number that is being hosted.
            verification_type: Value sent with the request.
            verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the
                document for verifying ownership of the number to be hosted. Required when VerificationType is
                phone-bill.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_hosted_numbers_hosted_number_order(
            phone_number,
            sms_capability,
            account_sid=account_sid,
            friendly_name=friendly_name,
            unique_name=unique_name,
            cc_emails=cc_emails,
            sms_url=sms_url,
            sms_method=sms_method,
            sms_fallback_url=sms_fallback_url,
            sms_fallback_method=sms_fallback_method,
            status_callback_url=status_callback_url,
            status_callback_method=status_callback_method,
            sms_application_sid=sms_application_sid,
            address_sid=address_sid,
            email=email,
            verification_type=verification_type,
            verification_document_sid=verification_document_sid,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV3HostedNumbersHostedNumberOrderApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV3HostedNumbersHostedNumberOrderApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV3HostedNumbersHostedNumberOrderApiWithRawResponse(client, server, auth)

    async def create_hosted_numbers_hosted_number_order(
        self,
        phone_number: str,
        sms_capability: bool,
        *,
        account_sid: str | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        cc_emails: list[str] | None = None,
        sms_url: str | None = None,
        sms_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_application_sid: str | None = None,
        address_sid: str | None = None,
        email: str | None = None,
        verification_type: DependentOrderEnumVerificationTypeOrStr | None = None,
        verification_document_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV3HostedNumbersHostedNumberOrder:
        """Host a phone number's capability on Twilio's platform.

        Args:
            phone_number: The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format
            sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
            account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to
                specify a subaccount to add the HostedNumberOrder to.
            friendly_name: A 64 character string that is a human readable text that describes this resource.
            unique_name: Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder,
                assigned by the developer, to be optionally used in addition to SID.
            cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied
                to.
            sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be
                copied onto the IncomingPhoneNumber resource.
            sms_method: The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``.
                This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML
                defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either
                ``GET`` or ``POST``. This will be copied onto the IncomingPhoneNumber resource.
            status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
            status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
            sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS
                messages sent to this number. If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS
                urls above and use those set on the application.
            address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents
                the address of the owner of this phone number.
            email: Optional. Email of the owner of this phone number that is being hosted.
            verification_type: Value sent with the request.
            verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the
                document for verifying ownership of the number to be hosted. Required when VerificationType is
                phone-bill.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_hosted_numbers_hosted_number_order(
                phone_number,
                sms_capability,
                account_sid=account_sid,
                friendly_name=friendly_name,
                unique_name=unique_name,
                cc_emails=cc_emails,
                sms_url=sms_url,
                sms_method=sms_method,
                sms_fallback_url=sms_fallback_url,
                sms_fallback_method=sms_fallback_method,
                status_callback_url=status_callback_url,
                status_callback_method=status_callback_method,
                sms_application_sid=sms_application_sid,
                address_sid=address_sid,
                email=email,
                verification_type=verification_type,
                verification_document_sid=verification_document_sid,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV3HostedNumbersHostedNumberOrderApiWithRawResponse:
        return self._with_raw_response


class NumbersV3HostedNumbersHostedNumberOrderApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_hosted_numbers_hosted_number_order(
        self,
        phone_number: str,
        sms_capability: bool,
        *,
        account_sid: str | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        cc_emails: list[str] | None = None,
        sms_url: str | None = None,
        sms_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_application_sid: str | None = None,
        address_sid: str | None = None,
        email: str | None = None,
        verification_type: DependentOrderEnumVerificationTypeOrStr | None = None,
        verification_document_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV3HostedNumbersHostedNumberOrder, RawError]:
        """Host a phone number's capability on Twilio's platform.

        Args:
            phone_number: The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format
            sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
            account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to
                specify a subaccount to add the HostedNumberOrder to.
            friendly_name: A 64 character string that is a human readable text that describes this resource.
            unique_name: Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder,
                assigned by the developer, to be optionally used in addition to SID.
            cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied
                to.
            sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be
                copied onto the IncomingPhoneNumber resource.
            sms_method: The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``.
                This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML
                defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either
                ``GET`` or ``POST``. This will be copied onto the IncomingPhoneNumber resource.
            status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
            status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
            sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS
                messages sent to this number. If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS
                urls above and use those set on the application.
            address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents
                the address of the owner of this phone number.
            email: Optional. Email of the owner of this phone number that is being hosted.
            verification_type: Value sent with the request.
            verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the
                document for verifying ownership of the number to be hosted. Required when VerificationType is
                phone-bill.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v3/HostedNumbers/HostedNumberOrders"),
            body=form_body(
                [
                    param[str]("phoneNumber", phone_number),
                    param[bool]("smsCapability", sms_capability),
                    param[str | None]("accountSid", account_sid),
                    param[str | None]("friendlyName", friendly_name),
                    param[str | None]("uniqueName", unique_name),
                    param[list[str] | None]("ccEmails", cc_emails),
                    param[str | None]("smsUrl", sms_url),
                    param[AmdStatusCallbackMethodOrStr | None]("smsMethod", sms_method),
                    param[str | None]("smsFallbackUrl", sms_fallback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("smsFallbackMethod", sms_fallback_method),
                    param[str | None]("statusCallbackUrl", status_callback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("statusCallbackMethod", status_callback_method),
                    param[str | None]("smsApplicationSid", sms_application_sid),
                    param[str | None]("addressSid", address_sid),
                    param[str | None]("email", email),
                    param[DependentOrderEnumVerificationTypeOrStr | None]("verificationType", verification_type),
                    param[str | None]("verificationDocumentSid", verification_document_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV3HostedNumbersHostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV3HostedNumbersHostedNumberOrderApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_hosted_numbers_hosted_number_order(
        self,
        phone_number: str,
        sms_capability: bool,
        *,
        account_sid: str | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        cc_emails: list[str] | None = None,
        sms_url: str | None = None,
        sms_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_fallback_url: str | None = None,
        sms_fallback_method: AmdStatusCallbackMethodOrStr | None = None,
        status_callback_url: str | None = None,
        status_callback_method: AmdStatusCallbackMethodOrStr | None = None,
        sms_application_sid: str | None = None,
        address_sid: str | None = None,
        email: str | None = None,
        verification_type: DependentOrderEnumVerificationTypeOrStr | None = None,
        verification_document_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV3HostedNumbersHostedNumberOrder, RawError]:
        """Host a phone number's capability on Twilio's platform.

        Args:
            phone_number: The number to host in `+E.164 <https://en.wikipedia.org/wiki/E.164>`__ format
            sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
            account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to
                specify a subaccount to add the HostedNumberOrder to.
            friendly_name: A 64 character string that is a human readable text that describes this resource.
            unique_name: Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder,
                assigned by the developer, to be optionally used in addition to SID.
            cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied
                to.
            sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be
                copied onto the IncomingPhoneNumber resource.
            sms_method: The HTTP method that should be used to request the SmsUrl. Must be either ``GET`` or ``POST``.
                This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML
                defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
            sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either
                ``GET`` or ``POST``. This will be copied onto the IncomingPhoneNumber resource.
            status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
            status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
            sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS
                messages sent to this number. If a ``SmsApplicationSid`` is present, Twilio will ignore all of the SMS
                urls above and use those set on the application.
            address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents
                the address of the owner of this phone number.
            email: Optional. Email of the owner of this phone number that is being hosted.
            verification_type: Value sent with the request.
            verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the
                document for verifying ownership of the number to be hosted. Required when VerificationType is
                phone-bill.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default5("/v3/HostedNumbers/HostedNumberOrders"),
            body=form_body(
                [
                    param[str]("phoneNumber", phone_number),
                    param[bool]("smsCapability", sms_capability),
                    param[str | None]("accountSid", account_sid),
                    param[str | None]("friendlyName", friendly_name),
                    param[str | None]("uniqueName", unique_name),
                    param[list[str] | None]("ccEmails", cc_emails),
                    param[str | None]("smsUrl", sms_url),
                    param[AmdStatusCallbackMethodOrStr | None]("smsMethod", sms_method),
                    param[str | None]("smsFallbackUrl", sms_fallback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("smsFallbackMethod", sms_fallback_method),
                    param[str | None]("statusCallbackUrl", status_callback_url),
                    param[AmdStatusCallbackMethodOrStr | None]("statusCallbackMethod", status_callback_method),
                    param[str | None]("smsApplicationSid", sms_application_sid),
                    param[str | None]("addressSid", address_sid),
                    param[str | None]("email", email),
                    param[DependentOrderEnumVerificationTypeOrStr | None]("verificationType", verification_type),
                    param[str | None]("verificationDocumentSid", verification_document_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV3HostedNumbersHostedNumberOrder],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
