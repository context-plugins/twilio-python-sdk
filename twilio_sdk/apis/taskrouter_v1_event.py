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
from ..models.list_event_response import ListEventResponse
from ..models.taskrouter_v1_workspace_event import TaskrouterV1WorkspaceEvent
from ..server.server import Server


class TaskrouterV1Event:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1EventWithRawResponse(client, server, auth)

    def fetch_event(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceEvent:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Event to fetch.
            sid: The SID of the Event resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_event(workspace_sid, sid, request_options=request_options).unwrap()

    def list_event(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        event_type: str | None = None,
        minutes: int | None = None,
        reservation_sid: str | None = None,
        start_date: RFC3339DateTime | None = None,
        task_queue_sid: str | None = None,
        task_sid: str | None = None,
        worker_sid: str | None = None,
        workflow_sid: str | None = None,
        task_channel: str | None = None,
        sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEventResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Events to read. Returns only the Events that pertain to the
                specified Workspace.
            end_date: Only include Events that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            event_type: The type of Events to read. Returns only Events of the type specified.
            minutes: The period of events to read in minutes. Returns only Events that occurred since this many minutes
                in the past. The default is ``15`` minutes. Task Attributes for Events occuring more 43,200 minutes ago
                will be redacted.
            reservation_sid: The SID of the Reservation with the Events to read. Returns only Events that pertain to the
                specified Reservation.
            start_date: Only include Events from on or after this date and time, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format. Task Attributes for Events older than 30 days will
                be redacted.
            task_queue_sid: The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to
                the specified TaskQueue.
            task_sid: The SID of the Task with the Events to read. Returns only the Events that pertain to the specified
                Task.
            worker_sid: The SID of the Worker with the Events to read. Returns only the Events that pertain to the
                specified Worker.
            workflow_sid: The SID of the Workflow with the Events to read. Returns only the Events that pertain to the
                specified Workflow.
            task_channel: The TaskChannel with the Events to read. Returns only the Events that pertain to the specified
                TaskChannel.
            sid: The SID of the Event resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_event(
            workspace_sid,
            end_date=end_date,
            event_type=event_type,
            minutes=minutes,
            reservation_sid=reservation_sid,
            start_date=start_date,
            task_queue_sid=task_queue_sid,
            task_sid=task_sid,
            worker_sid=worker_sid,
            workflow_sid=workflow_sid,
            task_channel=task_channel,
            sid=sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1EventWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1Event:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1EventWithRawResponse(client, server, auth)

    async def fetch_event(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceEvent:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Event to fetch.
            sid: The SID of the Event resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_event(workspace_sid, sid, request_options=request_options)).unwrap()

    async def list_event(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        event_type: str | None = None,
        minutes: int | None = None,
        reservation_sid: str | None = None,
        start_date: RFC3339DateTime | None = None,
        task_queue_sid: str | None = None,
        task_sid: str | None = None,
        worker_sid: str | None = None,
        workflow_sid: str | None = None,
        task_channel: str | None = None,
        sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEventResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Events to read. Returns only the Events that pertain to the
                specified Workspace.
            end_date: Only include Events that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            event_type: The type of Events to read. Returns only Events of the type specified.
            minutes: The period of events to read in minutes. Returns only Events that occurred since this many minutes
                in the past. The default is ``15`` minutes. Task Attributes for Events occuring more 43,200 minutes ago
                will be redacted.
            reservation_sid: The SID of the Reservation with the Events to read. Returns only Events that pertain to the
                specified Reservation.
            start_date: Only include Events from on or after this date and time, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format. Task Attributes for Events older than 30 days will
                be redacted.
            task_queue_sid: The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to
                the specified TaskQueue.
            task_sid: The SID of the Task with the Events to read. Returns only the Events that pertain to the specified
                Task.
            worker_sid: The SID of the Worker with the Events to read. Returns only the Events that pertain to the
                specified Worker.
            workflow_sid: The SID of the Workflow with the Events to read. Returns only the Events that pertain to the
                specified Workflow.
            task_channel: The TaskChannel with the Events to read. Returns only the Events that pertain to the specified
                TaskChannel.
            sid: The SID of the Event resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_event(
                workspace_sid,
                end_date=end_date,
                event_type=event_type,
                minutes=minutes,
                reservation_sid=reservation_sid,
                start_date=start_date,
                task_queue_sid=task_queue_sid,
                task_sid=task_sid,
                worker_sid=worker_sid,
                workflow_sid=workflow_sid,
                task_channel=task_channel,
                sid=sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1EventWithRawResponse:
        return self._with_raw_response


class TaskrouterV1EventWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_event(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceEvent, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Event to fetch.
            sid: The SID of the Event resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Events/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceEvent],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_event(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        event_type: str | None = None,
        minutes: int | None = None,
        reservation_sid: str | None = None,
        start_date: RFC3339DateTime | None = None,
        task_queue_sid: str | None = None,
        task_sid: str | None = None,
        worker_sid: str | None = None,
        workflow_sid: str | None = None,
        task_channel: str | None = None,
        sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEventResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Events to read. Returns only the Events that pertain to the
                specified Workspace.
            end_date: Only include Events that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            event_type: The type of Events to read. Returns only Events of the type specified.
            minutes: The period of events to read in minutes. Returns only Events that occurred since this many minutes
                in the past. The default is ``15`` minutes. Task Attributes for Events occuring more 43,200 minutes ago
                will be redacted.
            reservation_sid: The SID of the Reservation with the Events to read. Returns only Events that pertain to the
                specified Reservation.
            start_date: Only include Events from on or after this date and time, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format. Task Attributes for Events older than 30 days will
                be redacted.
            task_queue_sid: The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to
                the specified TaskQueue.
            task_sid: The SID of the Task with the Events to read. Returns only the Events that pertain to the specified
                Task.
            worker_sid: The SID of the Worker with the Events to read. Returns only the Events that pertain to the
                specified Worker.
            workflow_sid: The SID of the Workflow with the Events to read. Returns only the Events that pertain to the
                specified Workflow.
            task_channel: The TaskChannel with the Events to read. Returns only the Events that pertain to the specified
                TaskChannel.
            sid: The SID of the Event resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Events"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[str | None]("EventType", event_type),
                param[int | None]("Minutes", minutes),
                param[str | None]("ReservationSid", reservation_sid),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskQueueSid", task_queue_sid),
                param[str | None]("TaskSid", task_sid),
                param[str | None]("WorkerSid", worker_sid),
                param[str | None]("WorkflowSid", workflow_sid),
                param[str | None]("TaskChannel", task_channel),
                param[str | None]("Sid", sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEventResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1EventWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_event(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceEvent, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Event to fetch.
            sid: The SID of the Event resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Events/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceEvent],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_event(
        self,
        workspace_sid: str,
        *,
        end_date: RFC3339DateTime | None = None,
        event_type: str | None = None,
        minutes: int | None = None,
        reservation_sid: str | None = None,
        start_date: RFC3339DateTime | None = None,
        task_queue_sid: str | None = None,
        task_sid: str | None = None,
        worker_sid: str | None = None,
        workflow_sid: str | None = None,
        task_channel: str | None = None,
        sid: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEventResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Events to read. Returns only the Events that pertain to the
                specified Workspace.
            end_date: Only include Events that occurred on or before this date, specified in GMT as an `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ date-time.
            event_type: The type of Events to read. Returns only Events of the type specified.
            minutes: The period of events to read in minutes. Returns only Events that occurred since this many minutes
                in the past. The default is ``15`` minutes. Task Attributes for Events occuring more 43,200 minutes ago
                will be redacted.
            reservation_sid: The SID of the Reservation with the Events to read. Returns only Events that pertain to the
                specified Reservation.
            start_date: Only include Events from on or after this date and time, specified in `ISO 8601
                <https://en.wikipedia.org/wiki/ISO_8601>`__ format. Task Attributes for Events older than 30 days will
                be redacted.
            task_queue_sid: The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to
                the specified TaskQueue.
            task_sid: The SID of the Task with the Events to read. Returns only the Events that pertain to the specified
                Task.
            worker_sid: The SID of the Worker with the Events to read. Returns only the Events that pertain to the
                specified Worker.
            workflow_sid: The SID of the Workflow with the Events to read. Returns only the Events that pertain to the
                specified Workflow.
            task_channel: The TaskChannel with the Events to read. Returns only the Events that pertain to the specified
                TaskChannel.
            sid: The SID of the Event resource to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Events"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[RFC3339DateTime | None]("EndDate", end_date),
                param[str | None]("EventType", event_type),
                param[int | None]("Minutes", minutes),
                param[str | None]("ReservationSid", reservation_sid),
                param[RFC3339DateTime | None]("StartDate", start_date),
                param[str | None]("TaskQueueSid", task_queue_sid),
                param[str | None]("TaskSid", task_sid),
                param[str | None]("WorkerSid", worker_sid),
                param[str | None]("WorkflowSid", workflow_sid),
                param[str | None]("TaskChannel", task_channel),
                param[str | None]("Sid", sid),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListEventResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
