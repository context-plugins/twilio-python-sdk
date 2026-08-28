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
from ..models.api_v2010_account_balance import ApiV2010AccountBalance
from ..server.server import Server


class Api20100401Balance:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401BalanceWithRawResponse(client, server, auth)

    def fetch_balance(
        self, account_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountBalance:
        """Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately.
        Child accounts do not contain balance information

        Args:
            account_sid: The unique SID identifier of the Account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_balance(account_sid, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> Api20100401BalanceWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Balance:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401BalanceWithRawResponse(client, server, auth)

    async def fetch_balance(
        self, account_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountBalance:
        """Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately.
        Child accounts do not contain balance information

        Args:
            account_sid: The unique SID identifier of the Account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_balance(account_sid, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401BalanceWithRawResponse:
        return self._with_raw_response


class Api20100401BalanceWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_balance(
        self, account_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountBalance, RawError]:
        """Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately.
        Child accounts do not contain balance information

        Args:
            account_sid: The unique SID identifier of the Account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Balance.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountBalance],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401BalanceWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_balance(
        self, account_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountBalance, RawError]:
        """Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately.
        Child accounts do not contain balance information

        Args:
            account_sid: The unique SID identifier of the Account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Balance.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountBalance],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
