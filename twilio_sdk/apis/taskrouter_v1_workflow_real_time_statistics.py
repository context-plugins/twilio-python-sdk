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
from ..models.taskrouter_v1_workspace_workflow_workflow_real_time_statistics import (
    TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics,
)
from ..server.server import Server


class TaskrouterV1WorkflowRealTimeStatistics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1WorkflowRealTimeStatisticsWithRawResponse(client, server, auth)

    def fetch_workflow_real_time_statistics(
        self,
        workspace_sid: str,
        workflow_sid: str,
        *,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to fetch.
            workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID
                value.
            task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_workflow_real_time_statistics(
            workspace_sid, workflow_sid, task_channel=task_channel, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1WorkflowRealTimeStatisticsWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1WorkflowRealTimeStatistics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1WorkflowRealTimeStatisticsWithRawResponse(client, server, auth)

    async def fetch_workflow_real_time_statistics(
        self,
        workspace_sid: str,
        workflow_sid: str,
        *,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to fetch.
            workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID
                value.
            task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_workflow_real_time_statistics(
                workspace_sid, workflow_sid, task_channel=task_channel, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1WorkflowRealTimeStatisticsWithRawResponse:
        return self._with_raw_response


class TaskrouterV1WorkflowRealTimeStatisticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_workflow_real_time_statistics(
        self,
        workspace_sid: str,
        workflow_sid: str,
        *,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to fetch.
            workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID
                value.
            task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8(
                "/v1/Workspaces/{WorkspaceSid}/Workflows/{WorkflowSid}/RealTimeStatistics"
            ),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("WorkflowSid", workflow_sid)],
            query_params=[param[str | None]("TaskChannel", task_channel)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1WorkflowRealTimeStatisticsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_workflow_real_time_statistics(
        self,
        workspace_sid: str,
        workflow_sid: str,
        *,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to fetch.
            workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID
                value.
            task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8(
                "/v1/Workspaces/{WorkspaceSid}/Workflows/{WorkflowSid}/RealTimeStatistics"
            ),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("WorkflowSid", workflow_sid)],
            query_params=[param[str | None]("TaskChannel", task_channel)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
