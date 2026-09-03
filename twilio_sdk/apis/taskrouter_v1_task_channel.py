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
from ..models.list_task_channel_response import ListTaskChannelResponse
from ..models.taskrouter_v1_workspace_task_channel import TaskrouterV1WorkspaceTaskChannel
from ..server.server import Server


class TaskrouterV1TaskChannel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaskrouterV1TaskChannelWithRawResponse(client, server, auth)

    def create_task_channel(
        self,
        workspace_sid: str,
        friendly_name: str,
        unique_name: str,
        *,
        channel_optimized_routing: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskChannel:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace that the new Task Channel belongs to.
            friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64
                characters long.
            unique_name: An application-defined string that uniquely identifies the Task Channel, such as ``voice`` or
                ``sms``.
            channel_optimized_routing: Whether the Task Channel should prioritize Workers that have been idle. If
                ``true``, Workers that have been idle the longest are prioritized.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_task_channel(
            workspace_sid,
            friendly_name,
            unique_name,
            channel_optimized_routing=channel_optimized_routing,
            request_options=request_options,
        ).unwrap()

    def delete_task_channel(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to delete.
            sid: The SID of the Task Channel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_task_channel(workspace_sid, sid, request_options=request_options).unwrap()

    def fetch_task_channel(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTaskChannel:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to fetch.
            sid: The SID of the Task Channel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_task_channel(workspace_sid, sid, request_options=request_options).unwrap()

    def list_task_channel(
        self,
        workspace_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskChannelResponse:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_task_channel(
            workspace_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_task_channel(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        channel_optimized_routing: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskChannel:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to update.
            sid: The SID of the Task Channel resource to update.
            friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64
                characters long.
            channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If
                ``true``, Workers that have been idle the longest are prioritized.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_task_channel(
            workspace_sid,
            sid,
            friendly_name=friendly_name,
            channel_optimized_routing=channel_optimized_routing,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TaskrouterV1TaskChannelWithRawResponse:
        return self._with_raw_response


class AsyncTaskrouterV1TaskChannel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaskrouterV1TaskChannelWithRawResponse(client, server, auth)

    async def create_task_channel(
        self,
        workspace_sid: str,
        friendly_name: str,
        unique_name: str,
        *,
        channel_optimized_routing: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskChannel:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace that the new Task Channel belongs to.
            friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64
                characters long.
            unique_name: An application-defined string that uniquely identifies the Task Channel, such as ``voice`` or
                ``sms``.
            channel_optimized_routing: Whether the Task Channel should prioritize Workers that have been idle. If
                ``true``, Workers that have been idle the longest are prioritized.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_task_channel(
                workspace_sid,
                friendly_name,
                unique_name,
                channel_optimized_routing=channel_optimized_routing,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_task_channel(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to delete.
            sid: The SID of the Task Channel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_task_channel(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_task_channel(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TaskrouterV1WorkspaceTaskChannel:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to fetch.
            sid: The SID of the Task Channel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_task_channel(workspace_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_task_channel(
        self,
        workspace_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTaskChannelResponse:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_task_channel(
                workspace_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_task_channel(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        channel_optimized_routing: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TaskrouterV1WorkspaceTaskChannel:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to update.
            sid: The SID of the Task Channel resource to update.
            friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64
                characters long.
            channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If
                ``true``, Workers that have been idle the longest are prioritized.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_task_channel(
                workspace_sid,
                sid,
                friendly_name=friendly_name,
                channel_optimized_routing=channel_optimized_routing,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaskrouterV1TaskChannelWithRawResponse:
        return self._with_raw_response


class TaskrouterV1TaskChannelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_task_channel(
        self,
        workspace_sid: str,
        friendly_name: str,
        unique_name: str,
        *,
        channel_optimized_routing: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace that the new Task Channel belongs to.
            friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64
                characters long.
            unique_name: An application-defined string that uniquely identifies the Task Channel, such as ``voice`` or
                ``sms``.
            channel_optimized_routing: Whether the Task Channel should prioritize Workers that have been idle. If
                ``true``, Workers that have been idle the longest are prioritized.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("UniqueName", unique_name),
                    param[bool | None]("ChannelOptimizedRouting", channel_optimized_routing),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_task_channel(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to delete.
            sid: The SID of the Task Channel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_task_channel(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to fetch.
            sid: The SID of the Task Channel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_task_channel(
        self,
        workspace_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskChannelResponse, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_task_channel(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        channel_optimized_routing: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to update.
            sid: The SID of the Task Channel resource to update.
            friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64
                characters long.
            channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If
                ``true``, Workers that have been idle the longest are prioritized.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("ChannelOptimizedRouting", channel_optimized_routing),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTaskrouterV1TaskChannelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_task_channel(
        self,
        workspace_sid: str,
        friendly_name: str,
        unique_name: str,
        *,
        channel_optimized_routing: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace that the new Task Channel belongs to.
            friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64
                characters long.
            unique_name: An application-defined string that uniquely identifies the Task Channel, such as ``voice`` or
                ``sms``.
            channel_optimized_routing: Whether the Task Channel should prioritize Workers that have been idle. If
                ``true``, Workers that have been idle the longest are prioritized.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("FriendlyName", friendly_name),
                    param[str]("UniqueName", unique_name),
                    param[bool | None]("ChannelOptimizedRouting", channel_optimized_routing),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_task_channel(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to delete.
            sid: The SID of the Task Channel resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_task_channel(
        self, workspace_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to fetch.
            sid: The SID of the Task Channel resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_task_channel(
        self,
        workspace_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTaskChannelResponse, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels"),
            path_params=[param[str]("WorkspaceSid", workspace_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListTaskChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_task_channel(
        self,
        workspace_sid: str,
        sid: str,
        *,
        friendly_name: str | None = None,
        channel_optimized_routing: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TaskrouterV1WorkspaceTaskChannel, RawError]:
        """Types of tasks

        Args:
            workspace_sid: The SID of the Workspace with the Task Channel to update.
            sid: The SID of the Task Channel resource to update.
            friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64
                characters long.
            channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If
                ``true``, Workers that have been idle the longest are prioritized.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default8("/v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid}"),
            path_params=[param[str]("WorkspaceSid", workspace_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[bool | None]("ChannelOptimizedRouting", channel_optimized_routing),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[TaskrouterV1WorkspaceTaskChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
