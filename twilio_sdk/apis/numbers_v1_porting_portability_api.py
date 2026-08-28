from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.numbers_v1_porting_portability import NumbersV1PortingPortability
from ..server.server import Server


class NumbersV1PortingPortabilityApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NumbersV1PortingPortabilityApiWithRawResponse(client, server, auth)

    def fetch_porting_portability(
        self,
        phone_number: str,
        *,
        target_account_sid: str | None = None,
        address_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV1PortingPortability:
        """Check if a single phone number can be ported to Twilio

        Args:
            phone_number: Phone number to check portability in e164 format.
            target_account_sid: Account Sid to which the number will be ported. This can be used to determine if a sub
                account already has the number in its inventory or a different sub account. If this is not provided, the
                authenticated account will be assumed to be the target account.
            address_sid: Address Sid of customer to which the number will be ported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_porting_portability(
            phone_number,
            target_account_sid=target_account_sid,
            address_sid=address_sid,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> NumbersV1PortingPortabilityApiWithRawResponse:
        return self._with_raw_response


class AsyncNumbersV1PortingPortabilityApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNumbersV1PortingPortabilityApiWithRawResponse(client, server, auth)

    async def fetch_porting_portability(
        self,
        phone_number: str,
        *,
        target_account_sid: str | None = None,
        address_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NumbersV1PortingPortability:
        """Check if a single phone number can be ported to Twilio

        Args:
            phone_number: Phone number to check portability in e164 format.
            target_account_sid: Account Sid to which the number will be ported. This can be used to determine if a sub
                account already has the number in its inventory or a different sub account. If this is not provided, the
                authenticated account will be assumed to be the target account.
            address_sid: Address Sid of customer to which the number will be ported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_porting_portability(
                phone_number,
                target_account_sid=target_account_sid,
                address_sid=address_sid,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNumbersV1PortingPortabilityApiWithRawResponse:
        return self._with_raw_response


class NumbersV1PortingPortabilityApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_porting_portability(
        self,
        phone_number: str,
        *,
        target_account_sid: str | None = None,
        address_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV1PortingPortability, RawError]:
        """Check if a single phone number can be ported to Twilio

        Args:
            phone_number: Phone number to check portability in e164 format.
            target_account_sid: Account Sid to which the number will be ported. This can be used to determine if a sub
                account already has the number in its inventory or a different sub account. If this is not provided, the
                authenticated account will be assumed to be the target account.
            address_sid: Address Sid of customer to which the number will be ported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/Portability/PhoneNumber/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            query_params=[
                param[str | None]("TargetAccountSid", target_account_sid), param[str | None]("AddressSid", address_sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingPortability],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNumbersV1PortingPortabilityApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_porting_portability(
        self,
        phone_number: str,
        *,
        target_account_sid: str | None = None,
        address_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NumbersV1PortingPortability, RawError]:
        """Check if a single phone number can be ported to Twilio

        Args:
            phone_number: Phone number to check portability in e164 format.
            target_account_sid: Account Sid to which the number will be ported. This can be used to determine if a sub
                account already has the number in its inventory or a different sub account. If this is not provided, the
                authenticated account will be assumed to be the target account.
            address_sid: Address Sid of customer to which the number will be ported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default5("/v1/Porting/Portability/PhoneNumber/{PhoneNumber}"),
            path_params=[param[str]("PhoneNumber", phone_number)],
            query_params=[
                param[str | None]("TargetAccountSid", target_account_sid), param[str | None]("AddressSid", address_sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[NumbersV1PortingPortability],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
