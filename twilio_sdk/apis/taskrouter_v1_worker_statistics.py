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
from ..models.taskrouter_v1_workspace_worker_worker_instance_statistics import (
    TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics,
)
from ..server.server import Server


class TaskrouterV1WorkerStatistics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1WorkerStatisticsWithRawResponse(client, server, auth)

    def fetch_worker_instance_statistics(
        self,
        workspace_sid: str,
        worker_sid: str,
        *,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
            worker_sid: The SID of the Worker with the WorkerChannel to fetch.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            end_date: Only include usage that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_worker_instance_statistics(
            workspace_sid,
            worker_sid,
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_channel=task_channel,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1WorkerStatisticsWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1WorkerStatistics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1WorkerStatisticsWithRawResponse(client, server, auth)

    async def fetch_worker_instance_statistics(
        self,
        workspace_sid: str,
        worker_sid: str,
        *,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
            worker_sid: The SID of the Worker with the WorkerChannel to fetch.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            end_date: Only include usage that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_worker_instance_statistics(
                workspace_sid,
                worker_sid,
                minutes=minutes,
                start_date=start_date,
                end_date=end_date,
                task_channel=task_channel,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1WorkerStatisticsWithRawResponse:
        return self._with_raw_response


class TaskrouterV1WorkerStatisticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_worker_instance_statistics(
        self,
        workspace_sid: str,
        worker_sid: str,
        *,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
            worker_sid: The SID of the Worker with the WorkerChannel to fetch.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            end_date: Only include usage that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Statistics"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("WorkerSid", worker_sid)],
            query_params=[
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[str | None]("TaskChannel", task_channel),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1WorkerStatisticsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_worker_instance_statistics(
        self,
        workspace_sid: str,
        worker_sid: str,
        *,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        end_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
            worker_sid: The SID of the Worker with the WorkerChannel to fetch.
            minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is
                helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8
                hours) to see trends.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            end_date: Only include usage that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Statistics"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("WorkerSid", worker_sid)],
            query_params=[
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[str | None]("TaskChannel", task_channel),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkerWorkerInstanceStatistics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
