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
from ..models.taskrouter_v1_workspace_task_queue_task_queue_cumulative_statistics import (
    TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics,
)
from ..server.server import Server


class TaskrouterV1TaskQueueCumulativeStatistics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1TaskQueueCumulativeStatisticsWithRawResponse(client, server, auth)

    def fetch_task_queue_cumulative_statistics(
        self,
        workspace_sid: str,
        task_queue_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
            end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed. TaskRouter will calculate statistics
                on up to 10,000 Tasks/Reservations for any given threshold.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_task_queue_cumulative_statistics(
            workspace_sid,
            task_queue_sid,
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1TaskQueueCumulativeStatisticsWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1TaskQueueCumulativeStatistics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1TaskQueueCumulativeStatisticsWithRawResponse(client, server, auth)

    async def fetch_task_queue_cumulative_statistics(
        self,
        workspace_sid: str,
        task_queue_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
            end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed. TaskRouter will calculate statistics
                on up to 10,000 Tasks/Reservations for any given threshold.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_task_queue_cumulative_statistics(
                workspace_sid,
                task_queue_sid,
                end_date=end_date,
                minutes=minutes,
                start_date=start_date,
                task_channel=task_channel,
                split_by_wait_time=split_by_wait_time,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1TaskQueueCumulativeStatisticsWithRawResponse:
        return self._with_raw_response


class TaskrouterV1TaskQueueCumulativeStatisticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_task_queue_cumulative_statistics(
        self,
        workspace_sid: str,
        task_queue_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
            end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed. TaskRouter will calculate statistics
                on up to 10,000 Tasks/Reservations for any given threshold.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8(
                "/v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/CumulativeStatistics"
            ),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("TaskQueueSid", task_queue_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskChannel", task_channel),
                param[str | None]("SplitByWaitTime", split_by_wait_time),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1TaskQueueCumulativeStatisticsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_task_queue_cumulative_statistics(
        self,
        workspace_sid: str,
        task_queue_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
            end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed. TaskRouter will calculate statistics
                on up to 10,000 Tasks/Reservations for any given threshold.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8(
                "/v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/CumulativeStatistics"
            ),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("TaskQueueSid", task_queue_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskChannel", task_channel),
                param[str | None]("SplitByWaitTime", split_by_wait_time),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
