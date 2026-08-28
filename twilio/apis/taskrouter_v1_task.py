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
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.enums.task_enum_status import TaskEnumStatusOrStr
from ..models.list_task_response import ListTaskResponse
from ..models.taskrouter_v1_workspace_task import TaskrouterV1WorkspaceTask
from ..server.server import Server


class TaskrouterV1Task:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1TaskWithRawResponse(client, server, auth)

    def create_task(
        self,
        workspace_sid: str,
        *,
        timeout: int | None = None,
        priority: int | None = None,
        task_channel: str | None = None,
        workflow_sid: str | None = None,
        attributes: str | None = None,
        virtual_start_time: RFC3339DateTime | None = None,
        routing_target: str | None = None,
        ignore_capacity: str | None = None,
        task_queue_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTask:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Task belongs to.
            timeout: The amount of time in seconds the new task can live before being assigned. Can be up to a maximum
                of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the
                ``task.canceled`` event will fire with description ``Task TTL Exceeded``.
            priority: The priority to assign the new task and override the default. When supplied, the new Task will
                have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new
                Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647).
            task_channel: When MultiTasking is enabled, specify the TaskChannel by passing either its ``unique_name`` or
                ``sid``. Default value is ``default``.
            workflow_sid: The SID of the Workflow that you would like to handle routing for the new Task. If there is
                only one Workflow defined for the Workspace that you are posting the new task to, this parameter is
                optional.
            attributes: A JSON string with the attributes of the new task. This value is passed to the Workflow's
                ``assignment_callback_url`` when the Task is assigned to a Worker. For example: ``{ "task_type": "call",
                "twilio_call_sid": "CAxxx", "customer_ticket_number": "12345" }``.
            virtual_start_time: The virtual start time to assign the new task and override the default. When supplied,
                the new task will have this virtual start time. When not supplied, the new task will have the virtual
                start time equal to ``date_created``. Value can't be in the future or before the year of 1900.
            routing_target: A SID of a Worker, Queue, or Workflow to route a Task to
            ignore_capacity: A boolean that indicates if the Task should respect a Worker's capacity and availability
                during assignment. This field can only be used when the ``RoutingTarget`` field is set to a Worker SID.
                By setting ``IgnoreCapacity`` to a value of ``true``, ``1``, or ``yes``, the Task will be routed to the
                Worker without respecting their capacity and availability. Any other value will enforce the Worker's
                capacity and availability. The default value of ``IgnoreCapacity`` is ``true`` when the
                ``RoutingTarget`` is set to a Worker SID.
            task_queue_sid: The SID of the TaskQueue in which the Task belongs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_task(
            workspace_sid,
            timeout=timeout,
            priority=priority,
            task_channel=task_channel,
            workflow_sid=workflow_sid,
            attributes=attributes,
            virtual_start_time=virtual_start_time,
            routing_target=routing_target,
            ignore_capacity=ignore_capacity,
            task_queue_sid=task_queue_sid,
            request_options=request_options,
        ).unwrap()

    def delete_task(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to delete.
            sid: The SID of the Task resource to delete.
            if_match: If provided, deletes this Task if (and only if) the `ETag
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`__ header of the Task matches the
                provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match header
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_task(
            workspace_sid, sid, if_match=if_match, request_options=request_options
        ).unwrap()

    def fetch_task(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTask:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to fetch.
            sid: The SID of the Task resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_task(workspace_sid, sid, request_options=request_options).unwrap()

    def list_task(
        self,
        workspace_sid: str,
        *,
        priority: int | None = None,
        assignment_status: list[str] | None = None,
        workflow_sid: str | None = None,
        workflow_name: str | None = None,
        task_queue_sid: str | None = None,
        task_queue_name: str | None = None,
        evaluate_task_attributes: str | None = None,
        routing_target: str | None = None,
        ordering: str | None = None,
        has_addons: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Tasks to read.
            priority: The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the
                specified priority.
            assignment_status: The ``assignment_status`` of the Tasks you want to read. Can be: ``pending``,
                ``reserved``, ``assigned``, ``canceled``, ``wrapping``, or ``completed``. Returns all Tasks in the
                Workspace with the specified ``assignment_status``.
            workflow_sid: The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow
                identified by this SID.
            workflow_name: The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the
                Workflow identified by this friendly name.
            task_queue_sid: The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue
                identified by this SID.
            task_queue_name: The ``friendly_name`` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in
                the TaskQueue identified by this friendly name.
            evaluate_task_attributes: The attributes of the Tasks to read. Returns the Tasks that match the attributes
                specified in this parameter.
            routing_target: A SID of a Worker, Queue, or Workflow to route a Task to
            ordering: How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated.
                This value is specified as: ``Attribute:Order``, where ``Attribute`` can be either ``DateCreated``,
                ``Priority``, or ``VirtualStartTime`` and ``Order`` can be either ``asc`` or ``desc``. For example,
                ``Priority:desc`` returns Tasks ordered in descending order of their Priority. Pairings of sort orders
                can be specified in a comma-separated list such as ``Priority:desc,DateCreated:asc``, which returns the
                Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not
                allowed is DateCreated and VirtualStartTime.
            has_addons: Whether to read Tasks with Add-ons. If ``true``, returns only Tasks with Add-ons. If ``false``,
                returns only Tasks without Add-ons.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_task(
            workspace_sid,
            priority=priority,
            assignment_status=assignment_status,
            workflow_sid=workflow_sid,
            workflow_name=workflow_name,
            task_queue_sid=task_queue_sid,
            task_queue_name=task_queue_name,
            evaluate_task_attributes=evaluate_task_attributes,
            routing_target=routing_target,
            ordering=ordering,
            has_addons=has_addons,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_task(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        attributes: str | None = None,
        assignment_status: TaskEnumStatusOrStr | None = None,
        reason: str | None = None,
        priority: int | None = None,
        task_channel: str | None = None,
        virtual_start_time: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTask:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to update.
            sid: The SID of the Task resource to update.
            if_match: If provided, applies this mutation if (and only if) the `ETag
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`__ header of the Task matches the
                provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match header
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            attributes: The JSON string that describes the custom attributes of the task.
            assignment_status: The current status of the Task's assignment. Can be: ``pending``, ``reserved``,
                ``assigned``, ``canceled``, ``wrapping``, or ``completed``.
            reason: The reason that the Task was canceled or completed. This parameter is required only if the Task is
                canceled or completed. Setting this value queues the task for deletion and logs the reason.
            priority: The Task's new priority value. When supplied, the Task takes on the specified priority unless it
                matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
            task_channel: When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the
                TaskChannel's SID or its ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            virtual_start_time: The task's new virtual start time value. When supplied, the Task takes on the specified
                virtual start time. Value can't be in the future or before the year of 1900.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_task(
            workspace_sid,
            sid,
            if_match=if_match,
            attributes=attributes,
            assignment_status=assignment_status,
            reason=reason,
            priority=priority,
            task_channel=task_channel,
            virtual_start_time=virtual_start_time,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1TaskWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1Task:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1TaskWithRawResponse(client, server, auth)

    async def create_task(
        self,
        workspace_sid: str,
        *,
        timeout: int | None = None,
        priority: int | None = None,
        task_channel: str | None = None,
        workflow_sid: str | None = None,
        attributes: str | None = None,
        virtual_start_time: RFC3339DateTime | None = None,
        routing_target: str | None = None,
        ignore_capacity: str | None = None,
        task_queue_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTask:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Task belongs to.
            timeout: The amount of time in seconds the new task can live before being assigned. Can be up to a maximum
                of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the
                ``task.canceled`` event will fire with description ``Task TTL Exceeded``.
            priority: The priority to assign the new task and override the default. When supplied, the new Task will
                have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new
                Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647).
            task_channel: When MultiTasking is enabled, specify the TaskChannel by passing either its ``unique_name`` or
                ``sid``. Default value is ``default``.
            workflow_sid: The SID of the Workflow that you would like to handle routing for the new Task. If there is
                only one Workflow defined for the Workspace that you are posting the new task to, this parameter is
                optional.
            attributes: A JSON string with the attributes of the new task. This value is passed to the Workflow's
                ``assignment_callback_url`` when the Task is assigned to a Worker. For example: ``{ "task_type": "call",
                "twilio_call_sid": "CAxxx", "customer_ticket_number": "12345" }``.
            virtual_start_time: The virtual start time to assign the new task and override the default. When supplied,
                the new task will have this virtual start time. When not supplied, the new task will have the virtual
                start time equal to ``date_created``. Value can't be in the future or before the year of 1900.
            routing_target: A SID of a Worker, Queue, or Workflow to route a Task to
            ignore_capacity: A boolean that indicates if the Task should respect a Worker's capacity and availability
                during assignment. This field can only be used when the ``RoutingTarget`` field is set to a Worker SID.
                By setting ``IgnoreCapacity`` to a value of ``true``, ``1``, or ``yes``, the Task will be routed to the
                Worker without respecting their capacity and availability. Any other value will enforce the Worker's
                capacity and availability. The default value of ``IgnoreCapacity`` is ``true`` when the
                ``RoutingTarget`` is set to a Worker SID.
            task_queue_sid: The SID of the TaskQueue in which the Task belongs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_task(
                workspace_sid,
                timeout=timeout,
                priority=priority,
                task_channel=task_channel,
                workflow_sid=workflow_sid,
                attributes=attributes,
                virtual_start_time=virtual_start_time,
                routing_target=routing_target,
                ignore_capacity=ignore_capacity,
                task_queue_sid=task_queue_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_task(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to delete.
            sid: The SID of the Task resource to delete.
            if_match: If provided, deletes this Task if (and only if) the `ETag
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`__ header of the Task matches the
                provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match header
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_task(
                workspace_sid, sid, if_match=if_match, request_options=request_options
            )
        ).unwrap()

    async def fetch_task(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTask:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to fetch.
            sid: The SID of the Task resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_task(workspace_sid, sid, request_options=request_options)).unwrap()

    async def list_task(
        self,
        workspace_sid: str,
        *,
        priority: int | None = None,
        assignment_status: list[str] | None = None,
        workflow_sid: str | None = None,
        workflow_name: str | None = None,
        task_queue_sid: str | None = None,
        task_queue_name: str | None = None,
        evaluate_task_attributes: str | None = None,
        routing_target: str | None = None,
        ordering: str | None = None,
        has_addons: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Tasks to read.
            priority: The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the
                specified priority.
            assignment_status: The ``assignment_status`` of the Tasks you want to read. Can be: ``pending``,
                ``reserved``, ``assigned``, ``canceled``, ``wrapping``, or ``completed``. Returns all Tasks in the
                Workspace with the specified ``assignment_status``.
            workflow_sid: The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow
                identified by this SID.
            workflow_name: The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the
                Workflow identified by this friendly name.
            task_queue_sid: The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue
                identified by this SID.
            task_queue_name: The ``friendly_name`` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in
                the TaskQueue identified by this friendly name.
            evaluate_task_attributes: The attributes of the Tasks to read. Returns the Tasks that match the attributes
                specified in this parameter.
            routing_target: A SID of a Worker, Queue, or Workflow to route a Task to
            ordering: How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated.
                This value is specified as: ``Attribute:Order``, where ``Attribute`` can be either ``DateCreated``,
                ``Priority``, or ``VirtualStartTime`` and ``Order`` can be either ``asc`` or ``desc``. For example,
                ``Priority:desc`` returns Tasks ordered in descending order of their Priority. Pairings of sort orders
                can be specified in a comma-separated list such as ``Priority:desc,DateCreated:asc``, which returns the
                Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not
                allowed is DateCreated and VirtualStartTime.
            has_addons: Whether to read Tasks with Add-ons. If ``true``, returns only Tasks with Add-ons. If ``false``,
                returns only Tasks without Add-ons.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_task(
                workspace_sid,
                priority=priority,
                assignment_status=assignment_status,
                workflow_sid=workflow_sid,
                workflow_name=workflow_name,
                task_queue_sid=task_queue_sid,
                task_queue_name=task_queue_name,
                evaluate_task_attributes=evaluate_task_attributes,
                routing_target=routing_target,
                ordering=ordering,
                has_addons=has_addons,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_task(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        attributes: str | None = None,
        assignment_status: TaskEnumStatusOrStr | None = None,
        reason: str | None = None,
        priority: int | None = None,
        task_channel: str | None = None,
        virtual_start_time: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTask:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to update.
            sid: The SID of the Task resource to update.
            if_match: If provided, applies this mutation if (and only if) the `ETag
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`__ header of the Task matches the
                provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match header
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            attributes: The JSON string that describes the custom attributes of the task.
            assignment_status: The current status of the Task's assignment. Can be: ``pending``, ``reserved``,
                ``assigned``, ``canceled``, ``wrapping``, or ``completed``.
            reason: The reason that the Task was canceled or completed. This parameter is required only if the Task is
                canceled or completed. Setting this value queues the task for deletion and logs the reason.
            priority: The Task's new priority value. When supplied, the Task takes on the specified priority unless it
                matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
            task_channel: When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the
                TaskChannel's SID or its ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            virtual_start_time: The task's new virtual start time value. When supplied, the Task takes on the specified
                virtual start time. Value can't be in the future or before the year of 1900.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_task(
                workspace_sid,
                sid,
                if_match=if_match,
                attributes=attributes,
                assignment_status=assignment_status,
                reason=reason,
                priority=priority,
                task_channel=task_channel,
                virtual_start_time=virtual_start_time,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1TaskWithRawResponse:
        return self._with_raw_response


class TaskrouterV1TaskWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_task(
        self,
        workspace_sid: str,
        *,
        timeout: int | None = None,
        priority: int | None = None,
        task_channel: str | None = None,
        workflow_sid: str | None = None,
        attributes: str | None = None,
        virtual_start_time: RFC3339DateTime | None = None,
        routing_target: str | None = None,
        ignore_capacity: str | None = None,
        task_queue_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTask, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Task belongs to.
            timeout: The amount of time in seconds the new task can live before being assigned. Can be up to a maximum
                of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the
                ``task.canceled`` event will fire with description ``Task TTL Exceeded``.
            priority: The priority to assign the new task and override the default. When supplied, the new Task will
                have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new
                Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647).
            task_channel: When MultiTasking is enabled, specify the TaskChannel by passing either its ``unique_name`` or
                ``sid``. Default value is ``default``.
            workflow_sid: The SID of the Workflow that you would like to handle routing for the new Task. If there is
                only one Workflow defined for the Workspace that you are posting the new task to, this parameter is
                optional.
            attributes: A JSON string with the attributes of the new task. This value is passed to the Workflow's
                ``assignment_callback_url`` when the Task is assigned to a Worker. For example: ``{ "task_type": "call",
                "twilio_call_sid": "CAxxx", "customer_ticket_number": "12345" }``.
            virtual_start_time: The virtual start time to assign the new task and override the default. When supplied,
                the new task will have this virtual start time. When not supplied, the new task will have the virtual
                start time equal to ``date_created``. Value can't be in the future or before the year of 1900.
            routing_target: A SID of a Worker, Queue, or Workflow to route a Task to
            ignore_capacity: A boolean that indicates if the Task should respect a Worker's capacity and availability
                during assignment. This field can only be used when the ``RoutingTarget`` field is set to a Worker SID.
                By setting ``IgnoreCapacity`` to a value of ``true``, ``1``, or ``yes``, the Task will be routed to the
                Worker without respecting their capacity and availability. Any other value will enforce the Worker's
                capacity and availability. The default value of ``IgnoreCapacity`` is ``true`` when the
                ``RoutingTarget`` is set to a Worker SID.
            task_queue_sid: The SID of the TaskQueue in which the Task belongs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            body=form_body(
                [
                    param[int | None]("Timeout", timeout),
                    param[int | None]("Priority", priority),
                    param[str | None]("TaskChannel", task_channel),
                    param[str | None]("WorkflowSid", workflow_sid),
                    param[str | None]("Attributes", attributes),
                    param[RFC3339DateTime | None]("VirtualStartTime", virtual_start_time),
                    param[str | None]("RoutingTarget", routing_target),
                    param[str | None]("IgnoreCapacity", ignore_capacity),
                    param[str | None]("TaskQueueSid", task_queue_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTask],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_task(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to delete.
            sid: The SID of the Task resource to delete.
            if_match: If provided, deletes this Task if (and only if) the `ETag
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`__ header of the Task matches the
                provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match header
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_task(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTask, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to fetch.
            sid: The SID of the Task resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTask],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_task(
        self,
        workspace_sid: str,
        *,
        priority: int | None = None,
        assignment_status: list[str] | None = None,
        workflow_sid: str | None = None,
        workflow_name: str | None = None,
        task_queue_sid: str | None = None,
        task_queue_name: str | None = None,
        evaluate_task_attributes: str | None = None,
        routing_target: str | None = None,
        ordering: str | None = None,
        has_addons: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Tasks to read.
            priority: The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the
                specified priority.
            assignment_status: The ``assignment_status`` of the Tasks you want to read. Can be: ``pending``,
                ``reserved``, ``assigned``, ``canceled``, ``wrapping``, or ``completed``. Returns all Tasks in the
                Workspace with the specified ``assignment_status``.
            workflow_sid: The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow
                identified by this SID.
            workflow_name: The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the
                Workflow identified by this friendly name.
            task_queue_sid: The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue
                identified by this SID.
            task_queue_name: The ``friendly_name`` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in
                the TaskQueue identified by this friendly name.
            evaluate_task_attributes: The attributes of the Tasks to read. Returns the Tasks that match the attributes
                specified in this parameter.
            routing_target: A SID of a Worker, Queue, or Workflow to route a Task to
            ordering: How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated.
                This value is specified as: ``Attribute:Order``, where ``Attribute`` can be either ``DateCreated``,
                ``Priority``, or ``VirtualStartTime`` and ``Order`` can be either ``asc`` or ``desc``. For example,
                ``Priority:desc`` returns Tasks ordered in descending order of their Priority. Pairings of sort orders
                can be specified in a comma-separated list such as ``Priority:desc,DateCreated:asc``, which returns the
                Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not
                allowed is DateCreated and VirtualStartTime.
            has_addons: Whether to read Tasks with Add-ons. If ``true``, returns only Tasks with Add-ons. If ``false``,
                returns only Tasks without Add-ons.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[int | None]("Priority", priority),
                param[list[str] | None]("AssignmentStatus", assignment_status),
                param[str | None]("WorkflowSid", workflow_sid),
                param[str | None]("WorkflowName", workflow_name),
                param[str | None]("TaskQueueSid", task_queue_sid),
                param[str | None]("TaskQueueName", task_queue_name),
                param[str | None]("EvaluateTaskAttributes", evaluate_task_attributes),
                param[str | None]("RoutingTarget", routing_target),
                param[str | None]("Ordering", ordering),
                param[bool | None]("HasAddons", has_addons),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_task(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        attributes: str | None = None,
        assignment_status: TaskEnumStatusOrStr | None = None,
        reason: str | None = None,
        priority: int | None = None,
        task_channel: str | None = None,
        virtual_start_time: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTask, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to update.
            sid: The SID of the Task resource to update.
            if_match: If provided, applies this mutation if (and only if) the `ETag
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`__ header of the Task matches the
                provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match header
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            attributes: The JSON string that describes the custom attributes of the task.
            assignment_status: The current status of the Task's assignment. Can be: ``pending``, ``reserved``,
                ``assigned``, ``canceled``, ``wrapping``, or ``completed``.
            reason: The reason that the Task was canceled or completed. This parameter is required only if the Task is
                canceled or completed. Setting this value queues the task for deletion and logs the reason.
            priority: The Task's new priority value. When supplied, the Task takes on the specified priority unless it
                matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
            task_channel: When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the
                TaskChannel's SID or its ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            virtual_start_time: The task's new virtual start time value. When supplied, the Task takes on the specified
                virtual start time. Value can't be in the future or before the year of 1900.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match)],
            body=form_body(
                [
                    param[str | None]("Attributes", attributes),
                    param[TaskEnumStatusOrStr | None]("AssignmentStatus", assignment_status),
                    param[str | None]("Reason", reason),
                    param[int | None]("Priority", priority),
                    param[str | None]("TaskChannel", task_channel),
                    param[RFC3339DateTime | None]("VirtualStartTime", virtual_start_time),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTask],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1TaskWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_task(
        self,
        workspace_sid: str,
        *,
        timeout: int | None = None,
        priority: int | None = None,
        task_channel: str | None = None,
        workflow_sid: str | None = None,
        attributes: str | None = None,
        virtual_start_time: RFC3339DateTime | None = None,
        routing_target: str | None = None,
        ignore_capacity: str | None = None,
        task_queue_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTask, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Task belongs to.
            timeout: The amount of time in seconds the new task can live before being assigned. Can be up to a maximum
                of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the
                ``task.canceled`` event will fire with description ``Task TTL Exceeded``.
            priority: The priority to assign the new task and override the default. When supplied, the new Task will
                have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new
                Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647).
            task_channel: When MultiTasking is enabled, specify the TaskChannel by passing either its ``unique_name`` or
                ``sid``. Default value is ``default``.
            workflow_sid: The SID of the Workflow that you would like to handle routing for the new Task. If there is
                only one Workflow defined for the Workspace that you are posting the new task to, this parameter is
                optional.
            attributes: A JSON string with the attributes of the new task. This value is passed to the Workflow's
                ``assignment_callback_url`` when the Task is assigned to a Worker. For example: ``{ "task_type": "call",
                "twilio_call_sid": "CAxxx", "customer_ticket_number": "12345" }``.
            virtual_start_time: The virtual start time to assign the new task and override the default. When supplied,
                the new task will have this virtual start time. When not supplied, the new task will have the virtual
                start time equal to ``date_created``. Value can't be in the future or before the year of 1900.
            routing_target: A SID of a Worker, Queue, or Workflow to route a Task to
            ignore_capacity: A boolean that indicates if the Task should respect a Worker's capacity and availability
                during assignment. This field can only be used when the ``RoutingTarget`` field is set to a Worker SID.
                By setting ``IgnoreCapacity`` to a value of ``true``, ``1``, or ``yes``, the Task will be routed to the
                Worker without respecting their capacity and availability. Any other value will enforce the Worker's
                capacity and availability. The default value of ``IgnoreCapacity`` is ``true`` when the
                ``RoutingTarget`` is set to a Worker SID.
            task_queue_sid: The SID of the TaskQueue in which the Task belongs
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            body=form_body(
                [
                    param[int | None]("Timeout", timeout),
                    param[int | None]("Priority", priority),
                    param[str | None]("TaskChannel", task_channel),
                    param[str | None]("WorkflowSid", workflow_sid),
                    param[str | None]("Attributes", attributes),
                    param[RFC3339DateTime | None]("VirtualStartTime", virtual_start_time),
                    param[str | None]("RoutingTarget", routing_target),
                    param[str | None]("IgnoreCapacity", ignore_capacity),
                    param[str | None]("TaskQueueSid", task_queue_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTask],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_task(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to delete.
            sid: The SID of the Task resource to delete.
            if_match: If provided, deletes this Task if (and only if) the `ETag
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`__ header of the Task matches the
                provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match header
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_task(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTask, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to fetch.
            sid: The SID of the Task resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTask],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_task(
        self,
        workspace_sid: str,
        *,
        priority: int | None = None,
        assignment_status: list[str] | None = None,
        workflow_sid: str | None = None,
        workflow_name: str | None = None,
        task_queue_sid: str | None = None,
        task_queue_name: str | None = None,
        evaluate_task_attributes: str | None = None,
        routing_target: str | None = None,
        ordering: str | None = None,
        has_addons: bool | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Tasks to read.
            priority: The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the
                specified priority.
            assignment_status: The ``assignment_status`` of the Tasks you want to read. Can be: ``pending``,
                ``reserved``, ``assigned``, ``canceled``, ``wrapping``, or ``completed``. Returns all Tasks in the
                Workspace with the specified ``assignment_status``.
            workflow_sid: The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow
                identified by this SID.
            workflow_name: The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the
                Workflow identified by this friendly name.
            task_queue_sid: The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue
                identified by this SID.
            task_queue_name: The ``friendly_name`` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in
                the TaskQueue identified by this friendly name.
            evaluate_task_attributes: The attributes of the Tasks to read. Returns the Tasks that match the attributes
                specified in this parameter.
            routing_target: A SID of a Worker, Queue, or Workflow to route a Task to
            ordering: How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated.
                This value is specified as: ``Attribute:Order``, where ``Attribute`` can be either ``DateCreated``,
                ``Priority``, or ``VirtualStartTime`` and ``Order`` can be either ``asc`` or ``desc``. For example,
                ``Priority:desc`` returns Tasks ordered in descending order of their Priority. Pairings of sort orders
                can be specified in a comma-separated list such as ``Priority:desc,DateCreated:asc``, which returns the
                Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not
                allowed is DateCreated and VirtualStartTime.
            has_addons: Whether to read Tasks with Add-ons. If ``true``, returns only Tasks with Add-ons. If ``false``,
                returns only Tasks without Add-ons.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[int | None]("Priority", priority),
                param[list[str] | None]("AssignmentStatus", assignment_status),
                param[str | None]("WorkflowSid", workflow_sid),
                param[str | None]("WorkflowName", workflow_name),
                param[str | None]("TaskQueueSid", task_queue_sid),
                param[str | None]("TaskQueueName", task_queue_name),
                param[str | None]("EvaluateTaskAttributes", evaluate_task_attributes),
                param[str | None]("RoutingTarget", routing_target),
                param[str | None]("Ordering", ordering),
                param[bool | None]("HasAddons", has_addons),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_task(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        attributes: str | None = None,
        assignment_status: TaskEnumStatusOrStr | None = None,
        reason: str | None = None,
        priority: int | None = None,
        task_channel: str | None = None,
        virtual_start_time: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTask, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Task to update.
            sid: The SID of the Task resource to update.
            if_match: If provided, applies this mutation if (and only if) the `ETag
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag>`__ header of the Task matches the
                provided value. This matches the semantics of (and is implemented with) the HTTP `If-Match header
                <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match>`__.
            attributes: The JSON string that describes the custom attributes of the task.
            assignment_status: The current status of the Task's assignment. Can be: ``pending``, ``reserved``,
                ``assigned``, ``canceled``, ``wrapping``, or ``completed``.
            reason: The reason that the Task was canceled or completed. This parameter is required only if the Task is
                canceled or completed. Setting this value queues the task for deletion and logs the reason.
            priority: The Task's new priority value. When supplied, the Task takes on the specified priority unless it
                matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
            task_channel: When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the
                TaskChannel's SID or its ``unique_name``, such as ``voice``, ``sms``, or ``default``.
            virtual_start_time: The task's new virtual start time value. When supplied, the Task takes on the specified
                virtual start time. Value can't be in the future or before the year of 1900.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Tasks/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match)],
            body=form_body(
                [
                    param[str | None]("Attributes", attributes),
                    param[TaskEnumStatusOrStr | None]("AssignmentStatus", assignment_status),
                    param[str | None]("Reason", reason),
                    param[int | None]("Priority", priority),
                    param[str | None]("TaskChannel", task_channel),
                    param[RFC3339DateTime | None]("VirtualStartTime", virtual_start_time),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTask],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
