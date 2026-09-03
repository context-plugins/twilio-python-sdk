from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_conversation_with_config_error import (
    CreateConversationWithConfigErrorBody,
    create_conversation_with_config_error_mapper,
)
from ..errors.delete_conversation_async_error import (
    DeleteConversationAsyncErrorBody,
    delete_conversation_async_error_mapper,
)
from ..errors.fetch_conversation2_error import FetchConversation2ErrorBody, fetch_conversation2_error_mapper
from ..errors.list_conversation_by_account_error import (
    ListConversationByAccountErrorBody,
    list_conversation_by_account_error_mapper,
)
from ..errors.patch_conversation_by_id_error import (
    PatchConversationByIdErrorBody,
    patch_conversation_by_id_error_mapper,
)
from ..errors.update_conversation_by_id_error import (
    UpdateConversationByIdErrorBody,
    update_conversation_by_id_error_mapper,
)
from ..models.conversations_v2_conversation import ConversationsV2Conversation
from ..models.conversations_v2_operation_accepted import ConversationsV2OperationAccepted
from ..models.enums.status31 import Status31OrStr
from ..models.v2_conversations_request import V2ConversationsRequest, V2ConversationsRequestDict
from ..models.v2_conversations_request1 import V2ConversationsRequest1, V2ConversationsRequest1Dict
from ..models.v2_conversations_request2 import V2ConversationsRequest2, V2ConversationsRequest2Dict
from ..models.v2_conversations_response import V2ConversationsResponse
from ..server.server import Server


