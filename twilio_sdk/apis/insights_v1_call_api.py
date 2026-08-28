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
from ..models.insights_v1_call import InsightsV1Call
from ..server.server import Server


class InsightsV1CallApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsV1CallApiWithRawResponse(client, server, auth)

    def fetch_call2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> InsightsV1Call:
        """Send a ``GET`` request.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_call2(sid, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> InsightsV1CallApiWithRawResponse:
        return self._with_raw_response


class AsyncInsightsV1CallApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsV1CallApiWithRawResponse(client, server, auth)

    async def fetch_call2(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> InsightsV1Call:
        """Send a ``GET`` request.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_call2(sid, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncInsightsV1CallApiWithRawResponse:
        return self._with_raw_response


class InsightsV1CallApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_call2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1Call, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1Call],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsV1CallApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_call2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsightsV1Call, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default14("/v1/Voice/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[InsightsV1Call],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
