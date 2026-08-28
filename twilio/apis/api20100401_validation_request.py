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
from ..models.api_v2010_account_validation_request import ApiV2010AccountValidationRequest
from ..models.enums.status_callback_method15 import StatusCallbackMethod15OrStr
from ..server.server import Server


class Api20100401ValidationRequest:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401ValidationRequestWithRawResponse(client, server, auth)

    def create_validation_request(
        self,
        account_sid: str,
        phone_number: str,
        *,
        friendly_name: str | None = None,
        call_delay: int | None = None,
        extension: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountValidationRequest:
        """An OutgoingCallerId resource represents a single verified number that may be used as a caller ID when making
        outgoing calls via the REST API and within the TwiML ``<Dial>`` verb.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for the
                new caller ID resource.
            phone_number: The phone number to verify in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__
                format, which consists of a + followed by the country code and subscriber number.
            friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to
                64 characters long. The default value is a formatted version of the phone number.
            call_delay: The number of seconds to delay before initiating the verification call. Can be an integer
                between ``0`` and ``60``, inclusive. The default is ``0``.
            extension: The digits to dial after connecting the verification call.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information
                about the verification process to your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``, and the default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_validation_request(
            account_sid,
            phone_number,
            friendly_name=friendly_name,
            call_delay=call_delay,
            extension=extension,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> Api20100401ValidationRequestWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401ValidationRequest:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401ValidationRequestWithRawResponse(client, server, auth)

    async def create_validation_request(
        self,
        account_sid: str,
        phone_number: str,
        *,
        friendly_name: str | None = None,
        call_delay: int | None = None,
        extension: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiV2010AccountValidationRequest:
        """An OutgoingCallerId resource represents a single verified number that may be used as a caller ID when making
        outgoing calls via the REST API and within the TwiML ``<Dial>`` verb.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for the
                new caller ID resource.
            phone_number: The phone number to verify in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__
                format, which consists of a + followed by the country code and subscriber number.
            friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to
                64 characters long. The default value is a formatted version of the phone number.
            call_delay: The number of seconds to delay before initiating the verification call. Can be an integer
                between ``0`` and ``60``, inclusive. The default is ``0``.
            extension: The digits to dial after connecting the verification call.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information
                about the verification process to your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``, and the default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_validation_request(
                account_sid,
                phone_number,
                friendly_name=friendly_name,
                call_delay=call_delay,
                extension=extension,
                status_callback=status_callback,
                status_callback_method=status_callback_method,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401ValidationRequestWithRawResponse:
        return self._with_raw_response


class Api20100401ValidationRequestWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_validation_request(
        self,
        account_sid: str,
        phone_number: str,
        *,
        friendly_name: str | None = None,
        call_delay: int | None = None,
        extension: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountValidationRequest, RawError]:
        """An OutgoingCallerId resource represents a single verified number that may be used as a caller ID when making
        outgoing calls via the REST API and within the TwiML ``<Dial>`` verb.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for the
                new caller ID resource.
            phone_number: The phone number to verify in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__
                format, which consists of a + followed by the country code and subscriber number.
            friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to
                64 characters long. The default value is a formatted version of the phone number.
            call_delay: The number of seconds to delay before initiating the verification call. Can be an integer
                between ``0`` and ``60``, inclusive. The default is ``0``.
            extension: The digits to dial after connecting the verification call.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information
                about the verification process to your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``, and the default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("PhoneNumber", phone_number),
                    param[str | None]("FriendlyName", friendly_name),
                    param[int | None]("CallDelay", call_delay),
                    param[str | None]("Extension", extension),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod15OrStr | None]("StatusCallbackMethod", status_callback_method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountValidationRequest],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401ValidationRequestWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_validation_request(
        self,
        account_sid: str,
        phone_number: str,
        *,
        friendly_name: str | None = None,
        call_delay: int | None = None,
        extension: str | None = None,
        status_callback: str | None = None,
        status_callback_method: StatusCallbackMethod15OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApiV2010AccountValidationRequest, RawError]:
        """An OutgoingCallerId resource represents a single verified number that may be used as a caller ID when making
        outgoing calls via the REST API and within the TwiML ``<Dial>`` verb.

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ responsible for the
                new caller ID resource.
            phone_number: The phone number to verify in `E.164 <https://www.twilio.com/docs/glossary/what-e164>`__
                format, which consists of a + followed by the country code and subscriber number.
            friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to
                64 characters long. The default value is a formatted version of the phone number.
            call_delay: The number of seconds to delay before initiating the verification call. Can be an integer
                between ``0`` and ``60``, inclusive. The default is ``0``.
            extension: The digits to dial after connecting the verification call.
            status_callback: The URL we should call using the ``status_callback_method`` to send status information
                about the verification process to your application.
            status_callback_method: The HTTP method we should use to call ``status_callback``. Can be: ``GET`` or
                ``POST``, and the default is ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body(
                [
                    param[str]("PhoneNumber", phone_number),
                    param[str | None]("FriendlyName", friendly_name),
                    param[int | None]("CallDelay", call_delay),
                    param[str | None]("Extension", extension),
                    param[str | None]("StatusCallback", status_callback),
                    param[StatusCallbackMethod15OrStr | None]("StatusCallbackMethod", status_callback_method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountValidationRequest],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
