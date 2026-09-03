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
from ..models.list_activity_response import ListActivityResponse
from ..models.taskrouter_v1_workspace_activity import TaskrouterV1WorkspaceActivity
from ..server.server import Server


class TaskrouterV1Activity:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1ActivityWithRawResponse(client, server, auth)

    def create_activity(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        available: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceActivity:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Activity belongs to.
            friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64
                characters long. These names are used to calculate and expose statistics about Workers, and provide
                visibility into the state of each Worker. Examples of friendly names include: ``on-call``, ``break``,
                and ``email``.
            available: Whether the Worker should be eligible to receive a Task when it occupies the Activity. A value of
                ``true``, ``1``, or ``yes`` specifies the Activity is available. All other values specify that it is
                not. The value cannot be changed after the Activity is created.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_activity(
            workspace_sid, friendly_name, available=available, request_options=request_options
        ).unwrap()

    def delete_activity(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to delete.
            sid: The SID of the Activity resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_activity(workspace_sid, sid, request_options=request_options).unwrap()

    def fetch_activity(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceActivity:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to fetch.
            sid: The SID of the Activity resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_activity(workspace_sid, sid, request_options=request_options).unwrap()

    def list_activity(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        available: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListActivityResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to read.
            friendly_name: The ``friendly_name`` of the Activity resources to read.
            available: Whether return only Activity resources that are available or unavailable. A value of ``true``
                returns only available activities. Values of '1' or ``yes`` also indicate ``true``. All other values
                represent ``false`` and return activities that are unavailable.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_activity(
            workspace_sid,
            friendly_name=friendly_name,
            available=available,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_activity(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceActivity:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to update.
            sid: The SID of the Activity resource to update.
            friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64
                characters long. These names are used to calculate and expose statistics about Workers, and provide
                visibility into the state of each Worker. Examples of friendly names include: ``on-call``, ``break``,
                and ``email``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_activity(
            workspace_sid, sid, friendly_name=friendly_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1ActivityWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1Activity:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1ActivityWithRawResponse(client, server, auth)

    async def create_activity(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        available: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceActivity:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Activity belongs to.
            friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64
                characters long. These names are used to calculate and expose statistics about Workers, and provide
                visibility into the state of each Worker. Examples of friendly names include: ``on-call``, ``break``,
                and ``email``.
            available: Whether the Worker should be eligible to receive a Task when it occupies the Activity. A value of
                ``true``, ``1``, or ``yes`` specifies the Activity is available. All other values specify that it is
                not. The value cannot be changed after the Activity is created.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_activity(
                workspace_sid, friendly_name, available=available, request_options=request_options
            )
        ).unwrap()

    async def delete_activity(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to delete.
            sid: The SID of the Activity resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_activity(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_activity(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceActivity:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to fetch.
            sid: The SID of the Activity resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_activity(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_activity(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        available: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListActivityResponse:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to read.
            friendly_name: The ``friendly_name`` of the Activity resources to read.
            available: Whether return only Activity resources that are available or unavailable. A value of ``true``
                returns only available activities. Values of '1' or ``yes`` also indicate ``true``. All other values
                represent ``false`` and return activities that are unavailable.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_activity(
                workspace_sid,
                friendly_name=friendly_name,
                available=available,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_activity(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceActivity:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to update.
            sid: The SID of the Activity resource to update.
            friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64
                characters long. These names are used to calculate and expose statistics about Workers, and provide
                visibility into the state of each Worker. Examples of friendly names include: ``on-call``, ``break``,
                and ``email``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_activity(
                workspace_sid, sid, friendly_name=friendly_name, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1ActivityWithRawResponse:
        return self._with_raw_response


class TaskrouterV1ActivityWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_activity(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        available: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceActivity, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Activity belongs to.
            friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64
                characters long. These names are used to calculate and expose statistics about Workers, and provide
                visibility into the state of each Worker. Examples of friendly names include: ``on-call``, ``break``,
                and ``email``.
            available: Whether the Worker should be eligible to receive a Task when it occupies the Activity. A value of
                ``true``, ``1``, or ``yes`` specifies the Activity is available. All other values specify that it is
                not. The value cannot be changed after the Activity is created.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("FriendlyName", friendly_name), param[bool | None]("Available", available)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceActivity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_activity(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to delete.
            sid: The SID of the Activity resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_activity(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceActivity, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to fetch.
            sid: The SID of the Activity resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceActivity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_activity(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        available: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListActivityResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to read.
            friendly_name: The ``friendly_name`` of the Activity resources to read.
            available: Whether return only Activity resources that are available or unavailable. A value of ``true``
                returns only available activities. Values of '1' or ``yes`` also indicate ``true``. All other values
                represent ``false`` and return activities that are unavailable.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("Available", available),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListActivityResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_activity(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceActivity, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to update.
            sid: The SID of the Activity resource to update.
            friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64
                characters long. These names are used to calculate and expose statistics about Workers, and provide
                visibility into the state of each Worker. Examples of friendly names include: ``on-call``, ``break``,
                and ``email``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceActivity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1ActivityWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_activity(
        self,
        workspace_sid: str,
        friendly_name: str,
        *,
        available: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceActivity, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace that the new Activity belongs to.
            friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64
                characters long. These names are used to calculate and expose statistics about Workers, and provide
                visibility into the state of each Worker. Examples of friendly names include: ``on-call``, ``break``,
                and ``email``.
            available: Whether the Worker should be eligible to receive a Task when it occupies the Activity. A value of
                ``true``, ``1``, or ``yes`` specifies the Activity is available. All other values specify that it is
                not. The value cannot be changed after the Activity is created.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str]("FriendlyName", friendly_name), param[bool | None]("Available", available)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceActivity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_activity(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to delete.
            sid: The SID of the Activity resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_activity(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceActivity, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to fetch.
            sid: The SID of the Activity resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceActivity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_activity(
        self,
        workspace_sid: str,
        *,
        friendly_name: str | None = None,
        available: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListActivityResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to read.
            friendly_name: The ``friendly_name`` of the Activity resources to read.
            available: Whether return only Activity resources that are available or unavailable. A value of ``true``
                returns only available activities. Values of '1' or ``yes`` also indicate ``true``. All other values
                represent ``false`` and return activities that are unavailable.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[str | None]("FriendlyName", friendly_name),
                param[str | None]("Available", available),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListActivityResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_activity(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceActivity, RawError]:
        """Send a ``POST`` request.

        Args:
            workspace_sid: The SID of the Workspace with the Activity resources to update.
            sid: The SID of the Activity resource to update.
            friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64
                characters long. These names are used to calculate and expose statistics about Workers, and provide
                visibility into the state of each Worker. Examples of friendly names include: ``on-call``, ``break``,
                and ``email``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/Activities/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[str | None]("FriendlyName", friendly_name)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceActivity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
