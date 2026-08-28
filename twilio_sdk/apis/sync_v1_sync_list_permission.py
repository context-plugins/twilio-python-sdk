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
from ..models.list_sync_list_permission_response import ListSyncListPermissionResponse
from ..models.sync_v1_service_sync_list_sync_list_permission import SyncV1ServiceSyncListSyncListPermission
from ..server.server import Server


class SyncV1SyncListPermission:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1SyncListPermissionWithRawResponse(client, server, auth)

    def delete_sync_list_permission(
        self, service_sid: str, list_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Sync List Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to delete.
            list_sid: The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sync_list_permission(
            service_sid, list_sid, identity, request_options=request_options
        ).unwrap()

    def fetch_sync_list_permission(
        self, service_sid: str, list_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncListSyncListPermission:
        """Fetch a specific Sync List Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to fetch.
            list_sid: The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sync_list_permission(
            service_sid, list_sid, identity, request_options=request_options
        ).unwrap()

    def list_sync_list_permission(
        self,
        service_sid: str,
        list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncListPermissionResponse:
        """Retrieve a list of all Permissions applying to a Sync List.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resources to read.
            list_sid: The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sync_list_permission(
            service_sid,
            list_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_sync_list_permission(
        self,
        service_sid: str,
        list_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncListSyncListPermission:
        """Update an identity's access to a specific Sync List.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to update.
            list_sid: The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to update.
            read: Whether the identity can read the Sync List and its Items. Default value is ``false``.
            write: Whether the identity can create, update, and delete Items in the Sync List. Default value is
                ``false``.
            manage: Whether the identity can delete the Sync List. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sync_list_permission(
            service_sid, list_sid, identity, read, write, manage, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1SyncListPermissionWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1SyncListPermission:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1SyncListPermissionWithRawResponse(client, server, auth)

    async def delete_sync_list_permission(
        self, service_sid: str, list_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Sync List Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to delete.
            list_sid: The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sync_list_permission(
                service_sid, list_sid, identity, request_options=request_options
            )
        ).unwrap()

    async def fetch_sync_list_permission(
        self, service_sid: str, list_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncListSyncListPermission:
        """Fetch a specific Sync List Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to fetch.
            list_sid: The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sync_list_permission(
                service_sid, list_sid, identity, request_options=request_options
            )
        ).unwrap()

    async def list_sync_list_permission(
        self,
        service_sid: str,
        list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncListPermissionResponse:
        """Retrieve a list of all Permissions applying to a Sync List.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resources to read.
            list_sid: The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sync_list_permission(
                service_sid,
                list_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_sync_list_permission(
        self,
        service_sid: str,
        list_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncListSyncListPermission:
        """Update an identity's access to a specific Sync List.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to update.
            list_sid: The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to update.
            read: Whether the identity can read the Sync List and its Items. Default value is ``false``.
            write: Whether the identity can create, update, and delete Items in the Sync List. Default value is
                ``false``.
            manage: Whether the identity can delete the Sync List. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sync_list_permission(
                service_sid, list_sid, identity, read, write, manage, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1SyncListPermissionWithRawResponse:
        return self._with_raw_response


class SyncV1SyncListPermissionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_sync_list_permission(
        self, service_sid: str, list_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Sync List Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to delete.
            list_sid: The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[str]("Identity", identity)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sync_list_permission(
        self, service_sid: str, list_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncListSyncListPermission, RawError]:
        """Fetch a specific Sync List Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to fetch.
            list_sid: The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[str]("Identity", identity)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sync_list_permission(
        self,
        service_sid: str,
        list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncListPermissionResponse, RawError]:
        """Retrieve a list of all Permissions applying to a Sync List.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resources to read.
            list_sid: The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncListPermissionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sync_list_permission(
        self,
        service_sid: str,
        list_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncListSyncListPermission, RawError]:
        """Update an identity's access to a specific Sync List.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to update.
            list_sid: The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to update.
            read: Whether the identity can read the Sync List and its Items. Default value is ``false``.
            write: Whether the identity can create, update, and delete Items in the Sync List. Default value is
                ``false``.
            manage: Whether the identity can delete the Sync List. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[str]("Identity", identity)
            ],
            body=form_body([param[bool]("Read", read), param[bool]("Write", write), param[bool]("Manage", manage)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1SyncListPermissionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_sync_list_permission(
        self, service_sid: str, list_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Sync List Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to delete.
            list_sid: The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[str]("Identity", identity)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sync_list_permission(
        self, service_sid: str, list_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncListSyncListPermission, RawError]:
        """Fetch a specific Sync List Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to fetch.
            list_sid: The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[str]("Identity", identity)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sync_list_permission(
        self,
        service_sid: str,
        list_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncListPermissionResponse, RawError]:
        """Retrieve a list of all Permissions applying to a Sync List.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resources to read.
            list_sid: The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncListPermissionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sync_list_permission(
        self,
        service_sid: str,
        list_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncListSyncListPermission, RawError]:
        """Update an identity's access to a specific Sync List.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                List Permission resource to update.
            list_sid: The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync List Permission resource
                to update.
            read: Whether the identity can read the Sync List and its Items. Default value is ``false``.
            write: Whether the identity can create, update, and delete Items in the Sync List. Default value is
                ``false``.
            manage: Whether the identity can delete the Sync List. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("ListSid", list_sid), param[str]("Identity", identity)
            ],
            body=form_body([param[bool]("Read", read), param[bool]("Write", write), param[bool]("Manage", manage)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncListSyncListPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
