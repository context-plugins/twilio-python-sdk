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
from ..models.enums.workspace_enum_queue_order import WorkspaceEnumQueueOrderOrStr
from ..models.list_workspace_response import ListWorkspaceResponse
from ..models.taskrouter_v1_workspace import TaskrouterV1Workspace
from ..server.server import Server


class TaskrouterV1WorkspaceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1WorkspaceApiWithRawResponse(client, server, auth)

    def create_workspace(
        self,
        friendly_name: str,
        *,
        event_callback_url: str | None = None,
        events_filter: str | None = None,
        multi_task_enabled: bool | None = None,
        template: str | None = None,
        prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1Workspace:
        """Send a ``POST`` request.

        Args:
            friendly_name: A descriptive string that you create to describe the Workspace resource. It can be up to 64
                characters long. For example: ``Customer Support`` or ``2014 Election Campaign``.
            event_callback_url: The URL we should call when an event occurs. If provided, the Workspace will publish
                events to this URL, for example, to collect data for reporting. See `Workspace Events
                <https://www.twilio.com/docs/taskrouter/api/event>`__ for more information. This parameter supports
                Twilio's `Webhooks (HTTP callbacks) Connection Overrides
                <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__.
            events_filter: The list of Workspace events for which to call event_callback_url. For example, if
                ``EventsFilter=task.created, task.canceled, worker.activity.update``, then TaskRouter will call
                event_callback_url only when a task is created, canceled, or a Worker activity is updated.
            multi_task_enabled: Whether to enable multi-tasking. Can be: ``true`` to enable multi-tasking, or ``false``
                to disable it. However, all workspaces should be created as multi-tasking. The default is ``true``.
                Multi-tasking allows Workers to handle multiple Tasks simultaneously. When enabled (``true``), each
                Worker can receive parallel reservations up to the per-channel maximums defined in the Workers section.
                In single-tasking mode (legacy mode), each Worker will only receive a new reservation when the previous
                task is completed. Learn more at `Multitasking <https://www.twilio.com/docs/taskrouter/multitasking>`__.
            template: An available template name. Can be: ``NONE`` or ``FIFO`` and the default is ``NONE``.
                Pre-configures the Workspace with the Workflow and Activities specified in the template. ``NONE`` will
                create a Workspace with only a set of default activities. ``FIFO`` will configure TaskRouter with a set
                of default activities and a single TaskQueue for first-in, first-out distribution, which can be useful
                when you are getting started with TaskRouter.
            prioritize_queue_order: The type of TaskQueue to prioritize when Workers are receiving Tasks from both types
                of TaskQueues. Can be: ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see
                `Queue Ordering <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_workspace(
            friendly_name,
            event_callback_url=event_callback_url,
            events_filter=events_filter,
            multi_task_enabled=multi_task_enabled,
            template=template,
            prioritize_queue_order=prioritize_queue_order,
            request_options=request_options,
        ).unwrap()

    def delete_workspace(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Send a ``DELETE`` request.

        Args:
            sid: The SID of the Workspace resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_workspace(sid, request_options=request_options).unwrap()

    def fetch_workspace(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1Workspace:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Workspace resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_workspace(sid, request_options=request_options).unwrap()

    def list_workspace(
        self,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkspaceResponse:
        """Send a ``GET`` request.

        Args:
            friendly_name: The ``friendly_name`` of the Workspace resources to read. For example ``Customer Support`` or
                ``2014 Election Campaign``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_workspace(
            friendly_name=friendly_name,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_workspace(
        self,
        sid: str,
        *,
        default_activity_sid: str | None = None,
        event_callback_url: str | None = None,
        events_filter: str | None = None,
        friendly_name: str | None = None,
        multi_task_enabled: bool | None = None,
        timeout_activity_sid: str | None = None,
        prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1Workspace:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Workspace resource to update.
            default_activity_sid: The SID of the Activity that will be used when new Workers are created in the
                Workspace.
            event_callback_url: The URL we should call when an event occurs. See `Workspace Events
                <https://www.twilio.com/docs/taskrouter/api/event>`__ for more information. This parameter supports
                Twilio's `Webhooks (HTTP callbacks) Connection Overrides
                <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__.
            events_filter: The list of Workspace events for which to call event_callback_url. For example if
                ``EventsFilter=task.created,task.canceled,worker.activity.update``, then TaskRouter will call
                event_callback_url only when a task is created, canceled, or a Worker activity is updated.
            friendly_name: A descriptive string that you create to describe the Workspace resource. For example: ``Sales
                Call Center`` or ``Customer Support Team``.
            multi_task_enabled: Whether to enable multi-tasking. Can be: ``true`` to enable multi-tasking, or ``false``
                to disable it. However, all workspaces should be maintained as multi-tasking. There is no default when
                omitting this parameter. A multi-tasking Workspace can't be updated to single-tasking unless it is not a
                Flex Project and another (legacy) single-tasking Workspace exists. Multi-tasking allows Workers to
                handle multiple Tasks simultaneously. In multi-tasking mode, each Worker can receive parallel
                reservations up to the per-channel maximums defined in the Workers section. In single-tasking mode
                (legacy mode), each Worker will only receive a new reservation when the previous task is completed.
                Learn more at `Multitasking <https://www.twilio.com/docs/taskrouter/multitasking>`__.
            timeout_activity_sid: The SID of the Activity that will be assigned to a Worker when a Task reservation
                times out without a response.
            prioritize_queue_order: The type of TaskQueue to prioritize when Workers are receiving Tasks from both types
                of TaskQueues. Can be: ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see
                `Queue Ordering <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_workspace(
            sid,
            default_activity_sid=default_activity_sid,
            event_callback_url=event_callback_url,
            events_filter=events_filter,
            friendly_name=friendly_name,
            multi_task_enabled=multi_task_enabled,
            timeout_activity_sid=timeout_activity_sid,
            prioritize_queue_order=prioritize_queue_order,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1WorkspaceApiWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1WorkspaceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1WorkspaceApiWithRawResponse(client, server, auth)

    async def create_workspace(
        self,
        friendly_name: str,
        *,
        event_callback_url: str | None = None,
        events_filter: str | None = None,
        multi_task_enabled: bool | None = None,
        template: str | None = None,
        prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1Workspace:
        """Send a ``POST`` request.

        Args:
            friendly_name: A descriptive string that you create to describe the Workspace resource. It can be up to 64
                characters long. For example: ``Customer Support`` or ``2014 Election Campaign``.
            event_callback_url: The URL we should call when an event occurs. If provided, the Workspace will publish
                events to this URL, for example, to collect data for reporting. See `Workspace Events
                <https://www.twilio.com/docs/taskrouter/api/event>`__ for more information. This parameter supports
                Twilio's `Webhooks (HTTP callbacks) Connection Overrides
                <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__.
            events_filter: The list of Workspace events for which to call event_callback_url. For example, if
                ``EventsFilter=task.created, task.canceled, worker.activity.update``, then TaskRouter will call
                event_callback_url only when a task is created, canceled, or a Worker activity is updated.
            multi_task_enabled: Whether to enable multi-tasking. Can be: ``true`` to enable multi-tasking, or ``false``
                to disable it. However, all workspaces should be created as multi-tasking. The default is ``true``.
                Multi-tasking allows Workers to handle multiple Tasks simultaneously. When enabled (``true``), each
                Worker can receive parallel reservations up to the per-channel maximums defined in the Workers section.
                In single-tasking mode (legacy mode), each Worker will only receive a new reservation when the previous
                task is completed. Learn more at `Multitasking <https://www.twilio.com/docs/taskrouter/multitasking>`__.
            template: An available template name. Can be: ``NONE`` or ``FIFO`` and the default is ``NONE``.
                Pre-configures the Workspace with the Workflow and Activities specified in the template. ``NONE`` will
                create a Workspace with only a set of default activities. ``FIFO`` will configure TaskRouter with a set
                of default activities and a single TaskQueue for first-in, first-out distribution, which can be useful
                when you are getting started with TaskRouter.
            prioritize_queue_order: The type of TaskQueue to prioritize when Workers are receiving Tasks from both types
                of TaskQueues. Can be: ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see
                `Queue Ordering <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_workspace(
                friendly_name,
                event_callback_url=event_callback_url,
                events_filter=events_filter,
                multi_task_enabled=multi_task_enabled,
                template=template,
                prioritize_queue_order=prioritize_queue_order,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_workspace(self, sid: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Send a ``DELETE`` request.

        Args:
            sid: The SID of the Workspace resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_workspace(sid, request_options=request_options)).unwrap()

    async def fetch_workspace(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1Workspace:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Workspace resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_workspace(sid, request_options=request_options)).unwrap()

    async def list_workspace(
        self,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkspaceResponse:
        """Send a ``GET`` request.

        Args:
            friendly_name: The ``friendly_name`` of the Workspace resources to read. For example ``Customer Support`` or
                ``2014 Election Campaign``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_workspace(
                friendly_name=friendly_name,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_workspace(
        self,
        sid: str,
        *,
        default_activity_sid: str | None = None,
        event_callback_url: str | None = None,
        events_filter: str | None = None,
        friendly_name: str | None = None,
        multi_task_enabled: bool | None = None,
        timeout_activity_sid: str | None = None,
        prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1Workspace:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Workspace resource to update.
            default_activity_sid: The SID of the Activity that will be used when new Workers are created in the
                Workspace.
            event_callback_url: The URL we should call when an event occurs. See `Workspace Events
                <https://www.twilio.com/docs/taskrouter/api/event>`__ for more information. This parameter supports
                Twilio's `Webhooks (HTTP callbacks) Connection Overrides
                <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__.
            events_filter: The list of Workspace events for which to call event_callback_url. For example if
                ``EventsFilter=task.created,task.canceled,worker.activity.update``, then TaskRouter will call
                event_callback_url only when a task is created, canceled, or a Worker activity is updated.
            friendly_name: A descriptive string that you create to describe the Workspace resource. For example: ``Sales
                Call Center`` or ``Customer Support Team``.
            multi_task_enabled: Whether to enable multi-tasking. Can be: ``true`` to enable multi-tasking, or ``false``
                to disable it. However, all workspaces should be maintained as multi-tasking. There is no default when
                omitting this parameter. A multi-tasking Workspace can't be updated to single-tasking unless it is not a
                Flex Project and another (legacy) single-tasking Workspace exists. Multi-tasking allows Workers to
                handle multiple Tasks simultaneously. In multi-tasking mode, each Worker can receive parallel
                reservations up to the per-channel maximums defined in the Workers section. In single-tasking mode
                (legacy mode), each Worker will only receive a new reservation when the previous task is completed.
                Learn more at `Multitasking <https://www.twilio.com/docs/taskrouter/multitasking>`__.
            timeout_activity_sid: The SID of the Activity that will be assigned to a Worker when a Task reservation
                times out without a response.
            prioritize_queue_order: The type of TaskQueue to prioritize when Workers are receiving Tasks from both types
                of TaskQueues. Can be: ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see
                `Queue Ordering <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_workspace(
                sid,
                default_activity_sid=default_activity_sid,
                event_callback_url=event_callback_url,
                events_filter=events_filter,
                friendly_name=friendly_name,
                multi_task_enabled=multi_task_enabled,
                timeout_activity_sid=timeout_activity_sid,
                prioritize_queue_order=prioritize_queue_order,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1WorkspaceApiWithRawResponse:
        return self._with_raw_response


class TaskrouterV1WorkspaceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_workspace(
        self,
        friendly_name: str,
        *,
        event_callback_url: str | None = None,
        events_filter: str | None = None,
        multi_task_enabled: bool | None = None,
        template: str | None = None,
        prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1Workspace, RawError]:
        """Send a ``POST`` request.

        Args:
            friendly_name: A descriptive string that you create to describe the Workspace resource. It can be up to 64
                characters long. For example: ``Customer Support`` or ``2014 Election Campaign``.
            event_callback_url: The URL we should call when an event occurs. If provided, the Workspace will publish
                events to this URL, for example, to collect data for reporting. See `Workspace Events
                <https://www.twilio.com/docs/taskrouter/api/event>`__ for more information. This parameter supports
                Twilio's `Webhooks (HTTP callbacks) Connection Overrides
                <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__.
            events_filter: The list of Workspace events for which to call event_callback_url. For example, if
                ``EventsFilter=task.created, task.canceled, worker.activity.update``, then TaskRouter will call
                event_callback_url only when a task is created, canceled, or a Worker activity is updated.
            multi_task_enabled: Whether to enable multi-tasking. Can be: ``true`` to enable multi-tasking, or ``false``
                to disable it. However, all workspaces should be created as multi-tasking. The default is ``true``.
                Multi-tasking allows Workers to handle multiple Tasks simultaneously. When enabled (``true``), each
                Worker can receive parallel reservations up to the per-channel maximums defined in the Workers section.
                In single-tasking mode (legacy mode), each Worker will only receive a new reservation when the previous
                task is completed. Learn more at `Multitasking <https://www.twilio.com/docs/taskrouter/multitasking>`__.
            template: An available template name. Can be: ``NONE`` or ``FIFO`` and the default is ``NONE``.
                Pre-configures the Workspace with the Workflow and Activities specified in the template. ``NONE`` will
                create a Workspace with only a set of default activities. ``FIFO`` will configure TaskRouter with a set
                of default activities and a single TaskQueue for first-in, first-out distribution, which can be useful
                when you are getting started with TaskRouter.
            prioritize_queue_order: The type of TaskQueue to prioritize when Workers are receiving Tasks from both types
                of TaskQueues. Can be: ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see
                `Queue Ordering <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str | None]("EventCallbackUrl", event_callback_url),
                    param[str | None]("EventsFilter", events_filter),
                    param[bool | None]("MultiTaskEnabled", multi_task_enabled),
                    param[str | None]("Template", template),
                    param[WorkspaceEnumQueueOrderOrStr | None]("PrioritizeQueueOrder", prioritize_queue_order),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1Workspace],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_workspace(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            sid: The SID of the Workspace resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_workspace(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1Workspace, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Workspace resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1Workspace],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_workspace(
        self,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkspaceResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            friendly_name: The ``friendly_name`` of the Workspace resources to read. For example ``Customer Support`` or
                ``2014 Election Campaign``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces"),
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWorkspaceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_workspace(
        self,
        sid: str,
        *,
        default_activity_sid: str | None = None,
        event_callback_url: str | None = None,
        events_filter: str | None = None,
        friendly_name: str | None = None,
        multi_task_enabled: bool | None = None,
        timeout_activity_sid: str | None = None,
        prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1Workspace, RawError]:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Workspace resource to update.
            default_activity_sid: The SID of the Activity that will be used when new Workers are created in the
                Workspace.
            event_callback_url: The URL we should call when an event occurs. See `Workspace Events
                <https://www.twilio.com/docs/taskrouter/api/event>`__ for more information. This parameter supports
                Twilio's `Webhooks (HTTP callbacks) Connection Overrides
                <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__.
            events_filter: The list of Workspace events for which to call event_callback_url. For example if
                ``EventsFilter=task.created,task.canceled,worker.activity.update``, then TaskRouter will call
                event_callback_url only when a task is created, canceled, or a Worker activity is updated.
            friendly_name: A descriptive string that you create to describe the Workspace resource. For example: ``Sales
                Call Center`` or ``Customer Support Team``.
            multi_task_enabled: Whether to enable multi-tasking. Can be: ``true`` to enable multi-tasking, or ``false``
                to disable it. However, all workspaces should be maintained as multi-tasking. There is no default when
                omitting this parameter. A multi-tasking Workspace can't be updated to single-tasking unless it is not a
                Flex Project and another (legacy) single-tasking Workspace exists. Multi-tasking allows Workers to
                handle multiple Tasks simultaneously. In multi-tasking mode, each Worker can receive parallel
                reservations up to the per-channel maximums defined in the Workers section. In single-tasking mode
                (legacy mode), each Worker will only receive a new reservation when the previous task is completed.
                Learn more at `Multitasking <https://www.twilio.com/docs/taskrouter/multitasking>`__.
            timeout_activity_sid: The SID of the Activity that will be assigned to a Worker when a Task reservation
                times out without a response.
            prioritize_queue_order: The type of TaskQueue to prioritize when Workers are receiving Tasks from both types
                of TaskQueues. Can be: ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see
                `Queue Ordering <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("DefaultActivitySid", default_activity_sid),
                    param[str | None]("EventCallbackUrl", event_callback_url),
                    param[str | None]("EventsFilter", events_filter),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("MultiTaskEnabled", multi_task_enabled),
                    param[str | None]("TimeoutActivitySid", timeout_activity_sid),
                    param[WorkspaceEnumQueueOrderOrStr | None]("PrioritizeQueueOrder", prioritize_queue_order),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1Workspace],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1WorkspaceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_workspace(
        self,
        friendly_name: str,
        *,
        event_callback_url: str | None = None,
        events_filter: str | None = None,
        multi_task_enabled: bool | None = None,
        template: str | None = None,
        prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1Workspace, RawError]:
        """Send a ``POST`` request.

        Args:
            friendly_name: A descriptive string that you create to describe the Workspace resource. It can be up to 64
                characters long. For example: ``Customer Support`` or ``2014 Election Campaign``.
            event_callback_url: The URL we should call when an event occurs. If provided, the Workspace will publish
                events to this URL, for example, to collect data for reporting. See `Workspace Events
                <https://www.twilio.com/docs/taskrouter/api/event>`__ for more information. This parameter supports
                Twilio's `Webhooks (HTTP callbacks) Connection Overrides
                <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__.
            events_filter: The list of Workspace events for which to call event_callback_url. For example, if
                ``EventsFilter=task.created, task.canceled, worker.activity.update``, then TaskRouter will call
                event_callback_url only when a task is created, canceled, or a Worker activity is updated.
            multi_task_enabled: Whether to enable multi-tasking. Can be: ``true`` to enable multi-tasking, or ``false``
                to disable it. However, all workspaces should be created as multi-tasking. The default is ``true``.
                Multi-tasking allows Workers to handle multiple Tasks simultaneously. When enabled (``true``), each
                Worker can receive parallel reservations up to the per-channel maximums defined in the Workers section.
                In single-tasking mode (legacy mode), each Worker will only receive a new reservation when the previous
                task is completed. Learn more at `Multitasking <https://www.twilio.com/docs/taskrouter/multitasking>`__.
            template: An available template name. Can be: ``NONE`` or ``FIFO`` and the default is ``NONE``.
                Pre-configures the Workspace with the Workflow and Activities specified in the template. ``NONE`` will
                create a Workspace with only a set of default activities. ``FIFO`` will configure TaskRouter with a set
                of default activities and a single TaskQueue for first-in, first-out distribution, which can be useful
                when you are getting started with TaskRouter.
            prioritize_queue_order: The type of TaskQueue to prioritize when Workers are receiving Tasks from both types
                of TaskQueues. Can be: ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see
                `Queue Ordering <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str | None]("EventCallbackUrl", event_callback_url),
                    param[str | None]("EventsFilter", events_filter),
                    param[bool | None]("MultiTaskEnabled", multi_task_enabled),
                    param[str | None]("Template", template),
                    param[WorkspaceEnumQueueOrderOrStr | None]("PrioritizeQueueOrder", prioritize_queue_order),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1Workspace],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_workspace(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            sid: The SID of the Workspace resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_workspace(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1Workspace, RawError]:
        """Send a ``GET`` request.

        Args:
            sid: The SID of the Workspace resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1Workspace],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_workspace(
        self,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkspaceResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            friendly_name: The ``friendly_name`` of the Workspace resources to read. For example ``Customer Support`` or
                ``2014 Election Campaign``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces"),
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWorkspaceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_workspace(
        self,
        sid: str,
        *,
        default_activity_sid: str | None = None,
        event_callback_url: str | None = None,
        events_filter: str | None = None,
        friendly_name: str | None = None,
        multi_task_enabled: bool | None = None,
        timeout_activity_sid: str | None = None,
        prioritize_queue_order: WorkspaceEnumQueueOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1Workspace, RawError]:
        """Send a ``POST`` request.

        Args:
            sid: The SID of the Workspace resource to update.
            default_activity_sid: The SID of the Activity that will be used when new Workers are created in the
                Workspace.
            event_callback_url: The URL we should call when an event occurs. See `Workspace Events
                <https://www.twilio.com/docs/taskrouter/api/event>`__ for more information. This parameter supports
                Twilio's `Webhooks (HTTP callbacks) Connection Overrides
                <https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides>`__.
            events_filter: The list of Workspace events for which to call event_callback_url. For example if
                ``EventsFilter=task.created,task.canceled,worker.activity.update``, then TaskRouter will call
                event_callback_url only when a task is created, canceled, or a Worker activity is updated.
            friendly_name: A descriptive string that you create to describe the Workspace resource. For example: ``Sales
                Call Center`` or ``Customer Support Team``.
            multi_task_enabled: Whether to enable multi-tasking. Can be: ``true`` to enable multi-tasking, or ``false``
                to disable it. However, all workspaces should be maintained as multi-tasking. There is no default when
                omitting this parameter. A multi-tasking Workspace can't be updated to single-tasking unless it is not a
                Flex Project and another (legacy) single-tasking Workspace exists. Multi-tasking allows Workers to
                handle multiple Tasks simultaneously. In multi-tasking mode, each Worker can receive parallel
                reservations up to the per-channel maximums defined in the Workers section. In single-tasking mode
                (legacy mode), each Worker will only receive a new reservation when the previous task is completed.
                Learn more at `Multitasking <https://www.twilio.com/docs/taskrouter/multitasking>`__.
            timeout_activity_sid: The SID of the Activity that will be assigned to a Worker when a Task reservation
                times out without a response.
            prioritize_queue_order: The type of TaskQueue to prioritize when Workers are receiving Tasks from both types
                of TaskQueues. Can be: ``LIFO`` or ``FIFO`` and the default is ``FIFO``. For more information, see
                `Queue Ordering <https://www.twilio.com/docs/taskrouter/queue-ordering-last-first-out-lifo>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("DefaultActivitySid", default_activity_sid),
                    param[str | None]("EventCallbackUrl", event_callback_url),
                    param[str | None]("EventsFilter", events_filter),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("MultiTaskEnabled", multi_task_enabled),
                    param[str | None]("TimeoutActivitySid", timeout_activity_sid),
                    param[WorkspaceEnumQueueOrderOrStr | None]("PrioritizeQueueOrder", prioritize_queue_order),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1Workspace],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
