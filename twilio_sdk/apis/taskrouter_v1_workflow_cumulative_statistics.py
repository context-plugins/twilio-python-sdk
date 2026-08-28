from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.taskrouter_v1_workspace_workflow_workflow_cumulative_statistics import (
    TaskrouterV1WorkspaceWorkflowWorkflowCumulativeStatistics,
)
from ..server.server import Server


class TaskrouterV1WorkflowCumulativeStatistics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1WorkflowCumulativeStatisticsWithRawResponse(client, server, auth)

    def fetch_workflow_cumulative_statistics(
        self,
        workspace_sid: str,
        workflow_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkflowWorkflowCumulativeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the resource to fetch.
            workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified Sid
                value.
            end_date: Only include usage that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed. For example, ``5,30`` would show
                splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30
                seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. TaskRouter
                will calculate statistics on up to 10,000 Tasks for any given threshold.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_workflow_cumulative_statistics(
            workspace_sid,
            workflow_sid,
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1WorkflowCumulativeStatisticsWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1WorkflowCumulativeStatistics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1WorkflowCumulativeStatisticsWithRawResponse(client, server, auth)

    async def fetch_workflow_cumulative_statistics(
        self,
        workspace_sid: str,
        workflow_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkflowWorkflowCumulativeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the resource to fetch.
            workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified Sid
                value.
            end_date: Only include usage that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed. For example, ``5,30`` would show
                splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30
                seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. TaskRouter
                will calculate statistics on up to 10,000 Tasks for any given threshold.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_workflow_cumulative_statistics(
                workspace_sid,
                workflow_sid,
                end_date=end_date,
                minutes=minutes,
                start_date=start_date,
                task_channel=task_channel,
                split_by_wait_time=split_by_wait_time,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1WorkflowCumulativeStatisticsWithRawResponse:
        return self._with_raw_response


class TaskrouterV1WorkflowCumulativeStatisticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_workflow_cumulative_statistics(
        self,
        workspace_sid: str,
        workflow_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflowWorkflowCumulativeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the resource to fetch.
            workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified Sid
                value.
            end_date: Only include usage that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed. For example, ``5,30`` would show
                splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30
                seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. TaskRouter
                will calculate statistics on up to 10,000 Tasks for any given threshold.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8(
                "/v1/Workspaces/{WorkspaceSid}/Workflows/{WorkflowSid}/CumulativeStatistics"
            ),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("WorkflowSid", workflow_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskChannel", task_channel),
                param[str | None]("SplitByWaitTime", split_by_wait_time),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflowWorkflowCumulativeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1WorkflowCumulativeStatisticsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_workflow_cumulative_statistics(
        self,
        workspace_sid: str,
        workflow_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflowWorkflowCumulativeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the resource to fetch.
            workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified Sid
                value.
            end_date: Only include usage that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed. For example, ``5,30`` would show
                splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30
                seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. TaskRouter
                will calculate statistics on up to 10,000 Tasks for any given threshold.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8(
                "/v1/Workspaces/{WorkspaceSid}/Workflows/{WorkflowSid}/CumulativeStatistics"
            ),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("WorkflowSid", workflow_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskChannel", task_channel),
                param[str | None]("SplitByWaitTime", split_by_wait_time),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflowWorkflowCumulativeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
