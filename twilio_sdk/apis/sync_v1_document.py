from __future__ import annotations

from typing import Any
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
from ..models.list_document_response import ListDocumentResponse
from ..models.sync_v1_service_document import SyncV1ServiceDocument
from ..server.server import Server


class SyncV1Document:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1DocumentWithRawResponse(client, server, auth)

    def create_document(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceDocument:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Document resource in.
            unique_name: An application-defined string that uniquely identifies the Sync Document
            data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be
                up to 16 KiB in length.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the Sync
                Document expires and is deleted (the Sync Document's time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_document(
            service_sid, unique_name=unique_name, data=data, ttl=ttl, request_options=request_options
        ).unwrap()

    def delete_document(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to delete.
            sid: The SID of the Document resource to delete. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_document(service_sid, sid, request_options=request_options).unwrap()

    def fetch_document(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceDocument:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to fetch.
            sid: The SID of the Document resource to fetch. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_document(service_sid, sid, request_options=request_options).unwrap()

    def list_document(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDocumentResponse:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_document(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_document(
        self,
        service_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceDocument:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to update.
            sid: The SID of the Document resource to update. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            if_match: The If-Match HTTP request header
            data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be
                up to 16 KiB in length.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the Sync
                Document expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_document(
            service_sid, sid, if_match=if_match, data=data, ttl=ttl, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1DocumentWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1Document:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1DocumentWithRawResponse(client, server, auth)

    async def create_document(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceDocument:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Document resource in.
            unique_name: An application-defined string that uniquely identifies the Sync Document
            data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be
                up to 16 KiB in length.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the Sync
                Document expires and is deleted (the Sync Document's time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_document(
                service_sid, unique_name=unique_name, data=data, ttl=ttl, request_options=request_options
            )
        ).unwrap()

    async def delete_document(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to delete.
            sid: The SID of the Document resource to delete. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_document(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def fetch_document(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceDocument:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to fetch.
            sid: The SID of the Document resource to fetch. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_document(service_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_document(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDocumentResponse:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_document(
                service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_document(
        self,
        service_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SyncV1ServiceDocument:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to update.
            sid: The SID of the Document resource to update. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            if_match: The If-Match HTTP request header
            data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be
                up to 16 KiB in length.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the Sync
                Document expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_document(
                service_sid, sid, if_match=if_match, data=data, ttl=ttl, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1DocumentWithRawResponse:
        return self._with_raw_response


class SyncV1DocumentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_document(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceDocument, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Document resource in.
            unique_name: An application-defined string that uniquely identifies the Sync Document
            data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be
                up to 16 KiB in length.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the Sync
                Document expires and is deleted (the Sync Document's time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("UniqueName", unique_name),
                    param[Any | None]("Data", data),
                    param[int | None]("Ttl", ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_document(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to delete.
            sid: The SID of the Document resource to delete. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_document(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceDocument, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to fetch.
            sid: The SID of the Document resource to fetch. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_document(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDocumentResponse, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDocumentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_document(
        self,
        service_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceDocument, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to update.
            sid: The SID of the Document resource to update. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            if_match: The If-Match HTTP request header
            data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be
                up to 16 KiB in length.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the Sync
                Document expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[Any | None]("Data", data), param[int | None]("Ttl", ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1DocumentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_document(
        self,
        service_sid: str,
        *,
        unique_name: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceDocument, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Document resource in.
            unique_name: An application-defined string that uniquely identifies the Sync Document
            data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be
                up to 16 KiB in length.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the Sync
                Document expires and is deleted (the Sync Document's time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents"),
            path_params=[param[str]("ServiceSid", service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("UniqueName", unique_name),
                    param[Any | None]("Data", data),
                    param[int | None]("Ttl", ttl),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_document(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to delete.
            sid: The SID of the Document resource to delete. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_document(
        self, service_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceDocument, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to fetch.
            sid: The SID of the Document resource to fetch. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_document(
        self,
        service_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDocumentResponse, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resources to read.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents"),
            path_params=[param[str]("ServiceSid", service_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListDocumentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_document(
        self,
        service_sid: str,
        sid: str,
        *,
        if_match: str | None = None,
        data: Any | None = None,
        ttl: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SyncV1ServiceDocument, RawError]:
        """Sync Document objects

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ with the
                Document resource to update.
            sid: The SID of the Document resource to update. Can be the Document resource's ``sid`` or its
                ``unique_name``.
            if_match: The If-Match HTTP request header
            data: A JSON string that represents an arbitrary, schema-less object that the Sync Document stores. Can be
                up to 16 KiB in length.
            ttl: How long, `in seconds <https://www.twilio.com/docs/sync/limits#sync-payload-limits>`__, before the Sync
                Document expires and is deleted (time-to-live).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Documents/{Sid}"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("Sid", sid)],
            headers=[param[str | None]("If-Match", if_match), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[Any | None]("Data", data), param[int | None]("Ttl", ttl)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceDocument],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
