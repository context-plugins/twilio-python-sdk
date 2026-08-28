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
from ..models.taskrouter_v1_workspace_worker_workers_cumulative_statistics import (
    TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics,
)
from ..server.server import Server


class TaskrouterV1WorkersCumulativeStatistics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1WorkersCumulativeStatisticsWithRawResponse(client, server, auth)

    def fetch_workers_cumulative_statistics(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the resource to fetch.
            end_date: Only calculate statistics from this date and time and earlier, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_workers_cumulative_statistics(
            workspace_sid,
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1WorkersCumulativeStatisticsWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1WorkersCumulativeStatistics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1WorkersCumulativeStatisticsWithRawResponse(client, server, auth)

    async def fetch_workers_cumulative_statistics(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the resource to fetch.
            end_date: Only calculate statistics from this date and time and earlier, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_workers_cumulative_statistics(
                workspace_sid,
                end_date=end_date,
                minutes=minutes,
                start_date=start_date,
                task_channel=task_channel,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1WorkersCumulativeStatisticsWithRawResponse:
        return self._with_raw_response


class TaskrouterV1WorkersCumulativeStatisticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_workers_cumulative_statistics(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the resource to fetch.
            end_date: Only calculate statistics from this date and time and earlier, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/CumulativeStatistics"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskChannel", task_channel),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1WorkersCumulativeStatisticsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def fetch_workers_cumulative_statistics(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the resource to fetch.
            end_date: Only calculate statistics from this date and time and earlier, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/CumulativeStatistics"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskChannel", task_channel),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
