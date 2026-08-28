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
from ..models.flex_v1_insights_user_roles import FlexV1InsightsUserRoles
from ..server.server import Server


class FlexV1InsightsUserRolesApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InsightsUserRolesApiWithRawResponse(client, server, auth)

    def fetch_insights_user_roles(
        self, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InsightsUserRoles:
        """This is used by Flex UI and Quality Management to fetch the Flex Insights roles for the user

        Args:
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_insights_user_roles(
            authorization=authorization, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InsightsUserRolesApiWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InsightsUserRolesApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InsightsUserRolesApiWithRawResponse(client, server, auth)

    async def fetch_insights_user_roles(
        self, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InsightsUserRoles:
        """This is used by Flex UI and Quality Management to fetch the Flex Insights roles for the user

        Args:
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_insights_user_roles(
                authorization=authorization, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InsightsUserRolesApiWithRawResponse:
        return self._with_raw_response


class FlexV1InsightsUserRolesApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_insights_user_roles(
        self, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InsightsUserRoles, RawError]:
        """This is used by Flex UI and Quality Management to fetch the Flex Insights roles for the user

        Args:
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/UserRoles"),
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsUserRoles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InsightsUserRolesApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_insights_user_roles(
        self, *, authorization: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InsightsUserRoles, RawError]:
        """This is used by Flex UI and Quality Management to fetch the Flex Insights roles for the user

        Args:
            authorization: The Authorization HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Insights/UserRoles"),
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InsightsUserRoles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
