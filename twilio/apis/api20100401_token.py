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
from ..models.api_v2010_account_token import ApiV2010AccountToken
from ..server.server import Server


class Api20100401Token:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = Api20100401TokenWithRawResponse(client, server, auth)

    def create_token(
        self, account_sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountToken:
        """Create a new token for ICE servers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24
                hours).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_token(account_sid, ttl=ttl, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> Api20100401TokenWithRawResponse:
        return self._with_raw_response


class AsyncApi20100401Token:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApi20100401TokenWithRawResponse(client, server, auth)

    async def create_token(
        self, account_sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiV2010AccountToken:
        """Create a new token for ICE servers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24
                hours).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_token(account_sid, ttl=ttl, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApi20100401TokenWithRawResponse:
        return self._with_raw_response


class Api20100401TokenWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_token(
        self, account_sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountToken, RawError]:
        """Create a new token for ICE servers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24
                hours).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Tokens.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body([param[int | None]("Ttl", ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountToken],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApi20100401TokenWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_token(
        self, account_sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ApiV2010AccountToken, RawError]:
        """Create a new token for ICE servers

        Args:
            account_sid: The SID of the `Account <https://www.twilio.com/docs/iam/api/account>`__ that will create the
                resource.
            ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24
                hours).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/2010-04-01/Accounts/{AccountSid}/Tokens.json"),
            path_params=[param[str]("AccountSid", account_sid)],
            body=form_body([param[int | None]("Ttl", ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ApiV2010AccountToken],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