class ConversationsV2ConversationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV2ConversationApiWithRawResponse(client, server, auth)

    def create_conversation_with_config(
        self,
        *,
        body: V2ConversationsRequest | V2ConversationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Conversation:
        """Create a new conversation

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Conflict Too Many Requests Internal Server Error Service Unavailable
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.create_conversation_with_config(
            body=body, request_options=request_options
        ).unwrap()

    def delete_conversation_async(
        self, sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2OperationAccepted:
        """Asynchronously delete a conversation and all associated data. Returns 202 Accepted with an Operation-Id for
        status tracking via GET /v2/ControlPlane/Operations/{operationId}.

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Operation accepted for asynchronous processing

        Raises:
            ApiError: Bad Request Not Found Conflict Too Many Requests Internal Server Error Service Unavailable
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.delete_conversation_async(
            sid, idempotency_key=idempotency_key, request_options=request_options
        ).unwrap()

    def fetch_conversation2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Conversation:
        """Retrieve a Conversation.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.fetch_conversation2(sid, request_options=request_options).unwrap()

    def list_conversation_by_account(
        self,
        *,
        status: list[Status31OrStr] | None = None,
        channel_id: str | None = None,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ConversationsResponse:
        """Retrieve a list of Conversations.

        Args:
            status: Filters for specific statuses
            channel_id: The resource identifier (such as callSid or messageSid) to filter conversations.
            page_size: Maximum number of items to return in a single response
            page_token: A URL-safe, base64-encoded token representing the page of results to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.list_conversation_by_account(
            status=status,
            channel_id=channel_id,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def patch_conversation_by_id(
        self,
        sid: str,
        *,
        body: V2ConversationsRequest2 | V2ConversationsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Conversation:
        """Partially update the details of an existing Conversation.

        Args:
            sid: Value sent with the request.
            body: The conversation fields to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.patch_conversation_by_id(
            sid, body=body, request_options=request_options
        ).unwrap()

    def update_conversation_by_id(
        self,
        sid: str,
        *,
        body: V2ConversationsRequest1 | V2ConversationsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Conversation:
        """Update an existing conversation

        Args:
            sid: Value sent with the request.
            body: The conversation to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.update_conversation_by_id(
            sid, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV2ConversationApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV2ConversationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV2ConversationApiWithRawResponse(client, server, auth)

    async def create_conversation_with_config(
        self,
        *,
        body: V2ConversationsRequest | V2ConversationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Conversation:
        """Create a new conversation

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Conflict Too Many Requests Internal Server Error Service Unavailable
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.create_conversation_with_config(body=body, request_options=request_options)
        ).unwrap()

    async def delete_conversation_async(
        self, sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2OperationAccepted:
        """Asynchronously delete a conversation and all associated data. Returns 202 Accepted with an Operation-Id for
        status tracking via GET /v2/ControlPlane/Operations/{operationId}.

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Operation accepted for asynchronous processing

        Raises:
            ApiError: Bad Request Not Found Conflict Too Many Requests Internal Server Error Service Unavailable
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.delete_conversation_async(
                sid, idempotency_key=idempotency_key, request_options=request_options
            )
        ).unwrap()

    async def fetch_conversation2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Conversation:
        """Retrieve a Conversation.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (await self._with_raw_response.fetch_conversation2(sid, request_options=request_options)).unwrap()

    async def list_conversation_by_account(
        self,
        *,
        status: list[Status31OrStr] | None = None,
        channel_id: str | None = None,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ConversationsResponse:
        """Retrieve a list of Conversations.

        Args:
            status: Filters for specific statuses
            channel_id: The resource identifier (such as callSid or messageSid) to filter conversations.
            page_size: Maximum number of items to return in a single response
            page_token: A URL-safe, base64-encoded token representing the page of results to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.list_conversation_by_account(
                status=status,
                channel_id=channel_id,
                page_size=page_size,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def patch_conversation_by_id(
        self,
        sid: str,
        *,
        body: V2ConversationsRequest2 | V2ConversationsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Conversation:
        """Partially update the details of an existing Conversation.

        Args:
            sid: Value sent with the request.
            body: The conversation fields to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.patch_conversation_by_id(sid, body=body, request_options=request_options)
        ).unwrap()

    async def update_conversation_by_id(
        self,
        sid: str,
        *,
        body: V2ConversationsRequest1 | V2ConversationsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Conversation:
        """Update an existing conversation

        Args:
            sid: Value sent with the request.
            body: The conversation to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.update_conversation_by_id(sid, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV2ConversationApiWithRawResponse:
        return self._with_raw_response


class ConversationsV2ConversationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_conversation_with_config(
        self,
        *,
        body: V2ConversationsRequest | V2ConversationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Conversation, CreateConversationWithConfigErrorBody]:
        """Create a new conversation

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/Conversations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsRequest | V2ConversationsRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Conversation],
            error_mapper=create_conversation_with_config_error_mapper,
            request_options=request_options,
        )

    def delete_conversation_async(
        self, sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2OperationAccepted, DeleteConversationAsyncErrorBody]:
        """Asynchronously delete a conversation and all associated data. Returns 202 Accepted with an Operation-Id for
        status tracking via GET /v2/ControlPlane/Operations/{operationId}.

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v2/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationAccepted],
            error_mapper=delete_conversation_async_error_mapper,
            request_options=request_options,
        )

    def fetch_conversation2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Conversation, FetchConversation2ErrorBody]:
        """Retrieve a Conversation.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Conversation],
            error_mapper=fetch_conversation2_error_mapper,
            request_options=request_options,
        )

    def list_conversation_by_account(
        self,
        *,
        status: list[Status31OrStr] | None = None,
        channel_id: str | None = None,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ConversationsResponse, ListConversationByAccountErrorBody]:
        """Retrieve a list of Conversations.

        Args:
            status: Filters for specific statuses
            channel_id: The resource identifier (such as callSid or messageSid) to filter conversations.
            page_size: Maximum number of items to return in a single response
            page_token: A URL-safe, base64-encoded token representing the page of results to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations"),
            query_params=[
                param[list[Status31OrStr] | None]("status", status),
                param[str | None]("channelId", channel_id),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ConversationsResponse],
            error_mapper=list_conversation_by_account_error_mapper,
            request_options=request_options,
        )

    def patch_conversation_by_id(
        self,
        sid: str,
        *,
        body: V2ConversationsRequest2 | V2ConversationsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Conversation, PatchConversationByIdErrorBody]:
        """Partially update the details of an existing Conversation.

        Args:
            sid: Value sent with the request.
            body: The conversation fields to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default7("/v2/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsRequest2 | V2ConversationsRequest2Dict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Conversation],
            error_mapper=patch_conversation_by_id_error_mapper,
            request_options=request_options,
        )

    def update_conversation_by_id(
        self,
        sid: str,
        *,
        body: V2ConversationsRequest1 | V2ConversationsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Conversation, UpdateConversationByIdErrorBody]:
        """Update an existing conversation

        Args:
            sid: Value sent with the request.
            body: The conversation to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default7("/v2/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsRequest1 | V2ConversationsRequest1Dict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Conversation],
            error_mapper=update_conversation_by_id_error_mapper,
            request_options=request_options,
        )


class AsyncConversationsV2ConversationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_conversation_with_config(
        self,
        *,
        body: V2ConversationsRequest | V2ConversationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Conversation, CreateConversationWithConfigErrorBody]:
        """Create a new conversation

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/Conversations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsRequest | V2ConversationsRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Conversation],
            error_mapper=create_conversation_with_config_error_mapper,
            request_options=request_options,
        )

    async def delete_conversation_async(
        self, sid: str, *, idempotency_key: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2OperationAccepted, DeleteConversationAsyncErrorBody]:
        """Asynchronously delete a conversation and all associated data. Returns 202 Accepted with an Operation-Id for
        status tracking via GET /v2/ControlPlane/Operations/{operationId}.

        Args:
            sid: Value sent with the request.
            idempotency_key: Client-generated UUID key to ensure idempotent behavior. Submitting the same key returns
                the original response without creating a duplicate operation. Keys are scoped to account + region with a
                24-hour TTL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v2/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2OperationAccepted],
            error_mapper=delete_conversation_async_error_mapper,
            request_options=request_options,
        )

    async def fetch_conversation2(
        self, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Conversation, FetchConversation2ErrorBody]:
        """Retrieve a Conversation.

        Args:
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Conversation],
            error_mapper=fetch_conversation2_error_mapper,
            request_options=request_options,
        )

    async def list_conversation_by_account(
        self,
        *,
        status: list[Status31OrStr] | None = None,
        channel_id: str | None = None,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ConversationsResponse, ListConversationByAccountErrorBody]:
        """Retrieve a list of Conversations.

        Args:
            status: Filters for specific statuses
            channel_id: The resource identifier (such as callSid or messageSid) to filter conversations.
            page_size: Maximum number of items to return in a single response
            page_token: A URL-safe, base64-encoded token representing the page of results to return
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations"),
            query_params=[
                param[list[Status31OrStr] | None]("status", status),
                param[str | None]("channelId", channel_id),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ConversationsResponse],
            error_mapper=list_conversation_by_account_error_mapper,
            request_options=request_options,
        )

    async def patch_conversation_by_id(
        self,
        sid: str,
        *,
        body: V2ConversationsRequest2 | V2ConversationsRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Conversation, PatchConversationByIdErrorBody]:
        """Partially update the details of an existing Conversation.

        Args:
            sid: Value sent with the request.
            body: The conversation fields to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default7("/v2/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsRequest2 | V2ConversationsRequest2Dict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Conversation],
            error_mapper=patch_conversation_by_id_error_mapper,
            request_options=request_options,
        )

    async def update_conversation_by_id(
        self,
        sid: str,
        *,
        body: V2ConversationsRequest1 | V2ConversationsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Conversation, UpdateConversationByIdErrorBody]:
        """Update an existing conversation

        Args:
            sid: Value sent with the request.
            body: The conversation to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default7("/v2/Conversations/{Sid}"),
            path_params=[param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsRequest1 | V2ConversationsRequest1Dict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Conversation],
            error_mapper=update_conversation_by_id_error_mapper,
            request_options=request_options,
        )
