from __future__ import annotations

from uuid import UUID, uuid4

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
from ..models.list_flow_response import ListFlowResponse
from ..models.studio_v1_flow import StudioV1Flow
from ..server.server import Server


class StudioV1FlowApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StudioV1FlowApiWithRawResponse(client, server, auth)

    def delete_flow(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Flow.

        Args:
            sid: The SID of the Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_flow(sid, request_options=request_options).unwrap()

    def fetch_flow(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> StudioV1Flow:
        """Retrieve a specific Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_flow(sid, request_options=request_options).unwrap()

    def list_flow(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListFlowResponse:
        """Retrieve a list of all Flows.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_flow(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StudioV1FlowApiWithRawResponse:
        return self._with_raw_response


class AsyncStudioV1FlowApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStudioV1FlowApiWithRawResponse(client, server, auth)

    async def delete_flow(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete a specific Flow.

        Args:
            sid: The SID of the Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_flow(sid, request_options=request_options)).unwrap()

    async def fetch_flow(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> StudioV1Flow:
        """Retrieve a specific Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_flow(sid, request_options=request_options)).unwrap()

    async def list_flow(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListFlowResponse:
        """Retrieve a list of all Flows.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_flow(
                page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStudioV1FlowApiWithRawResponse:
        return self._with_raw_response


class StudioV1FlowApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_flow(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Flow.

        Args:
            sid: The SID of the Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default11("/v1/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_flow(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1Flow, RawError]:
        """Retrieve a specific Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1Flow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_flow(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListFlowResponse, RawError]:
        """Retrieve a list of all Flows.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListFlowResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStudioV1FlowApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_flow(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Flow.

        Args:
            sid: The SID of the Flow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default11("/v1/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_flow(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StudioV1Flow, RawError]:
        """Retrieve a specific Flow.

        Args:
            sid: The SID of the Flow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[StudioV1Flow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_flow(
        self,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListFlowResponse, RawError]:
        """Retrieve a list of all Flows.

        Args:
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default11("/v1/Flows"),
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListFlowResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
