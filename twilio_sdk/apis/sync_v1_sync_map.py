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
from ..models.list_sync_map_response import ListSyncMapResponse
from ..models.sync_v1_service_sync_map import SyncV1ServiceSyncMap
from ..server.server import Server


class SyncV1SyncMap:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1SyncMapWithRawResponse(client, server, auth)

    def create_sync_map(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMap:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                Sync Map in.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used as an
                alternative to the ``sid`` in the URL path to address the resource.
            ttl: An alias for ``collection_ttl``. If both parameters are provided, this value is ignored.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sync_map(
            service_sid,
            unique_name=unique_name,
            ttl=ttl,
            collection_ttl=collection_ttl,
            request_options=request_options,
        ).unwrap()

    def delete_sync_map(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to delete.
            sid: The SID of the Sync Map resource to delete. Can be the Sync Map's ``sid`` or its ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sync_map(service_sid, sid, request_options=request_options).unwrap()

    def fetch_sync_map(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncMap:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to fetch.
            sid: The SID of the Sync Map resource to fetch. Can be the Sync Map's ``sid`` or its ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sync_map(service_sid, sid, request_options=request_options).unwrap()

    def list_sync_map(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncMapResponse:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sync_map(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_sync_map(
        self,
        service_sid: str,
        sid: str,
        *,
        ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMap:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to update.
            sid: The SID of the Sync Map resource to update. Can be the Sync Map's ``sid`` or its ``unique_name``.
            ttl: An alias for ``collection_ttl``. If both parameters are provided, this value is ignored.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sync_map(
            service_sid, sid, ttl=ttl, collection_ttl=collection_ttl, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1SyncMapWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1SyncMap:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1SyncMapWithRawResponse(client, server, auth)

    async def create_sync_map(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMap:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                Sync Map in.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used as an
                alternative to the ``sid`` in the URL path to address the resource.
            ttl: An alias for ``collection_ttl``. If both parameters are provided, this value is ignored.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sync_map(
                service_sid,
                unique_name=unique_name,
                ttl=ttl,
                collection_ttl=collection_ttl,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_sync_map(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to delete.
            sid: The SID of the Sync Map resource to delete. Can be the Sync Map's ``sid`` or its ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sync_map(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_sync_map(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncMap:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to fetch.
            sid: The SID of the Sync Map resource to fetch. Can be the Sync Map's ``sid`` or its ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sync_map(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_sync_map(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncMapResponse:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sync_map(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_sync_map(
        self,
        service_sid: str,
        sid: str,
        *,
        ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncMap:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to update.
            sid: The SID of the Sync Map resource to update. Can be the Sync Map's ``sid`` or its ``unique_name``.
            ttl: An alias for ``collection_ttl``. If both parameters are provided, this value is ignored.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sync_map(
                service_sid, sid, ttl=ttl, collection_ttl=collection_ttl, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1SyncMapWithRawResponse:
        return self._with_raw_response


class SyncV1SyncMapWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sync_map(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMap, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                Sync Map in.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used as an
                alternative to the ``sid`` in the URL path to address the resource.
            ttl: An alias for ``collection_ttl``. If both parameters are provided, this value is ignored.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body(
                [
                    param[str | None]("UniqueName", unique_name),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMap],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sync_map(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to delete.
            sid: The SID of the Sync Map resource to delete. Can be the Sync Map's ``sid`` or its ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sync_map(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncMap, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to fetch.
            sid: The SID of the Sync Map resource to fetch. Can be the Sync Map's ``sid`` or its ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMap],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sync_map(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncMapResponse, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncMapResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sync_map(
        self,
        service_sid: str,
        sid: str,
        *,
        ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMap, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to update.
            sid: The SID of the Sync Map resource to update. Can be the Sync Map's ``sid`` or its ``unique_name``.
            ttl: An alias for ``collection_ttl``. If both parameters are provided, this value is ignored.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            body=form_body([param[int | None]("Ttl", ttl), param[int | None]("CollectionTtl", collection_ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMap],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1SyncMapWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_sync_map(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMap, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                Sync Map in.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used as an
                alternative to the ``sid`` in the URL path to address the resource.
            ttl: An alias for ``collection_ttl``. If both parameters are provided, this value is ignored.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body(
                [
                    param[str | None]("UniqueName", unique_name),
                    param[int | None]("Ttl", ttl),
                    param[int | None]("CollectionTtl", collection_ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMap],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sync_map(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to delete.
            sid: The SID of the Sync Map resource to delete. Can be the Sync Map's ``sid`` or its ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sync_map(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncMap, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to fetch.
            sid: The SID of the Sync Map resource to fetch. Can be the Sync Map's ``sid`` or its ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMap],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sync_map(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncMapResponse, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncMapResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sync_map(
        self,
        service_sid: str,
        sid: str,
        *,
        ttl: int | None = None,
        collection_ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncMap, RawError]:
        """Sync map objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Map resource to update.
            sid: The SID of the Sync Map resource to update. Can be the Sync Map's ``sid`` or its ``unique_name``.
            ttl: An alias for ``collection_ttl``. If both parameters are provided, this value is ignored.
            collection_ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__,
                before the Sync Map expires (time-to-live) and is deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Maps/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            body=form_body([param[int | None]("Ttl", ttl), param[int | None]("CollectionTtl", collection_ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncMap],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
