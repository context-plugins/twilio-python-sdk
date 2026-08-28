from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.fetch_operation_status_error import FetchOperationStatusErrorBody, fetch_operation_status_error_mapper
from ..models.conversations_v2_operation_status import ConversationsV2OperationStatus
from ..server.server import Server


class ConversationsV2Operation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV2OperationWithRawResponse(client, server, auth)

    def fetch_operation_status(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2OperationStatus:
        """Retrieve the current status of a long-running operation. Operations progress through: PENDING -> RUNNING ->
        COMPLETED or FAILED.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Operation status

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.fetch_operation_status(sid, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV2OperationWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV2Operation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV2OperationWithRawResponse(client, server, auth)

    async def fetch_operation_status(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2OperationStatus:
        """Retrieve the current status of a long-running operation. Operations progress through: PENDING -> RUNNING ->
        COMPLETED or FAILED.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Operation status

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (await self._with_raw_response.fetch_operation_status(sid, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV2OperationWithRawResponse:
        return self._with_raw_response


class ConversationsV2OperationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_operation_status(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2OperationStatus, FetchOperationStatusErrorBody]:
        """Retrieve the current status of a long-running operation. Operations progress through: PENDING -> RUNNING ->
        COMPLETED or FAILED.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/ControlPlane/Operations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationStatus],
            error_mapper=fetch_operation_status_error_mapper,
            request_options=request_options,
        )


class AsyncConversationsV2OperationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_operation_status(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2OperationStatus, FetchOperationStatusErrorBody]:
        """Retrieve the current status of a long-running operation. Operations progress through: PENDING -> RUNNING ->
        COMPLETED or FAILED.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/ControlPlane/Operations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationStatus],
            error_mapper=fetch_operation_status_error_mapper,
            request_options=request_options,
        )
