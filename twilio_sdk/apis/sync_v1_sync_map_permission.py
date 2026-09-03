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
from ..models.list_sync_map_permission_response import ListSyncMapPermissionResponse
from ..models.sync_v1_service_sync_map_sync_map_permission import SyncV1ServiceSyncMapSyncMapPermission
from ..server.server import Server


class SyncV1SyncMapPermission:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1SyncMapPermissionWithRawResponse(client, server, auth)

    def delete_sync_map_permission(
        self, service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Sync Map Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to delete. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sync_map_permission(
            service_sid, map_sid, identity, request_options=request_options
        ).unwrap()

    def fetch_sync_map_permission(
        self, service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncMapSyncMapPermission:
        """Fetch a specific Sync Map Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to fetch. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sync_map_permission(
            service_sid, map_sid, identity, request_options=request_options
        ).unwrap()

    def list_sync_map_permission(
        self,
        service_sid: str,
        map_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncMapPermissionResponse:
        """Retrieve a list of all Permissions applying to a Sync Map.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resources to read. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sync_map_permission(
            service_sid, map_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_sync_map_permission(
        self,
        service_sid: str,
        map_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMapSyncMapPermission:
        """Update an identity's access to a specific Sync Map.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to update. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                update.
            read: Whether the identity can read the Sync Map and its Items. Default value is ``false``.
            write: Whether the identity can create, update, and delete Items in the Sync Map. Default value is
                ``false``.
            manage: Whether the identity can delete the Sync Map. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sync_map_permission(
            service_sid, map_sid, identity, read, write, manage, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1SyncMapPermissionWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1SyncMapPermission:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1SyncMapPermissionWithRawResponse(client, server, auth)

    async def delete_sync_map_permission(
        self, service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Sync Map Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to delete. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sync_map_permission(
                service_sid, map_sid, identity, request_options=request_options
            )
        ).unwrap()

    async def fetch_sync_map_permission(
        self, service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncMapSyncMapPermission:
        """Fetch a specific Sync Map Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to fetch. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sync_map_permission(
                service_sid, map_sid, identity, request_options=request_options
            )
        ).unwrap()

    async def list_sync_map_permission(
        self,
        service_sid: str,
        map_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncMapPermissionResponse:
        """Retrieve a list of all Permissions applying to a Sync Map.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resources to read. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sync_map_permission(
                service_sid,
                map_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_sync_map_permission(
        self,
        service_sid: str,
        map_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMapSyncMapPermission:
        """Update an identity's access to a specific Sync Map.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to update. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                update.
            read: Whether the identity can read the Sync Map and its Items. Default value is ``false``.
            write: Whether the identity can create, update, and delete Items in the Sync Map. Default value is
                ``false``.
            manage: Whether the identity can delete the Sync Map. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sync_map_permission(
                service_sid, map_sid, identity, read, write, manage, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1SyncMapPermissionWithRawResponse:
        return self._with_raw_response


class SyncV1SyncMapPermissionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_sync_map_permission(
        self, service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Sync Map Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to delete. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Identity", identity)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sync_map_permission(
        self, service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapPermission, RawError]:
        """Fetch a specific Sync Map Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to fetch. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Identity", identity)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sync_map_permission(
        self,
        service_sid: str,
        map_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncMapPermissionResponse, RawError]:
        """Retrieve a list of all Permissions applying to a Sync Map.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resources to read. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncMapPermissionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sync_map_permission(
        self,
        service_sid: str,
        map_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapPermission, RawError]:
        """Update an identity's access to a specific Sync Map.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to update. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                update.
            read: Whether the identity can read the Sync Map and its Items. Default value is ``false``.
            write: Whether the identity can create, update, and delete Items in the Sync Map. Default value is
                ``false``.
            manage: Whether the identity can delete the Sync Map. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Identity", identity)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[bool]("Read", read), param[bool]("Write", write), param[bool]("Manage", manage)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1SyncMapPermissionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_sync_map_permission(
        self, service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Sync Map Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to delete. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Identity", identity)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sync_map_permission(
        self, service_sid: str, map_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapPermission, RawError]:
        """Fetch a specific Sync Map Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to fetch. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Identity", identity)
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sync_map_permission(
        self,
        service_sid: str,
        map_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncMapPermissionResponse, RawError]:
        """Retrieve a list of all Permissions applying to a Sync Map.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resources to read. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource's
                ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncMapPermissionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sync_map_permission(
        self,
        service_sid: str,
        map_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMapSyncMapPermission, RawError]:
        """Update an identity's access to a specific Sync Map.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map Permission resource to update. Can be the Service's ``sid`` value or ``default``.
            map_sid: The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map
                resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to
                update.
            read: Whether the identity can read the Sync Map and its Items. Default value is ``false``.
            write: Whether the identity can create, update, and delete Items in the Sync Map. Default value is
                ``false``.
            manage: Whether the identity can delete the Sync Map. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity}"),
            path_params=[
                param[str]("ServiceSid", service_sid), param[str]("MapSid", map_sid), param[str]("Identity", identity)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[bool]("Read", read), param[bool]("Write", write), param[bool]("Manage", manage)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMapSyncMapPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
