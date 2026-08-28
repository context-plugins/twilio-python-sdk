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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.numbers_v1_porting_port_in_phone_number import NumbersV1PortingPortInPhoneNumber
from ..server.server import Server


class NumbersV1PortingPortInPhoneNumberApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1PortingPortInPhoneNumberApiWithRawResponse(client, server, auth)

    def delete_porting_port_in_phone_number(
        self, port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Allows to cancel a port in request phone number by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            phone_number_sid: The SID of the Port In request phone number. This is a unique identifier of the phone
                number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_porting_port_in_phone_number(
            port_in_request_sid, phone_number_sid, request_options=request_options
        ).unwrap()

    def fetch_porting_port_in_phone_number(
        self, port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingPortInPhoneNumber:
        """Fetch a phone number by port in request SID and phone number SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            phone_number_sid: The SID of the Phone number. This is a unique identifier of the phone number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_porting_port_in_phone_number(
            port_in_request_sid, phone_number_sid, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1PortingPortInPhoneNumberApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1PortingPortInPhoneNumberApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1PortingPortInPhoneNumberApiWithRawResponse(client, server, auth)

    async def delete_porting_port_in_phone_number(
        self, port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Allows to cancel a port in request phone number by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            phone_number_sid: The SID of the Port In request phone number. This is a unique identifier of the phone
                number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_porting_port_in_phone_number(
                port_in_request_sid, phone_number_sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_porting_port_in_phone_number(
        self, port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NumbersV1PortingPortInPhoneNumber:
        """Fetch a phone number by port in request SID and phone number SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            phone_number_sid: The SID of the Phone number. This is a unique identifier of the phone number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_porting_port_in_phone_number(
                port_in_request_sid, phone_number_sid, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1PortingPortInPhoneNumberApiWithRawResponse:
        return self._with_raw_response


class NumbersV1PortingPortInPhoneNumberApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_porting_port_in_phone_number(
        self, port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Allows to cancel a port in request phone number by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            phone_number_sid: The SID of the Port In request phone number. This is a unique identifier of the phone
                number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v1/Porting/PortIn/{PortInRequestSid}/PhoneNumber/{PhoneNumberSid}"),
            path_params=[
                param[str]("PortInRequestSid", port_in_request_sid), param[str]("PhoneNumberSid", phone_number_sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_porting_port_in_phone_number(
        self, port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingPortInPhoneNumber, RawError]:
        """Fetch a phone number by port in request SID and phone number SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            phone_number_sid: The SID of the Phone number. This is a unique identifier of the phone number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/PortIn/{PortInRequestSid}/PhoneNumber/{PhoneNumberSid}"),
            path_params=[
                param[str]("PortInRequestSid", port_in_request_sid), param[str]("PhoneNumberSid", phone_number_sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingPortInPhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV1PortingPortInPhoneNumberApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def delete_porting_port_in_phone_number(
        self, port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Allows to cancel a port in request phone number by SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            phone_number_sid: The SID of the Port In request phone number. This is a unique identifier of the phone
                number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default5("/v1/Porting/PortIn/{PortInRequestSid}/PhoneNumber/{PhoneNumberSid}"),
            path_params=[
                param[str]("PortInRequestSid", port_in_request_sid), param[str]("PhoneNumberSid", phone_number_sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_porting_port_in_phone_number(
        self, port_in_request_sid: str, phone_number_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NumbersV1PortingPortInPhoneNumber, RawError]:
        """Fetch a phone number by port in request SID and phone number SID

        Args:
            port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
            phone_number_sid: The SID of the Phone number. This is a unique identifier of the phone number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/PortIn/{PortInRequestSid}/PhoneNumber/{PhoneNumberSid}"),
            path_params=[
                param[str]("PortInRequestSid", port_in_request_sid), param[str]("PhoneNumberSid", phone_number_sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingPortInPhoneNumber],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
