from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    param,
    raw_error_response,
)
from ..server.server import Server


class MessagingV1Deactivations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV1DeactivationsWithRawResponse(client, server, auth)

    def fetch_deactivation(
        self, *, date: Date | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Fetch a list of all United States numbers that have been deactivated on a specific date.

        Args:
            date: The request will return a list of all United States Phone Numbers that were deactivated on the day
                specified by this parameter. This date should be specified in YYYY-MM-DD format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_deactivation(date=date, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MessagingV1DeactivationsWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV1Deactivations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV1DeactivationsWithRawResponse(client, server, auth)

    async def fetch_deactivation(
        self, *, date: Date | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Fetch a list of all United States numbers that have been deactivated on a specific date.

        Args:
            date: The request will return a list of all United States Phone Numbers that were deactivated on the day
                specified by this parameter. This date should be specified in YYYY-MM-DD format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_deactivation(date=date, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV1DeactivationsWithRawResponse:
        return self._with_raw_response


class MessagingV1DeactivationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_deactivation(
        self, *, date: Date | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Fetch a list of all United States numbers that have been deactivated on a specific date.

        Args:
            date: The request will return a list of all United States Phone Numbers that were deactivated on the day
                specified by this parameter. This date should be specified in YYYY-MM-DD format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Deactivations"),
            query_params=[param[Date | None]("Date", date)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV1DeactivationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_deactivation(
        self, *, date: Date | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Fetch a list of all United States numbers that have been deactivated on a specific date.

        Args:
            date: The request will return a list of all United States Phone Numbers that were deactivated on the day
                specified by this parameter. This date should be specified in YYYY-MM-DD format.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/v1/Deactivations"),
            query_params=[param[Date | None]("Date", date)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
