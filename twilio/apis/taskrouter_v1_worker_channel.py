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
from ..models.list_worker_channel_response import ListWorkerChannelResponse
from ..models.taskrouter_v1_workspace_worker_worker_channel import TaskrouterV1WorkspaceWorkerWorkerChannel
from ..server.server import Server


class TaskrouterV1WorkerChannel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1WorkerChannelWithRawResponse(client, server, auth)

    def fetch_worker_channel(
        self, workspace_sid: str, worker_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceWorkerWorkerChannel:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
            worker_sid: The SID of the Worker with the WorkerChannel to fetch.
            sid: The SID of the WorkerChannel to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_worker_channel(
            workspace_sid, worker_sid, sid, request_options=request_options
        ).unwrap()

    def list_worker_channel(
        self,
        workspace_sid: str,
        worker_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkerChannelResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannels to read.
            worker_sid: The SID of the Worker with the WorkerChannels to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_worker_channel(
            workspace_sid,
            worker_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_worker_channel(
        self,
        workspace_sid: str,
        worker_sid: str,
        sid: str,
        *,
        capacity: int | None = None,
        available: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkerWorkerChannel:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to update.
            worker_sid: The SID of the Worker with the WorkerChannel to update.
            sid: The SID of the WorkerChannel to update.
            capacity: The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter
                creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is
                0, no new reservations will be created.
            available: Whether the WorkerChannel is available. Set to ``false`` to prevent the Worker from receiving any
                new Tasks of this TaskChannel type.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_worker_channel(
            workspace_sid, worker_sid, sid, capacity=capacity, available=available, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1WorkerChannelWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1WorkerChannel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1WorkerChannelWithRawResponse(client, server, auth)

    async def fetch_worker_channel(
        self, workspace_sid: str, worker_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceWorkerWorkerChannel:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
            worker_sid: The SID of the Worker with the WorkerChannel to fetch.
            sid: The SID of the WorkerChannel to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_worker_channel(
                workspace_sid, worker_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_worker_channel(
        self,
        workspace_sid: str,
        worker_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkerChannelResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannels to read.
            worker_sid: The SID of the Worker with the WorkerChannels to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_worker_channel(
                workspace_sid,
                worker_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_worker_channel(
        self,
        workspace_sid: str,
        worker_sid: str,
        sid: str,
        *,
        capacity: int | None = None,
        available: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkerWorkerChannel:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to update.
            worker_sid: The SID of the Worker with the WorkerChannel to update.
            sid: The SID of the WorkerChannel to update.
            capacity: The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter
                creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is
                0, no new reservations will be created.
            available: Whether the WorkerChannel is available. Set to ``false`` to prevent the Worker from receiving any
                new Tasks of this TaskChannel type.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_worker_channel(
                workspace_sid, worker_sid, sid, capacity=capacity, available=available, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1WorkerChannelWithRawResponse:
        return self._with_raw_response


class TaskrouterV1WorkerChannelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_worker_channel(
        self, workspace_sid: str, worker_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceWorkerWorkerChannel, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
            worker_sid: The SID of the Worker with the WorkerChannel to fetch.
            sid: The SID of the WorkerChannel to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid}"),
            path_params=[
                param[str]("WorkspaceSid", workspace_sid), param[str]("WorkerSid", worker_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkerWorkerChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_worker_channel(
        self,
        workspace_sid: str,
        worker_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkerChannelResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannels to read.
            worker_sid: The SID of the Worker with the WorkerChannels to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("WorkerSid", worker_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWorkerChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_worker_channel(
        self,
        workspace_sid: str,
        worker_sid: str,
        sid: str,
        *,
        capacity: int | None = None,
        available: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkerWorkerChannel, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to update.
            worker_sid: The SID of the Worker with the WorkerChannel to update.
            sid: The SID of the WorkerChannel to update.
            capacity: The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter
                creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is
                0, no new reservations will be created.
            available: Whether the WorkerChannel is available. Set to ``false`` to prevent the Worker from receiving any
                new Tasks of this TaskChannel type.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid}"),
            path_params=[
                param[str]("WorkspaceSid", workspace_sid), param[str]("WorkerSid", worker_sid), param[str]("Sid", sid)
            ],
            body=form_body([param[int | None]("Capacity", capacity), param[bool | None]("Available", available)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkerWorkerChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1WorkerChannelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_worker_channel(
        self, workspace_sid: str, worker_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceWorkerWorkerChannel, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
            worker_sid: The SID of the Worker with the WorkerChannel to fetch.
            sid: The SID of the WorkerChannel to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid}"),
            path_params=[
                param[str]("WorkspaceSid", workspace_sid), param[str]("WorkerSid", worker_sid), param[str]("Sid", sid)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkerWorkerChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_worker_channel(
        self,
        workspace_sid: str,
        worker_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkerChannelResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannels to read.
            worker_sid: The SID of the Worker with the WorkerChannels to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("WorkerSid", worker_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWorkerChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_worker_channel(
        self,
        workspace_sid: str,
        worker_sid: str,
        sid: str,
        *,
        capacity: int | None = None,
        available: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkerWorkerChannel, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to update.
            worker_sid: The SID of the Worker with the WorkerChannel to update.
            sid: The SID of the WorkerChannel to update.
            capacity: The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter
                creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is
                0, no new reservations will be created.
            available: Whether the WorkerChannel is available. Set to ``false`` to prevent the Worker from receiving any
                new Tasks of this TaskChannel type.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid}"),
            path_params=[
                param[str]("WorkspaceSid", workspace_sid), param[str]("WorkerSid", worker_sid), param[str]("Sid", sid)
            ],
            body=form_body([param[int | None]("Capacity", capacity), param[bool | None]("Available", available)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkerWorkerChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
