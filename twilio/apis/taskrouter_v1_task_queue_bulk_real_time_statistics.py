from __future__ import annotations

from typing import Any

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.taskrouter_v1_workspace_task_queue_task_queue_bulk_real_time_statistics import (
    TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics,
)
from ..server.server import Server


class TaskrouterV1TaskQueueBulkRealTimeStatistics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1TaskQueueBulkRealTimeStatisticsWithRawResponse(client, server, auth)

    def create_task_queue_bulk_real_time_statistics(
        self, workspace_sid: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics:
        """Fetch a Task Queue Real Time Statistics in bulk for the array of TaskQueue SIDs, support upto 50 in a
        request.

        Args:
            workspace_sid: The unique SID identifier of the Workspace.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_task_queue_bulk_real_time_statistics(
            workspace_sid, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1TaskQueueBulkRealTimeStatisticsWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1TaskQueueBulkRealTimeStatistics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1TaskQueueBulkRealTimeStatisticsWithRawResponse(client, server, auth)

    async def create_task_queue_bulk_real_time_statistics(
        self, workspace_sid: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics:
        """Fetch a Task Queue Real Time Statistics in bulk for the array of TaskQueue SIDs, support upto 50 in a
        request.

        Args:
            workspace_sid: The unique SID identifier of the Workspace.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_task_queue_bulk_real_time_statistics(
                workspace_sid, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1TaskQueueBulkRealTimeStatisticsWithRawResponse:
        return self._with_raw_response


class TaskrouterV1TaskQueueBulkRealTimeStatisticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_task_queue_bulk_real_time_statistics(
        self, workspace_sid: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics, RawError]:
        """Fetch a Task Queue Real Time Statistics in bulk for the array of TaskQueue SIDs, support upto 50 in a
        request.

        Args:
            workspace_sid: The unique SID identifier of the Workspace.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/RealTimeStatistics"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1TaskQueueBulkRealTimeStatisticsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_task_queue_bulk_real_time_statistics(
        self, workspace_sid: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics, RawError]:
        """Fetch a Task Queue Real Time Statistics in bulk for the array of TaskQueue SIDs, support upto 50 in a
        request.

        Args:
            workspace_sid: The unique SID identifier of the Workspace.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/RealTimeStatistics"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
