from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.task_queue_enum_task_order import TaskQueueEnumTaskOrderOrStr
from ..models.list_task_queue_response import ListTaskQueueResponse
from ..models.taskrouter_v1_workspace_task_queue import TaskrouterV1WorkspaceTaskQueue
from ..server.server import Server


class TaskrouterV1TaskQueue:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1TaskQueueWithRawResponse(client, server, auth)

    def create_task_queue(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        target_workers: str | None = None,
        max_reserved_workers: int | None = None,
        task_order: TaskQueueEnumTaskOrderOrStr | None = None,
        reservation_activity_sid: str | None = None,
        assignment_activity_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskQueue:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new TaskQueue belongs to.
            friendly_name: A descriptive string that you create to describe the TaskQueue. For example ``Support-Tier
                1``, ``Sales``, or ``Escalation``.
            target_workers: A string that describes the Worker selection criteria for any Tasks that enter the
                TaskQueue. For example, ``'"language" == "spanish"'``. The default value is ``1==1``. If this value is
                empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more
                information about Worker selection, see `Describing Worker selection criteria
                <https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers>`__.
            max_reserved_workers: The maximum number of Workers to reserve for the assignment of a Task in the queue.
                Can be an integer between 1 and 50, inclusive and defaults to 1.
            task_order: How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently
                created Task first or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
                <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more.
            reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
            assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned to them.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_task_queue(
            workspace_sid,
            friendly_name,
            target_workers=target_workers,
            max_reserved_workers=max_reserved_workers,
            task_order=task_order,
            reservation_activity_sid=reservation_activity_sid,
            assignment_activity_sid=assignment_activity_sid,
            request_options=request_options,
        ).unwrap()

    def delete_task_queue(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to delete.
            sid: The SID of the TaskQueue resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_task_queue(workspace_sid, sid, request_options=request_options).unwrap()

    def fetch_task_queue(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTaskQueue:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            sid: The SID of the TaskQueue resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_task_queue(workspace_sid, sid, request_options=request_options).unwrap()

    def list_task_queue(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        evaluate_worker_attributes: str | None = None,
        worker_sid: str | None = None,
        ordering: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskQueueResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to read.
            friendly_name: The ``friendly_name`` of the TaskQueue resources to read.
            evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that
                match the attributes specified in this parameter.
            worker_sid: The SID of the Worker with the TaskQueue resources to read.
            ordering: Sorting parameter for TaskQueues
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_task_queue(
            workspace_sid,
            friendly_name=friendly_name,
            evaluate_worker_attributes=evaluate_worker_attributes,
            worker_sid=worker_sid,
            ordering=ordering,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_task_queue(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        target_workers: str | None = None,
        reservation_activity_sid: str | None = None,
        assignment_activity_sid: str | None = None,
        max_reserved_workers: int | None = None,
        task_order: TaskQueueEnumTaskOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskQueue:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to update.
            sid: The SID of the TaskQueue resource to update.
            friendly_name: A descriptive string that you create to describe the TaskQueue. For example ``Support-Tier
                1``, ``Sales``, or ``Escalation``.
            target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue.
                For example '"language" == "spanish"' If no TargetWorkers parameter is provided, Tasks will wait in the
                queue until they are either deleted or moved to another queue. Additional examples on how to describing
                Worker selection criteria below.
            reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
            assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
            max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task
                while in the queue. Maximum of 50.
            task_order: How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently
                created Task first or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
                <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_task_queue(
            workspace_sid,
            sid,
            friendly_name=friendly_name,
            target_workers=target_workers,
            reservation_activity_sid=reservation_activity_sid,
            assignment_activity_sid=assignment_activity_sid,
            max_reserved_workers=max_reserved_workers,
            task_order=task_order,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1TaskQueueWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1TaskQueue:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1TaskQueueWithRawResponse(client, server, auth)

    async def create_task_queue(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        target_workers: str | None = None,
        max_reserved_workers: int | None = None,
        task_order: TaskQueueEnumTaskOrderOrStr | None = None,
        reservation_activity_sid: str | None = None,
        assignment_activity_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskQueue:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new TaskQueue belongs to.
            friendly_name: A descriptive string that you create to describe the TaskQueue. For example ``Support-Tier
                1``, ``Sales``, or ``Escalation``.
            target_workers: A string that describes the Worker selection criteria for any Tasks that enter the
                TaskQueue. For example, ``'"language" == "spanish"'``. The default value is ``1==1``. If this value is
                empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more
                information about Worker selection, see `Describing Worker selection criteria
                <https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers>`__.
            max_reserved_workers: The maximum number of Workers to reserve for the assignment of a Task in the queue.
                Can be an integer between 1 and 50, inclusive and defaults to 1.
            task_order: How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently
                created Task first or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
                <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more.
            reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
            assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned to them.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_task_queue(
                workspace_sid,
                friendly_name,
                target_workers=target_workers,
                max_reserved_workers=max_reserved_workers,
                task_order=task_order,
                reservation_activity_sid=reservation_activity_sid,
                assignment_activity_sid=assignment_activity_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_task_queue(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to delete.
            sid: The SID of the TaskQueue resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_task_queue(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_task_queue(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTaskQueue:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            sid: The SID of the TaskQueue resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_task_queue(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_task_queue(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        evaluate_worker_attributes: str | None = None,
        worker_sid: str | None = None,
        ordering: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskQueueResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to read.
            friendly_name: The ``friendly_name`` of the TaskQueue resources to read.
            evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that
                match the attributes specified in this parameter.
            worker_sid: The SID of the Worker with the TaskQueue resources to read.
            ordering: Sorting parameter for TaskQueues
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_task_queue(
                workspace_sid,
                friendly_name=friendly_name,
                evaluate_worker_attributes=evaluate_worker_attributes,
                worker_sid=worker_sid,
                ordering=ordering,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_task_queue(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        target_workers: str | None = None,
        reservation_activity_sid: str | None = None,
        assignment_activity_sid: str | None = None,
        max_reserved_workers: int | None = None,
        task_order: TaskQueueEnumTaskOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskQueue:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to update.
            sid: The SID of the TaskQueue resource to update.
            friendly_name: A descriptive string that you create to describe the TaskQueue. For example ``Support-Tier
                1``, ``Sales``, or ``Escalation``.
            target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue.
                For example '"language" == "spanish"' If no TargetWorkers parameter is provided, Tasks will wait in the
                queue until they are either deleted or moved to another queue. Additional examples on how to describing
                Worker selection criteria below.
            reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
            assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
            max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task
                while in the queue. Maximum of 50.
            task_order: How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently
                created Task first or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
                <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_task_queue(
                workspace_sid,
                sid,
                friendly_name=friendly_name,
                target_workers=target_workers,
                reservation_activity_sid=reservation_activity_sid,
                assignment_activity_sid=assignment_activity_sid,
                max_reserved_workers=max_reserved_workers,
                task_order=task_order,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1TaskQueueWithRawResponse:
        return self._with_raw_response


class TaskrouterV1TaskQueueWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_task_queue(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        target_workers: str | None = None,
        max_reserved_workers: int | None = None,
        task_order: TaskQueueEnumTaskOrderOrStr | None = None,
        reservation_activity_sid: str | None = None,
        assignment_activity_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueue, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new TaskQueue belongs to.
            friendly_name: A descriptive string that you create to describe the TaskQueue. For example ``Support-Tier
                1``, ``Sales``, or ``Escalation``.
            target_workers: A string that describes the Worker selection criteria for any Tasks that enter the
                TaskQueue. For example, ``'"language" == "spanish"'``. The default value is ``1==1``. If this value is
                empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more
                information about Worker selection, see `Describing Worker selection criteria
                <https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers>`__.
            max_reserved_workers: The maximum number of Workers to reserve for the assignment of a Task in the queue.
                Can be an integer between 1 and 50, inclusive and defaults to 1.
            task_order: How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently
                created Task first or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
                <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more.
            reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
            assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned to them.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str | None]("TargetWorkers", target_workers),
                    param[int | None]("MaxReservedWorkers", max_reserved_workers),
                    param[TaskQueueEnumTaskOrderOrStr | None]("TaskOrder", task_order),
                    param[str | None]("ReservationActivitySid", reservation_activity_sid),
                    param[str | None]("AssignmentActivitySid", assignment_activity_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_task_queue(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to delete.
            sid: The SID of the TaskQueue resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_task_queue(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueue, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            sid: The SID of the TaskQueue resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_task_queue(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        evaluate_worker_attributes: str | None = None,
        worker_sid: str | None = None,
        ordering: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskQueueResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to read.
            friendly_name: The ``friendly_name`` of the TaskQueue resources to read.
            evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that
                match the attributes specified in this parameter.
            worker_sid: The SID of the Worker with the TaskQueue resources to read.
            ordering: Sorting parameter for TaskQueues
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("EvaluateWorkerAttributes", evaluate_worker_attributes),
                param[str | None]("WorkerSid", worker_sid),
                param[str | None]("Ordering", ordering),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskQueueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_task_queue(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        target_workers: str | None = None,
        reservation_activity_sid: str | None = None,
        assignment_activity_sid: str | None = None,
        max_reserved_workers: int | None = None,
        task_order: TaskQueueEnumTaskOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueue, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to update.
            sid: The SID of the TaskQueue resource to update.
            friendly_name: A descriptive string that you create to describe the TaskQueue. For example ``Support-Tier
                1``, ``Sales``, or ``Escalation``.
            target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue.
                For example '"language" == "spanish"' If no TargetWorkers parameter is provided, Tasks will wait in the
                queue until they are either deleted or moved to another queue. Additional examples on how to describing
                Worker selection criteria below.
            reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
            assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
            max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task
                while in the queue. Maximum of 50.
            task_order: How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently
                created Task first or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
                <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("TargetWorkers", target_workers),
                    param[str | None]("ReservationActivitySid", reservation_activity_sid),
                    param[str | None]("AssignmentActivitySid", assignment_activity_sid),
                    param[int | None]("MaxReservedWorkers", max_reserved_workers),
                    param[TaskQueueEnumTaskOrderOrStr | None]("TaskOrder", task_order),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1TaskQueueWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_task_queue(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        target_workers: str | None = None,
        max_reserved_workers: int | None = None,
        task_order: TaskQueueEnumTaskOrderOrStr | None = None,
        reservation_activity_sid: str | None = None,
        assignment_activity_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueue, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new TaskQueue belongs to.
            friendly_name: A descriptive string that you create to describe the TaskQueue. For example ``Support-Tier
                1``, ``Sales``, or ``Escalation``.
            target_workers: A string that describes the Worker selection criteria for any Tasks that enter the
                TaskQueue. For example, ``'"language" == "spanish"'``. The default value is ``1==1``. If this value is
                empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more
                information about Worker selection, see `Describing Worker selection criteria
                <https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers>`__.
            max_reserved_workers: The maximum number of Workers to reserve for the assignment of a Task in the queue.
                Can be an integer between 1 and 50, inclusive and defaults to 1.
            task_order: How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently
                created Task first or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
                <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more.
            reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
            assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned to them.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str | None]("TargetWorkers", target_workers),
                    param[int | None]("MaxReservedWorkers", max_reserved_workers),
                    param[TaskQueueEnumTaskOrderOrStr | None]("TaskOrder", task_order),
                    param[str | None]("ReservationActivitySid", reservation_activity_sid),
                    param[str | None]("AssignmentActivitySid", assignment_activity_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_task_queue(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to delete.
            sid: The SID of the TaskQueue resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_task_queue(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueue, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
            sid: The SID of the TaskQueue resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_task_queue(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        evaluate_worker_attributes: str | None = None,
        worker_sid: str | None = None,
        ordering: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskQueueResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to read.
            friendly_name: The ``friendly_name`` of the TaskQueue resources to read.
            evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that
                match the attributes specified in this parameter.
            worker_sid: The SID of the Worker with the TaskQueue resources to read.
            ordering: Sorting parameter for TaskQueues
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("EvaluateWorkerAttributes", evaluate_worker_attributes),
                param[str | None]("WorkerSid", worker_sid),
                param[str | None]("Ordering", ordering),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskQueueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_task_queue(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        target_workers: str | None = None,
        reservation_activity_sid: str | None = None,
        assignment_activity_sid: str | None = None,
        max_reserved_workers: int | None = None,
        task_order: TaskQueueEnumTaskOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskQueue, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the TaskQueue to update.
            sid: The SID of the TaskQueue resource to update.
            friendly_name: A descriptive string that you create to describe the TaskQueue. For example ``Support-Tier
                1``, ``Sales``, or ``Escalation``.
            target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue.
                For example '"language" == "spanish"' If no TargetWorkers parameter is provided, Tasks will wait in the
                queue until they are either deleted or moved to another queue. Additional examples on how to describing
                Worker selection criteria below.
            reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
            assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
            max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task
                while in the queue. Maximum of 50.
            task_order: How Tasks will be assigned to Workers. Set this parameter to ``LIFO`` to assign most recently
                created Task first or ``FIFO`` to assign the oldest Task. Default is FIFO. `Click here
                <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__ to learn more.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("TargetWorkers", target_workers),
                    param[str | None]("ReservationActivitySid", reservation_activity_sid),
                    param[str | None]("AssignmentActivitySid", assignment_activity_sid),
                    param[int | None]("MaxReservedWorkers", max_reserved_workers),
                    param[TaskQueueEnumTaskOrderOrStr | None]("TaskOrder", task_order),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskQueue],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
