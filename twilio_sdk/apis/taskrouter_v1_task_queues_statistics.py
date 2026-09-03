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
from ..models.list_task_queues_statistics_response import ListTaskQueuesStatisticsResponse
from ..server.server import Server


class TaskrouterV1TaskQueuesStatistics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1TaskQueuesStatisticsWithRawResponse(client, server, auth)

    def list_task_queues_statistics(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        friendly_name: str | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskQueuesStatisticsResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueues to read.
            end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            friendly_name: The ``friendly_name`` of the TaskQueue statistics to read.
            minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_task_queues_statistics(
            workspace_sid,
            end_date=end_date,
            friendly_name=friendly_name,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1TaskQueuesStatisticsWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1TaskQueuesStatistics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1TaskQueuesStatisticsWithRawResponse(client, server, auth)

    async def list_task_queues_statistics(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        friendly_name: str | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskQueuesStatisticsResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueues to read.
            end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            friendly_name: The ``friendly_name`` of the TaskQueue statistics to read.
            minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_task_queues_statistics(
                workspace_sid,
                end_date=end_date,
                friendly_name=friendly_name,
                minutes=minutes,
                start_date=start_date,
                task_channel=task_channel,
                split_by_wait_time=split_by_wait_time,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1TaskQueuesStatisticsWithRawResponse:
        return self._with_raw_response


class TaskrouterV1TaskQueuesStatisticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_task_queues_statistics(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        friendly_name: str | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskQueuesStatisticsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueues to read.
            end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            friendly_name: The ``friendly_name`` of the TaskQueue statistics to read.
            minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/Statistics"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskChannel", task_channel),
                param[str | None]("SplitByWaitTime", split_by_wait_time),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskQueuesStatisticsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1TaskQueuesStatisticsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def list_task_queues_statistics(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        friendly_name: str | None = None,
        minutes: int | None = None,
        start_date: RFC3339DateTime | None = None,
        task_channel: str | None = None,
        split_by_wait_time: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskQueuesStatisticsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueues to read.
            end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            friendly_name: The ``friendly_name`` of the TaskQueue statistics to read.
            minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
            start_date: Only calculate statistics from this date and time and later, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format.
            task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its
                ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate
                statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted
                above and below the specified thresholds in seconds are computed.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/Statistics"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("Minutes", minutes),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskChannel", task_channel),
                param[str | None]("SplitByWaitTime", split_by_wait_time),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskQueuesStatisticsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
