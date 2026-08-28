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
from ..models.list_sync_stream_response import ListSyncStreamResponse
from ..models.sync_v1_service_sync_stream import SyncV1ServiceSyncStream
from ..server.server import Server


class SyncV1SyncStream:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1SyncStreamWithRawResponse(client, server, auth)

    def create_sync_stream(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncStream:
        """Create a new Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Stream in.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be unique
                within its Service and it can be up to 320 characters long. The ``unique_name`` value can be used as an
                alternative to the ``sid`` in the URL path to address the resource.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Stream expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_sync_stream(
            service_sid, unique_name=unique_name, ttl=ttl, request_options=request_options
        ).unwrap()

    def delete_sync_stream(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to delete.
            sid: The SID of the Stream resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_sync_stream(service_sid, sid, request_options=request_options).unwrap()

    def fetch_sync_stream(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncStream:
        """Fetch a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to fetch.
            sid: The SID of the Stream resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_sync_stream(service_sid, sid, request_options=request_options).unwrap()

    def list_sync_stream(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncStreamResponse:
        """Retrieve a list of all Streams in a Service Instance.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Stream
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sync_stream(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_sync_stream(
        self, service_sid: str, sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncStream:
        """Update a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to update.
            sid: The SID of the Stream resource to update.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Stream expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_sync_stream(
            service_sid, sid, ttl=ttl, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1SyncStreamWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1SyncStream:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1SyncStreamWithRawResponse(client, server, auth)

    async def create_sync_stream(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceSyncStream:
        """Create a new Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Stream in.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be unique
                within its Service and it can be up to 320 characters long. The ``unique_name`` value can be used as an
                alternative to the ``sid`` in the URL path to address the resource.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Stream expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_sync_stream(
                service_sid, unique_name=unique_name, ttl=ttl, request_options=request_options
            )
        ).unwrap()

    async def delete_sync_stream(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to delete.
            sid: The SID of the Stream resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_sync_stream(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_sync_stream(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncStream:
        """Fetch a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to fetch.
            sid: The SID of the Stream resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_sync_stream(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_sync_stream(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSyncStreamResponse:
        """Retrieve a list of all Streams in a Service Instance.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Stream
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_sync_stream(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_sync_stream(
        self, service_sid: str, sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncStream:
        """Update a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to update.
            sid: The SID of the Stream resource to update.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Stream expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_sync_stream(service_sid, sid, ttl=ttl, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1SyncStreamWithRawResponse:
        return self._with_raw_response


class SyncV1SyncStreamWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_sync_stream(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncStream, RawError]:
        """Create a new Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Stream in.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be unique
                within its Service and it can be up to 320 characters long. The ``unique_name`` value can be used as an
                alternative to the ``sid`` in the URL path to address the resource.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Stream expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body([param[str | None]("UniqueName", unique_name), param[int | None]("Ttl", ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncStream],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_sync_stream(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to delete.
            sid: The SID of the Stream resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_sync_stream(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncStream, RawError]:
        """Fetch a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to fetch.
            sid: The SID of the Stream resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncStream],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sync_stream(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncStreamResponse, RawError]:
        """Retrieve a list of all Streams in a Service Instance.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Stream
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncStreamResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_sync_stream(
        self, service_sid: str, sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncStream, RawError]:
        """Update a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to update.
            sid: The SID of the Stream resource to update.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Stream expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            body=form_body([param[int | None]("Ttl", ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncStream],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1SyncStreamWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_sync_stream(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceSyncStream, RawError]:
        """Create a new Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Stream in.
            unique_name: An application-defined string that uniquely identifies the resource. This value must be unique
                within its Service and it can be up to 320 characters long. The ``unique_name`` value can be used as an
                alternative to the ``sid`` in the URL path to address the resource.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Stream expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams"),
            path_params=[param[str]("ServiceSid", service_sid)],
            body=form_body([param[str | None]("UniqueName", unique_name), param[int | None]("Ttl", ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncStream],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_sync_stream(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to delete.
            sid: The SID of the Stream resource to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_sync_stream(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncStream, RawError]:
        """Fetch a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to fetch.
            sid: The SID of the Stream resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncStream],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sync_stream(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSyncStreamResponse, RawError]:
        """Retrieve a list of all Streams in a Service Instance.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Stream
                resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListSyncStreamResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_sync_stream(
        self, service_sid: str, sid: str, *, ttl: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncStream, RawError]:
        """Update a specific Stream.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the Sync
                Stream resource to update.
            sid: The SID of the Stream resource to update.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the
                Stream expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            body=form_body([param[int | None]("Ttl", ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncStream],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
