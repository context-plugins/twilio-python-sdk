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
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.sync_v1_service_sync_stream_stream_message import SyncV1ServiceSyncStreamStreamMessage
from ..server.server import Server


class SyncV1StreamMessage:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SyncV1StreamMessageWithRawResponse(client, server, auth)

    def create_stream_message(
        self, service_sid: str, stream_sid: str, data: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncStreamStreamMessage:
        """Create a new Stream Message.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Stream Message in.
            stream_sid: The SID of the Sync Stream to create the new Stream Message resource for.
            data: A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body.
                Can be up to 4 KiB in length.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_stream_message(
            service_sid, stream_sid, data, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SyncV1StreamMessageWithRawResponse:
        return self._with_raw_response


class AsyncSyncV1StreamMessage:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSyncV1StreamMessageWithRawResponse(client, server, auth)

    async def create_stream_message(
        self, service_sid: str, stream_sid: str, data: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> SyncV1ServiceSyncStreamStreamMessage:
        """Create a new Stream Message.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Stream Message in.
            stream_sid: The SID of the Sync Stream to create the new Stream Message resource for.
            data: A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body.
                Can be up to 4 KiB in length.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_stream_message(
                service_sid, stream_sid, data, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSyncV1StreamMessageWithRawResponse:
        return self._with_raw_response


class SyncV1StreamMessageWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_stream_message(
        self, service_sid: str, stream_sid: str, data: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncStreamStreamMessage, RawError]:
        """Create a new Stream Message.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Stream Message in.
            stream_sid: The SID of the Sync Stream to create the new Stream Message resource for.
            data: A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body.
                Can be up to 4 KiB in length.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams/{StreamSid}/Messages"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("StreamSid", stream_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[Any]("Data", data)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncStreamStreamMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSyncV1StreamMessageWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_stream_message(
        self, service_sid: str, stream_sid: str, data: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SyncV1ServiceSyncStreamStreamMessage, RawError]:
        """Create a new Stream Message.

        Args:
            service_sid: The SID of the `Sync Service <https://www.twilio.com/docs/sync/api/service>`__ to create the
                new Stream Message in.
            stream_sid: The SID of the Sync Stream to create the new Stream Message resource for.
            data: A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body.
                Can be up to 4 KiB in length.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default12("/v1/Services/{ServiceSid}/Streams/{StreamSid}/Messages"),
            path_params=[param[str]("ServiceSid", service_sid), param[str]("StreamSid", stream_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[Any]("Data", data)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[SyncV1ServiceSyncStreamStreamMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
