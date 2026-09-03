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
from ..models.taskrouter_v1_workspace_task_queue_task_queue_real_time_statistics import (
    TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics,
)
from ..server.server import Server


class TaskrouterV1TaskQueueRealTimeStatistics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1TaskQueueRealTimeStatisticsWithRawResponse(client, server, auth)

    def fetch_task_queue_real_time_statistics(
        self,
        workspace_sid: str,
        task_queue_sid: str,
        *,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
            task_channel: The TaskChannel for which to fetch statistics. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_task_queue_real_time_statistics(
            workspace_sid, task_queue_sid, task_channel=task_channel, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1TaskQueueRealTimeStatisticsWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1TaskQueueRealTimeStatistics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1TaskQueueRealTimeStatisticsWithRawResponse(client, server, auth)

    async def fetch_task_queue_real_time_statistics(
        self,
        workspace_sid: str,
        task_queue_sid: str,
        *,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
            task_channel: The TaskChannel for which to fetch statistics. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_task_queue_real_time_statistics(
                workspace_sid, task_queue_sid, task_channel=task_channel, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1TaskQueueRealTimeStatisticsWithRawResponse:
        return self._with_raw_response


class TaskrouterV1TaskQueueRealTimeStatisticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_task_queue_real_time_statistics(
        self,
        workspace_sid: str,
        task_queue_sid: str,
        *,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
            task_channel: The TaskChannel for which to fetch statistics. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8(
                "/v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/RealTimeStatistics"
            ),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("TaskQueueSid", task_queue_sid)],
            query_params=[param[str | None]("TaskChannel", task_channel)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1TaskQueueRealTimeStatisticsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_task_queue_real_time_statistics(
        self,
        workspace_sid: str,
        task_queue_sid: str,
        *,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
            task_channel: The TaskChannel for which to fetch statistics. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8(
                "/v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/RealTimeStatistics"
            ),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("TaskQueueSid", task_queue_sid)],
            query_params=[param[str | None]("TaskChannel", task_channel)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
