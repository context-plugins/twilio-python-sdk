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
    raw_error_response,
)
from ..models.messaging_v1_usecase import MessagingV1Usecase
from ..server.server import Server


class MessagingV1UsecaseApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1UsecaseApiWithRawResponse(client, server, auth)

    def fetch_usecase(self, *, request_options: RequestOptionsOrDict | None = None) -> MessagingV1Usecase:
        """Use Case resource. Fetch possible use cases for a Messaging Service.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_usecase(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1UsecaseApiWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1UsecaseApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1UsecaseApiWithRawResponse(client, server, auth)

    async def fetch_usecase(self, *, request_options: RequestOptionsOrDict | None = None) -> MessagingV1Usecase:
        """Use Case resource. Fetch possible use cases for a Messaging Service.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_usecase(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1UsecaseApiWithRawResponse:
        return self._with_raw_response


class MessagingV1UsecaseApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_usecase(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1Usecase, RawError]:
        """Use Case resource. Fetch possible use cases for a Messaging Service.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/Usecases"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1Usecase],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1UsecaseApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_usecase(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MessagingV1Usecase, RawError]:
        """Use Case resource. Fetch possible use cases for a Messaging Service.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Services/Usecases"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[MessagingV1Usecase],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
