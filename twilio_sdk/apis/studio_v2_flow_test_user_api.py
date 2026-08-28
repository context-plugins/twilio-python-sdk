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
from ..models.studio_v2_flow_test_user import StudioV2FlowTestUser
from ..server.server import Server


class StudioV2FlowTestUserApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV2FlowTestUserApiWithRawResponse(client, server, auth)

    def fetch_test_user(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> StudioV2FlowTestUser:
        """Fetch flow test users

        Args:
            sid: Unique identifier of the flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_test_user(sid, request_options=request_options).unwrap()

    def update_test_user(
        self, sid: str, test_users: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV2FlowTestUser:
        """Update flow test users

        Args:
            sid: Unique identifier of the flow.
            test_users: List of test user identities that can test draft versions of the flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_test_user(sid, test_users, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> StudioV2FlowTestUserApiWithRawResponse:
        return self._with_raw_response


class AsyncStudioV2FlowTestUserApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV2FlowTestUserApiWithRawResponse(client, server, auth)

    async def fetch_test_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV2FlowTestUser:
        """Fetch flow test users

        Args:
            sid: Unique identifier of the flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_test_user(sid, request_options=request_options)).unwrap()

    async def update_test_user(
        self, sid: str, test_users: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> StudioV2FlowTestUser:
        """Update flow test users

        Args:
            sid: Unique identifier of the flow.
            test_users: List of test user identities that can test draft versions of the flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_test_user(sid, test_users, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV2FlowTestUserApiWithRawResponse:
        return self._with_raw_response


class StudioV2FlowTestUserApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_test_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2FlowTestUser, RawError]:
        """Fetch flow test users

        Args:
            sid: Unique identifier of the flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{Sid}/TestUsers"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowTestUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_test_user(
        self, sid: str, test_users: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2FlowTestUser, RawError]:
        """Update flow test users

        Args:
            sid: Unique identifier of the flow.
            test_users: List of test user identities that can test draft versions of the flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/{Sid}/TestUsers"),
            path_params=[param[str]("Sid", sid)],
            body=form_body([param[list[str]]("TestUsers", test_users)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowTestUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV2FlowTestUserApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_test_user(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2FlowTestUser, RawError]:
        """Fetch flow test users

        Args:
            sid: Unique identifier of the flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v2/Flows/{Sid}/TestUsers"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowTestUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_test_user(
        self, sid: str, test_users: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV2FlowTestUser, RawError]:
        """Update flow test users

        Args:
            sid: Unique identifier of the flow.
            test_users: List of test user identities that can test draft versions of the flow.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default11("/v2/Flows/{Sid}/TestUsers"),
            path_params=[param[str]("Sid", sid)],
            body=form_body([param[list[str]]("TestUsers", test_users)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV2FlowTestUser],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
