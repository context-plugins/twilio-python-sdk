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
from ..models.flex_v1_insights_session import FlexV1InsightsSession
from ..server.server import Server


class FlexV1InsightsSessionApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InsightsSessionApiWithRawResponse(client, server, auth)

    def create_insights_session(
        self, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InsightsSession:
        """To obtain session details for fetching reports and dashboards

        Args:
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_insights_session(
            authorization=authorization, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InsightsSessionApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InsightsSessionApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InsightsSessionApiWithRawResponse(client, server, auth)

    async def create_insights_session(
        self, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InsightsSession:
        """To obtain session details for fetching reports and dashboards

        Args:
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_insights_session(
                authorization=authorization, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InsightsSessionApiWithRawResponse:
        return self._with_raw_response


class FlexV1InsightsSessionApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_insights_session(
        self, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InsightsSession, RawError]:
        """To obtain session details for fetching reports and dashboards

        Args:
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/Session"),
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsSession],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InsightsSessionApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_insights_session(
        self, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InsightsSession, RawError]:
        """To obtain session details for fetching reports and dashboards

        Args:
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Insights/Session"),
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsSession],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
