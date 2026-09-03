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
from ..models.list_worker_response import ListWorkerResponse
from ..models.taskrouter_v1_workspace_worker import TaskrouterV1WorkspaceWorker
from ..server.server import Server


class TaskrouterV1Worker:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1WorkerWithRawResponse(client, server, auth)

    def create_worker(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        activity_sid: str | None = None,
        attributes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorker:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Worker belongs to.
            friendly_name: A descriptive string that you create to describe the new Worker. It can be up to 64
                characters long.
            activity_sid: The SID of a valid Activity that will describe the new Worker's initial state. See `Activities
                <https://www.twilio.com/docs/taskrouter/api/activity>`__ for more information. If not provided, the new
                Worker's initial state is the ``default_activity_sid`` configured on the Workspace.
            attributes: A valid JSON string that describes the new Worker. For example: ``{ "email": "Bob@example.com",
                "phone": "+5095551234" }``. This data is passed to the ``assignment_callback_url`` when TaskRouter
                assigns a Task to the Worker. Defaults to {}.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_worker(
            workspace_sid,
            friendly_name,
            activity_sid=activity_sid,
            attributes=attributes,
            request_options=request_options,
        ).unwrap()

    def delete_worker(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to delete.
            sid: The SID of the Worker resource to delete.
            if_match: The If-Match HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_worker(
            workspace_sid, sid, if_match=if_match, request_options=request_options
        ).unwrap()

    def fetch_worker(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceWorker:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to fetch.
            sid: The SID of the Worker resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_worker(workspace_sid, sid, request_options=request_options).unwrap()

    def list_worker(
        self,
        workspace_sid: str,
        *,
        activity_name: str | None = None,
        activity_sid: str | None = None,
        available: str | None = None,
        friendly_name: str | None = None,
        target_workers_expression: str | None = None,
        task_queue_name: str | None = None,
        task_queue_sid: str | None = None,
        ordering: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkerResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workers to read.
            activity_name: The ``activity_name`` of the Worker resources to read.
            activity_sid: The ``activity_sid`` of the Worker resources to read.
            available: Whether to return only Worker resources that are available or unavailable. Can be ``true``,
                ``1``, or ``yes`` to return Worker resources that are available, and ``false``, or any value returns the
                Worker resources that are not available.
            friendly_name: The ``friendly_name`` of the Worker resources to read.
            target_workers_expression: Filter by Workers that would match an expression. In addition to fields in the
                workers' attributes, the expression can include the following worker fields: ``sid``, ``friendly_name``,
                ``activity_sid``, or ``activity_name``
            task_queue_name: The ``friendly_name`` of the TaskQueue that the Workers to read are eligible for.
            task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for.
            ordering: Sorting parameter for Workers
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_worker(
            workspace_sid,
            activity_name=activity_name,
            activity_sid=activity_sid,
            available=available,
            friendly_name=friendly_name,
            target_workers_expression=target_workers_expression,
            task_queue_name=task_queue_name,
            task_queue_sid=task_queue_sid,
            ordering=ordering,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_worker(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        activity_sid: str | None = None,
        attributes: str | None = None,
        friendly_name: str | None = None,
        reject_pending_reservations: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorker:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to update.
            sid: The SID of the Worker resource to update.
            if_match: The If-Match HTTP request header
            activity_sid: The SID of a valid Activity that will describe the Worker's initial state. See `Activities
                <https://www.twilio.com/docs/taskrouter/api/activity>`__ for more information.
            attributes: The JSON string that describes the Worker. For example: ``{ "email": "Bob@example.com", "phone":
                "+5095551234" }``. This data is passed to the ``assignment_callback_url`` when TaskRouter assigns a Task
                to the Worker. Defaults to {}.
            friendly_name: A descriptive string that you create to describe the Worker. It can be up to 64 characters
                long.
            reject_pending_reservations: Whether to reject the Worker's pending reservations. This option is only valid
                if the Worker's new `Activity <https://www.twilio.com/docs/taskrouter/api/activity>`__ resource has its
                ``availability`` property set to ``False``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_worker(
            workspace_sid,
            sid,
            if_match=if_match,
            activity_sid=activity_sid,
            attributes=attributes,
            friendly_name=friendly_name,
            reject_pending_reservations=reject_pending_reservations,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1WorkerWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1Worker:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1WorkerWithRawResponse(client, server, auth)

    async def create_worker(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        activity_sid: str | None = None,
        attributes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorker:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Worker belongs to.
            friendly_name: A descriptive string that you create to describe the new Worker. It can be up to 64
                characters long.
            activity_sid: The SID of a valid Activity that will describe the new Worker's initial state. See `Activities
                <https://www.twilio.com/docs/taskrouter/api/activity>`__ for more information. If not provided, the new
                Worker's initial state is the ``default_activity_sid`` configured on the Workspace.
            attributes: A valid JSON string that describes the new Worker. For example: ``{ "email": "Bob@example.com",
                "phone": "+5095551234" }``. This data is passed to the ``assignment_callback_url`` when TaskRouter
                assigns a Task to the Worker. Defaults to {}.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_worker(
                workspace_sid,
                friendly_name,
                activity_sid=activity_sid,
                attributes=attributes,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_worker(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to delete.
            sid: The SID of the Worker resource to delete.
            if_match: The If-Match HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_worker(
                workspace_sid, sid, if_match=if_match, request_options=request_options
            )
        ).unwrap()

    async def fetch_worker(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceWorker:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to fetch.
            sid: The SID of the Worker resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_worker(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_worker(
        self,
        workspace_sid: str,
        *,
        activity_name: str | None = None,
        activity_sid: str | None = None,
        available: str | None = None,
        friendly_name: str | None = None,
        target_workers_expression: str | None = None,
        task_queue_name: str | None = None,
        task_queue_sid: str | None = None,
        ordering: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkerResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workers to read.
            activity_name: The ``activity_name`` of the Worker resources to read.
            activity_sid: The ``activity_sid`` of the Worker resources to read.
            available: Whether to return only Worker resources that are available or unavailable. Can be ``true``,
                ``1``, or ``yes`` to return Worker resources that are available, and ``false``, or any value returns the
                Worker resources that are not available.
            friendly_name: The ``friendly_name`` of the Worker resources to read.
            target_workers_expression: Filter by Workers that would match an expression. In addition to fields in the
                workers' attributes, the expression can include the following worker fields: ``sid``, ``friendly_name``,
                ``activity_sid``, or ``activity_name``
            task_queue_name: The ``friendly_name`` of the TaskQueue that the Workers to read are eligible for.
            task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for.
            ordering: Sorting parameter for Workers
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_worker(
                workspace_sid,
                activity_name=activity_name,
                activity_sid=activity_sid,
                available=available,
                friendly_name=friendly_name,
                target_workers_expression=target_workers_expression,
                task_queue_name=task_queue_name,
                task_queue_sid=task_queue_sid,
                ordering=ordering,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_worker(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        activity_sid: str | None = None,
        attributes: str | None = None,
        friendly_name: str | None = None,
        reject_pending_reservations: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorker:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to update.
            sid: The SID of the Worker resource to update.
            if_match: The If-Match HTTP request header
            activity_sid: The SID of a valid Activity that will describe the Worker's initial state. See `Activities
                <https://www.twilio.com/docs/taskrouter/api/activity>`__ for more information.
            attributes: The JSON string that describes the Worker. For example: ``{ "email": "Bob@example.com", "phone":
                "+5095551234" }``. This data is passed to the ``assignment_callback_url`` when TaskRouter assigns a Task
                to the Worker. Defaults to {}.
            friendly_name: A descriptive string that you create to describe the Worker. It can be up to 64 characters
                long.
            reject_pending_reservations: Whether to reject the Worker's pending reservations. This option is only valid
                if the Worker's new `Activity <https://www.twilio.com/docs/taskrouter/api/activity>`__ resource has its
                ``availability`` property set to ``False``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_worker(
                workspace_sid,
                sid,
                if_match=if_match,
                activity_sid=activity_sid,
                attributes=attributes,
                friendly_name=friendly_name,
                reject_pending_reservations=reject_pending_reservations,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1WorkerWithRawResponse:
        return self._with_raw_response


class TaskrouterV1WorkerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_worker(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        activity_sid: str | None = None,
        attributes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorker, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Worker belongs to.
            friendly_name: A descriptive string that you create to describe the new Worker. It can be up to 64
                characters long.
            activity_sid: The SID of a valid Activity that will describe the new Worker's initial state. See `Activities
                <https://www.twilio.com/docs/taskrouter/api/activity>`__ for more information. If not provided, the new
                Worker's initial state is the ``default_activity_sid`` configured on the Workspace.
            attributes: A valid JSON string that describes the new Worker. For example: ``{ "email": "Bob@example.com",
                "phone": "+5095551234" }``. This data is passed to the ``assignment_callback_url`` when TaskRouter
                assigns a Task to the Worker. Defaults to {}.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str | None]("ActivitySid", activity_sid),
                    param[str | None]("Attributes", attributes),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorker],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_worker(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to delete.
            sid: The SID of the Worker resource to delete.
            if_match: The If-Match HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_worker(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceWorker, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to fetch.
            sid: The SID of the Worker resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorker],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_worker(
        self,
        workspace_sid: str,
        *,
        activity_name: str | None = None,
        activity_sid: str | None = None,
        available: str | None = None,
        friendly_name: str | None = None,
        target_workers_expression: str | None = None,
        task_queue_name: str | None = None,
        task_queue_sid: str | None = None,
        ordering: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkerResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workers to read.
            activity_name: The ``activity_name`` of the Worker resources to read.
            activity_sid: The ``activity_sid`` of the Worker resources to read.
            available: Whether to return only Worker resources that are available or unavailable. Can be ``true``,
                ``1``, or ``yes`` to return Worker resources that are available, and ``false``, or any value returns the
                Worker resources that are not available.
            friendly_name: The ``friendly_name`` of the Worker resources to read.
            target_workers_expression: Filter by Workers that would match an expression. In addition to fields in the
                workers' attributes, the expression can include the following worker fields: ``sid``, ``friendly_name``,
                ``activity_sid``, or ``activity_name``
            task_queue_name: The ``friendly_name`` of the TaskQueue that the Workers to read are eligible for.
            task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for.
            ordering: Sorting parameter for Workers
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[str | None]("ActivityName", activity_name),
                param[str | None]("ActivitySid", activity_sid),
                param[str | None]("Available", available),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("TargetWorkersExpression", target_workers_expression),
                param[str | None]("TaskQueueName", task_queue_name),
                param[str | None]("TaskQueueSid", task_queue_sid),
                param[str | None]("Ordering", ordering),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWorkerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_worker(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        activity_sid: str | None = None,
        attributes: str | None = None,
        friendly_name: str | None = None,
        reject_pending_reservations: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorker, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to update.
            sid: The SID of the Worker resource to update.
            if_match: The If-Match HTTP request header
            activity_sid: The SID of a valid Activity that will describe the Worker's initial state. See `Activities
                <https://www.twilio.com/docs/taskrouter/api/activity>`__ for more information.
            attributes: The JSON string that describes the Worker. For example: ``{ "email": "Bob@example.com", "phone":
                "+5095551234" }``. This data is passed to the ``assignment_callback_url`` when TaskRouter assigns a Task
                to the Worker. Defaults to {}.
            friendly_name: A descriptive string that you create to describe the Worker. It can be up to 64 characters
                long.
            reject_pending_reservations: Whether to reject the Worker's pending reservations. This option is only valid
                if the Worker's new `Activity <https://www.twilio.com/docs/taskrouter/api/activity>`__ resource has its
                ``availability`` property set to ``False``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("ActivitySid", activity_sid),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("RejectPendingReservations", reject_pending_reservations),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorker],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1WorkerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_worker(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        activity_sid: str | None = None,
        attributes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorker, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Worker belongs to.
            friendly_name: A descriptive string that you create to describe the new Worker. It can be up to 64
                characters long.
            activity_sid: The SID of a valid Activity that will describe the new Worker's initial state. See `Activities
                <https://www.twilio.com/docs/taskrouter/api/activity>`__ for more information. If not provided, the new
                Worker's initial state is the ``default_activity_sid`` configured on the Workspace.
            attributes: A valid JSON string that describes the new Worker. For example: ``{ "email": "Bob@example.com",
                "phone": "+5095551234" }``. This data is passed to the ``assignment_callback_url`` when TaskRouter
                assigns a Task to the Worker. Defaults to {}.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str | None]("ActivitySid", activity_sid),
                    param[str | None]("Attributes", attributes),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorker],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_worker(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to delete.
            sid: The SID of the Worker resource to delete.
            if_match: The If-Match HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_worker(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceWorker, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to fetch.
            sid: The SID of the Worker resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorker],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_worker(
        self,
        workspace_sid: str,
        *,
        activity_name: str | None = None,
        activity_sid: str | None = None,
        available: str | None = None,
        friendly_name: str | None = None,
        target_workers_expression: str | None = None,
        task_queue_name: str | None = None,
        task_queue_sid: str | None = None,
        ordering: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkerResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workers to read.
            activity_name: The ``activity_name`` of the Worker resources to read.
            activity_sid: The ``activity_sid`` of the Worker resources to read.
            available: Whether to return only Worker resources that are available or unavailable. Can be ``true``,
                ``1``, or ``yes`` to return Worker resources that are available, and ``false``, or any value returns the
                Worker resources that are not available.
            friendly_name: The ``friendly_name`` of the Worker resources to read.
            target_workers_expression: Filter by Workers that would match an expression. In addition to fields in the
                workers' attributes, the expression can include the following worker fields: ``sid``, ``friendly_name``,
                ``activity_sid``, or ``activity_name``
            task_queue_name: The ``friendly_name`` of the TaskQueue that the Workers to read are eligible for.
            task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for.
            ordering: Sorting parameter for Workers
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[str | None]("ActivityName", activity_name),
                param[str | None]("ActivitySid", activity_sid),
                param[str | None]("Available", available),
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("TargetWorkersExpression", target_workers_expression),
                param[str | None]("TaskQueueName", task_queue_name),
                param[str | None]("TaskQueueSid", task_queue_sid),
                param[str | None]("Ordering", ordering),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWorkerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_worker(
        self,
        workspace_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        activity_sid: str | None = None,
        attributes: str | None = None,
        friendly_name: str | None = None,
        reject_pending_reservations: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorker, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Worker to update.
            sid: The SID of the Worker resource to update.
            if_match: The If-Match HTTP request header
            activity_sid: The SID of a valid Activity that will describe the Worker's initial state. See `Activities
                <https://www.twilio.com/docs/taskrouter/api/activity>`__ for more information.
            attributes: The JSON string that describes the Worker. For example: ``{ "email": "Bob@example.com", "phone":
                "+5095551234" }``. This data is passed to the ``assignment_callback_url`` when TaskRouter assigns a Task
                to the Worker. Defaults to {}.
            friendly_name: A descriptive string that you create to describe the Worker. It can be up to 64 characters
                long.
            reject_pending_reservations: Whether to reject the Worker's pending reservations. This option is only valid
                if the Worker's new `Activity <https://www.twilio.com/docs/taskrouter/api/activity>`__ resource has its
                ``availability`` property set to ``False``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workers/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("ActivitySid", activity_sid),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("RejectPendingReservations", reject_pending_reservations),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorker],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
