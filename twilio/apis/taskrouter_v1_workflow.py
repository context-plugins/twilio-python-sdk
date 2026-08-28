from __future__ import annotations

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
from ..models.list_workflow_response import ListWorkflowResponse
from ..models.taskrouter_v1_workspace_workflow import TaskrouterV1WorkspaceWorkflow
from ..server.server import Server


class TaskrouterV1Workflow:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1WorkflowWithRawResponse(client, server, auth)

    def create_workflow(
        self,
        workspace_sid: str,
        friendly_name: str,
        configuration: str,
        *,
        assignment_callback_url: str | None = None,
        fallback_assignment_callback_url: str | None = None,
        task_reservation_timeout: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkflow:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Workflow to create belongs to.
            friendly_name: A descriptive string that you create to describe the Workflow resource. For example,
                ``Inbound Call Workflow`` or ``2014 Outbound Campaign``.
            configuration: A JSON string that contains the rules to apply to the Workflow. See `Configuring Workflows
                <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information.
            assignment_callback_url: The URL from your application that will process task assignment events. See
                `Handling Task Assignment Callback
                <https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks>`__ for more details.
            fallback_assignment_callback_url: The URL that we should call when a call to the ``assignment_callback_url``
                fails.
            task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application
                after it assigns a Task to a Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_workflow(
            workspace_sid,
            friendly_name,
            configuration,
            assignment_callback_url=assignment_callback_url,
            fallback_assignment_callback_url=fallback_assignment_callback_url,
            task_reservation_timeout=task_reservation_timeout,
            request_options=request_options,
        ).unwrap()

    def delete_workflow(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to delete.
            sid: The SID of the Workflow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_workflow(workspace_sid, sid, request_options=request_options).unwrap()

    def fetch_workflow(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceWorkflow:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to fetch.
            sid: The SID of the Workflow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_workflow(workspace_sid, sid, request_options=request_options).unwrap()

    def list_workflow(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkflowResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to read.
            friendly_name: The ``friendly_name`` of the Workflow resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_workflow(
            workspace_sid,
            friendly_name=friendly_name,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_workflow(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        assignment_callback_url: str | None = None,
        fallback_assignment_callback_url: str | None = None,
        configuration: str | None = None,
        task_reservation_timeout: int | None = None,
        re_evaluate_tasks: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkflow:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to update.
            sid: The SID of the Workflow resource to update.
            friendly_name: A descriptive string that you create to describe the Workflow resource. For example,
                ``Inbound Call Workflow`` or ``2014 Outbound Campaign``.
            assignment_callback_url: The URL from your application that will process task assignment events. See
                `Handling Task Assignment Callback
                <https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks>`__ for more details.
            fallback_assignment_callback_url: The URL that we should call when a call to the ``assignment_callback_url``
                fails.
            configuration: A JSON string that contains the rules to apply to the Workflow. See `Configuring Workflows
                <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information.
            task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application
                after it assigns a Task to a Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``.
            re_evaluate_tasks: Whether or not to re-evaluate Tasks. The default is ``false``, which means Tasks in the
                Workflow will not be processed through the assignment loop again.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_workflow(
            workspace_sid,
            sid,
            friendly_name=friendly_name,
            assignment_callback_url=assignment_callback_url,
            fallback_assignment_callback_url=fallback_assignment_callback_url,
            configuration=configuration,
            task_reservation_timeout=task_reservation_timeout,
            re_evaluate_tasks=re_evaluate_tasks,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1WorkflowWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1Workflow:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1WorkflowWithRawResponse(client, server, auth)

    async def create_workflow(
        self,
        workspace_sid: str,
        friendly_name: str,
        configuration: str,
        *,
        assignment_callback_url: str | None = None,
        fallback_assignment_callback_url: str | None = None,
        task_reservation_timeout: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkflow:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Workflow to create belongs to.
            friendly_name: A descriptive string that you create to describe the Workflow resource. For example,
                ``Inbound Call Workflow`` or ``2014 Outbound Campaign``.
            configuration: A JSON string that contains the rules to apply to the Workflow. See `Configuring Workflows
                <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information.
            assignment_callback_url: The URL from your application that will process task assignment events. See
                `Handling Task Assignment Callback
                <https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks>`__ for more details.
            fallback_assignment_callback_url: The URL that we should call when a call to the ``assignment_callback_url``
                fails.
            task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application
                after it assigns a Task to a Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_workflow(
                workspace_sid,
                friendly_name,
                configuration,
                assignment_callback_url=assignment_callback_url,
                fallback_assignment_callback_url=fallback_assignment_callback_url,
                task_reservation_timeout=task_reservation_timeout,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_workflow(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to delete.
            sid: The SID of the Workflow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_workflow(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_workflow(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceWorkflow:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to fetch.
            sid: The SID of the Workflow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_workflow(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_workflow(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkflowResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to read.
            friendly_name: The ``friendly_name`` of the Workflow resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_workflow(
                workspace_sid,
                friendly_name=friendly_name,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_workflow(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        assignment_callback_url: str | None = None,
        fallback_assignment_callback_url: str | None = None,
        configuration: str | None = None,
        task_reservation_timeout: int | None = None,
        re_evaluate_tasks: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceWorkflow:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to update.
            sid: The SID of the Workflow resource to update.
            friendly_name: A descriptive string that you create to describe the Workflow resource. For example,
                ``Inbound Call Workflow`` or ``2014 Outbound Campaign``.
            assignment_callback_url: The URL from your application that will process task assignment events. See
                `Handling Task Assignment Callback
                <https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks>`__ for more details.
            fallback_assignment_callback_url: The URL that we should call when a call to the ``assignment_callback_url``
                fails.
            configuration: A JSON string that contains the rules to apply to the Workflow. See `Configuring Workflows
                <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information.
            task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application
                after it assigns a Task to a Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``.
            re_evaluate_tasks: Whether or not to re-evaluate Tasks. The default is ``false``, which means Tasks in the
                Workflow will not be processed through the assignment loop again.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_workflow(
                workspace_sid,
                sid,
                friendly_name=friendly_name,
                assignment_callback_url=assignment_callback_url,
                fallback_assignment_callback_url=fallback_assignment_callback_url,
                configuration=configuration,
                task_reservation_timeout=task_reservation_timeout,
                re_evaluate_tasks=re_evaluate_tasks,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1WorkflowWithRawResponse:
        return self._with_raw_response


class TaskrouterV1WorkflowWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_workflow(
        self,
        workspace_sid: str,
        friendly_name: str,
        configuration: str,
        *,
        assignment_callback_url: str | None = None,
        fallback_assignment_callback_url: str | None = None,
        task_reservation_timeout: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Workflow to create belongs to.
            friendly_name: A descriptive string that you create to describe the Workflow resource. For example,
                ``Inbound Call Workflow`` or ``2014 Outbound Campaign``.
            configuration: A JSON string that contains the rules to apply to the Workflow. See `Configuring Workflows
                <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information.
            assignment_callback_url: The URL from your application that will process task assignment events. See
                `Handling Task Assignment Callback
                <https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks>`__ for more details.
            fallback_assignment_callback_url: The URL that we should call when a call to the ``assignment_callback_url``
                fails.
            task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application
                after it assigns a Task to a Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Configuration", configuration),
                    param[str | None]("AssignmentCallbackUrl", assignment_callback_url),
                    param[str | None]("FallbackAssignmentCallbackUrl", fallback_assignment_callback_url),
                    param[int | None]("TaskReservationTimeout", task_reservation_timeout),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_workflow(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to delete.
            sid: The SID of the Workflow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_workflow(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to fetch.
            sid: The SID of the Workflow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_workflow(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkflowResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to read.
            friendly_name: The ``friendly_name`` of the Workflow resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWorkflowResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_workflow(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        assignment_callback_url: str | None = None,
        fallback_assignment_callback_url: str | None = None,
        configuration: str | None = None,
        task_reservation_timeout: int | None = None,
        re_evaluate_tasks: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to update.
            sid: The SID of the Workflow resource to update.
            friendly_name: A descriptive string that you create to describe the Workflow resource. For example,
                ``Inbound Call Workflow`` or ``2014 Outbound Campaign``.
            assignment_callback_url: The URL from your application that will process task assignment events. See
                `Handling Task Assignment Callback
                <https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks>`__ for more details.
            fallback_assignment_callback_url: The URL that we should call when a call to the ``assignment_callback_url``
                fails.
            configuration: A JSON string that contains the rules to apply to the Workflow. See `Configuring Workflows
                <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information.
            task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application
                after it assigns a Task to a Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``.
            re_evaluate_tasks: Whether or not to re-evaluate Tasks. The default is ``false``, which means Tasks in the
                Workflow will not be processed through the assignment loop again.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("AssignmentCallbackUrl", assignment_callback_url),
                    param[str | None]("FallbackAssignmentCallbackUrl", fallback_assignment_callback_url),
                    param[str | None]("Configuration", configuration),
                    param[int | None]("TaskReservationTimeout", task_reservation_timeout),
                    param[str | None]("ReEvaluateTasks", re_evaluate_tasks),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1WorkflowWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_workflow(
        self,
        workspace_sid: str,
        friendly_name: str,
        configuration: str,
        *,
        assignment_callback_url: str | None = None,
        fallback_assignment_callback_url: str | None = None,
        task_reservation_timeout: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Workflow to create belongs to.
            friendly_name: A descriptive string that you create to describe the Workflow resource. For example,
                ``Inbound Call Workflow`` or ``2014 Outbound Campaign``.
            configuration: A JSON string that contains the rules to apply to the Workflow. See `Configuring Workflows
                <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information.
            assignment_callback_url: The URL from your application that will process task assignment events. See
                `Handling Task Assignment Callback
                <https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks>`__ for more details.
            fallback_assignment_callback_url: The URL that we should call when a call to the ``assignment_callback_url``
                fails.
            task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application
                after it assigns a Task to a Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("Configuration", configuration),
                    param[str | None]("AssignmentCallbackUrl", assignment_callback_url),
                    param[str | None]("FallbackAssignmentCallbackUrl", fallback_assignment_callback_url),
                    param[int | None]("TaskReservationTimeout", task_reservation_timeout),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_workflow(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to delete.
            sid: The SID of the Workflow resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_workflow(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to fetch.
            sid: The SID of the Workflow resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_workflow(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkflowResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to read.
            friendly_name: The ``friendly_name`` of the Workflow resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListWorkflowResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_workflow(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        assignment_callback_url: str | None = None,
        fallback_assignment_callback_url: str | None = None,
        configuration: str | None = None,
        task_reservation_timeout: int | None = None,
        re_evaluate_tasks: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceWorkflow, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Workflow to update.
            sid: The SID of the Workflow resource to update.
            friendly_name: A descriptive string that you create to describe the Workflow resource. For example,
                ``Inbound Call Workflow`` or ``2014 Outbound Campaign``.
            assignment_callback_url: The URL from your application that will process task assignment events. See
                `Handling Task Assignment Callback
                <https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks>`__ for more details.
            fallback_assignment_callback_url: The URL that we should call when a call to the ``assignment_callback_url``
                fails.
            configuration: A JSON string that contains the rules to apply to the Workflow. See `Configuring Workflows
                <https://www.twilio.com/docs/taskrouter/workflow-configuration>`__ for more information.
            task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application
                after it assigns a Task to a Worker. Can be up to ``86,400`` (24 hours) and the default is ``120``.
            re_evaluate_tasks: Whether or not to re-evaluate Tasks. The default is ``false``, which means Tasks in the
                Workflow will not be processed through the assignment loop again.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Workflows/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("AssignmentCallbackUrl", assignment_callback_url),
                    param[str | None]("FallbackAssignmentCallbackUrl", fallback_assignment_callback_url),
                    param[str | None]("Configuration", configuration),
                    param[int | None]("TaskReservationTimeout", task_reservation_timeout),
                    param[str | None]("ReEvaluateTasks", re_evaluate_tasks),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceWorkflow],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
