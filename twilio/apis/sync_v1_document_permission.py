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
from ..models.list_document_permission_response import ListDocumentPermissionResponse
from ..models.sync_v1_service_document_document_permission import SyncV1ServiceDocumentDocumentPermission
from ..server.server import Server


class SyncV1DocumentPermission:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1DocumentPermissionWithRawResponse(client, server, auth)

    def delete_document_permission(
        self, service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Sync Document Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to delete.
            document_sid: The SID of the Sync Document with the Document Permission resource to delete. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_document_permission(
            service_sid, document_sid, identity, request_options=request_options
        ).unwrap()

    def fetch_document_permission(
        self, service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceDocumentDocumentPermission:
        """Fetch a specific Sync Document Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to fetch.
            document_sid: The SID of the Sync Document with the Document Permission resource to fetch. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_document_permission(
            service_sid, document_sid, identity, request_options=request_options
        ).unwrap()

    def list_document_permission(
        self,
        service_sid: str,
        document_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDocumentPermissionResponse:
        """Retrieve a list of all Permissions applying to a Sync Document.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resources to read.
            document_sid: The SID of the Sync Document with the Document Permission resources to read. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_document_permission(
            service_sid,
            document_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_document_permission(
        self,
        service_sid: str,
        document_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceDocumentDocumentPermission:
        """Update an identity's access to a specific Sync Document.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to update.
            document_sid: The SID of the Sync Document with the Document Permission resource to update. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                update.
            read: Whether the identity can read the Sync Document. Default value is ``false``.
            write: Whether the identity can update the Sync Document. Default value is ``false``.
            manage: Whether the identity can delete the Sync Document. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_document_permission(
            service_sid, document_sid, identity, read, write, manage, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1DocumentPermissionWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1DocumentPermission:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1DocumentPermissionWithRawResponse(client, server, auth)

    async def delete_document_permission(
        self, service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Sync Document Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to delete.
            document_sid: The SID of the Sync Document with the Document Permission resource to delete. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_document_permission(
                service_sid, document_sid, identity, request_options=request_options
            )
        ).unwrap()

    async def fetch_document_permission(
        self, service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceDocumentDocumentPermission:
        """Fetch a specific Sync Document Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to fetch.
            document_sid: The SID of the Sync Document with the Document Permission resource to fetch. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_document_permission(
                service_sid, document_sid, identity, request_options=request_options
            )
        ).unwrap()

    async def list_document_permission(
        self,
        service_sid: str,
        document_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDocumentPermissionResponse:
        """Retrieve a list of all Permissions applying to a Sync Document.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resources to read.
            document_sid: The SID of the Sync Document with the Document Permission resources to read. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_document_permission(
                service_sid,
                document_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_document_permission(
        self,
        service_sid: str,
        document_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceDocumentDocumentPermission:
        """Update an identity's access to a specific Sync Document.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to update.
            document_sid: The SID of the Sync Document with the Document Permission resource to update. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                update.
            read: Whether the identity can read the Sync Document. Default value is ``false``.
            write: Whether the identity can update the Sync Document. Default value is ``false``.
            manage: Whether the identity can delete the Sync Document. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_document_permission(
                service_sid, document_sid, identity, read, write, manage, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1DocumentPermissionWithRawResponse:
        return self._with_raw_response


class SyncV1DocumentPermissionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_document_permission(
        self, service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Sync Document Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to delete.
            document_sid: The SID of the Sync Document with the Document Permission resource to delete. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12(
                "/v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("DocumentSid", document_sid),
                param[str]("Identity", identity),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_document_permission(
        self, service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceDocumentDocumentPermission, RawError]:
        """Fetch a specific Sync Document Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to fetch.
            document_sid: The SID of the Sync Document with the Document Permission resource to fetch. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12(
                "/v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("DocumentSid", document_sid),
                param[str]("Identity", identity),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocumentDocumentPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_document_permission(
        self,
        service_sid: str,
        document_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDocumentPermissionResponse, RawError]:
        """Retrieve a list of all Permissions applying to a Sync Document.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resources to read.
            document_sid: The SID of the Sync Document with the Document Permission resources to read. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("DocumentSid", document_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDocumentPermissionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_document_permission(
        self,
        service_sid: str,
        document_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceDocumentDocumentPermission, RawError]:
        """Update an identity's access to a specific Sync Document.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to update.
            document_sid: The SID of the Sync Document with the Document Permission resource to update. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                update.
            read: Whether the identity can read the Sync Document. Default value is ``false``.
            write: Whether the identity can update the Sync Document. Default value is ``false``.
            manage: Whether the identity can delete the Sync Document. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12(
                "/v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("DocumentSid", document_sid),
                param[str]("Identity", identity),
            ],
            body=form_body([param[bool]("Read", read), param[bool]("Write", write), param[bool]("Manage", manage)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocumentDocumentPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1DocumentPermissionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_document_permission(
        self, service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Sync Document Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to delete.
            document_sid: The SID of the Sync Document with the Document Permission resource to delete. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12(
                "/v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("DocumentSid", document_sid),
                param[str]("Identity", identity),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_document_permission(
        self, service_sid: str, document_sid: str, identity: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceDocumentDocumentPermission, RawError]:
        """Fetch a specific Sync Document Permission.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to fetch.
            document_sid: The SID of the Sync Document with the Document Permission resource to fetch. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12(
                "/v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("DocumentSid", document_sid),
                param[str]("Identity", identity),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocumentDocumentPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_document_permission(
        self,
        service_sid: str,
        document_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDocumentPermissionResponse, RawError]:
        """Retrieve a list of all Permissions applying to a Sync Document.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resources to read.
            document_sid: The SID of the Sync Document with the Document Permission resources to read. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("DocumentSid", document_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDocumentPermissionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_document_permission(
        self,
        service_sid: str,
        document_sid: str,
        identity: str,
        read: bool,
        write: bool,
        manage: bool,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceDocumentDocumentPermission, RawError]:
        """Update an identity's access to a specific Sync Document.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document Permission resource to update.
            document_sid: The SID of the Sync Document with the Document Permission resource to update. Can be the
                Document resource's ``sid`` or its ``unique_name``.
            identity: The application-defined string that uniquely identifies the User's Document Permission resource to
                update.
            read: Whether the identity can read the Sync Document. Default value is ``false``.
            write: Whether the identity can update the Sync Document. Default value is ``false``.
            manage: Whether the identity can delete the Sync Document. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12(
                "/v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity}"
            ),
            path_params=[
                param[str]("ServiceSid", service_sid),
                param[str]("DocumentSid", document_sid),
                param[str]("Identity", identity),
            ],
            body=form_body([param[bool]("Read", read), param[bool]("Write", write), param[bool]("Manage", manage)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocumentDocumentPermission],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
