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
from ..errors.create_communication_in_conversation_error import (
    CreateCommunicationInConversationErrorBody,
    create_communication_in_conversation_error_mapper,
)
from ..errors.fetch_communication_error import FetchCommunicationErrorBody, fetch_communication_error_mapper
from ..errors.list_communication_by_conversation_error import (
    ListCommunicationByConversationErrorBody,
    list_communication_by_conversation_error_mapper,
)
from ..models.conversations_v2_communication import ConversationsV2Communication
from ..models.v2_conversations_communications_request import (
    V2ConversationsCommunicationsRequest,
    V2ConversationsCommunicationsRequestDict,
)
from ..models.v2_conversations_communications_response import V2ConversationsCommunicationsResponse
from ..server.server import Server


class ConversationsV2CommunicationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV2CommunicationApiWithRawResponse(client, server, auth)

    def create_communication_in_conversation(
        self,
        conversation_sid: str,
        *,
        body: V2ConversationsCommunicationsRequest | V2ConversationsCommunicationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Communication:
        """Create a Communication.

        Args:
            conversation_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.create_communication_in_conversation(
            conversation_sid, body=body, request_options=request_options
        ).unwrap()

    def fetch_communication(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Communication:
        """Retrieve a Communication.

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.fetch_communication(
            conversation_sid, sid, request_options=request_options
        ).unwrap()

    def list_communication_by_conversation(
        self,
        conversation_sid: str,
        *,
        channel_id: str | None = None,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ConversationsCommunicationsResponse:
        """Retrieve a list of Communications in a Conversation.

        Args:
            conversation_sid: Value sent with the request.
            channel_id: Resource identifier to filter communications
            page_size: Maximum number of items to return
            page_token: Page token for pagination
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.list_communication_by_conversation(
            conversation_sid,
            channel_id=channel_id,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV2CommunicationApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV2CommunicationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV2CommunicationApiWithRawResponse(client, server, auth)

    async def create_communication_in_conversation(
        self,
        conversation_sid: str,
        *,
        body: V2ConversationsCommunicationsRequest | V2ConversationsCommunicationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Communication:
        """Create a Communication.

        Args:
            conversation_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.create_communication_in_conversation(
                conversation_sid, body=body, request_options=request_options
            )
        ).unwrap()

    async def fetch_communication(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Communication:
        """Retrieve a Communication.

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.fetch_communication(conversation_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_communication_by_conversation(
        self,
        conversation_sid: str,
        *,
        channel_id: str | None = None,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ConversationsCommunicationsResponse:
        """Retrieve a list of Communications in a Conversation.

        Args:
            conversation_sid: Value sent with the request.
            channel_id: Resource identifier to filter communications
            page_size: Maximum number of items to return
            page_token: Page token for pagination
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.list_communication_by_conversation(
                conversation_sid,
                channel_id=channel_id,
                page_size=page_size,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV2CommunicationApiWithRawResponse:
        return self._with_raw_response


class ConversationsV2CommunicationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_communication_in_conversation(
        self,
        conversation_sid: str,
        *,
        body: V2ConversationsCommunicationsRequest | V2ConversationsCommunicationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Communication, CreateCommunicationInConversationErrorBody]:
        """Create a Communication.

        Args:
            conversation_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Communications"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsCommunicationsRequest | V2ConversationsCommunicationsRequestDict | None](
                body
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Communication],
            error_mapper=create_communication_in_conversation_error_mapper,
            request_options=request_options,
        )

    def fetch_communication(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Communication, FetchCommunicationErrorBody]:
        """Retrieve a Communication.

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Communications/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Communication],
            error_mapper=fetch_communication_error_mapper,
            request_options=request_options,
        )

    def list_communication_by_conversation(
        self,
        conversation_sid: str,
        *,
        channel_id: str | None = None,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ConversationsCommunicationsResponse, ListCommunicationByConversationErrorBody]:
        """Retrieve a list of Communications in a Conversation.

        Args:
            conversation_sid: Value sent with the request.
            channel_id: Resource identifier to filter communications
            page_size: Maximum number of items to return
            page_token: Page token for pagination
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Communications"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[
                param[str | None]("channelId", channel_id),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ConversationsCommunicationsResponse],
            error_mapper=list_communication_by_conversation_error_mapper,
            request_options=request_options,
        )


class AsyncConversationsV2CommunicationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_communication_in_conversation(
        self,
        conversation_sid: str,
        *,
        body: V2ConversationsCommunicationsRequest | V2ConversationsCommunicationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Communication, CreateCommunicationInConversationErrorBody]:
        """Create a Communication.

        Args:
            conversation_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Communications"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsCommunicationsRequest | V2ConversationsCommunicationsRequestDict | None](
                body
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Communication],
            error_mapper=create_communication_in_conversation_error_mapper,
            request_options=request_options,
        )

    async def fetch_communication(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Communication, FetchCommunicationErrorBody]:
        """Retrieve a Communication.

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Communications/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Communication],
            error_mapper=fetch_communication_error_mapper,
            request_options=request_options,
        )

    async def list_communication_by_conversation(
        self,
        conversation_sid: str,
        *,
        channel_id: str | None = None,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ConversationsCommunicationsResponse, ListCommunicationByConversationErrorBody]:
        """Retrieve a list of Communications in a Conversation.

        Args:
            conversation_sid: Value sent with the request.
            channel_id: Resource identifier to filter communications
            page_size: Maximum number of items to return
            page_token: Page token for pagination
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Communications"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[
                param[str | None]("channelId", channel_id),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ConversationsCommunicationsResponse],
            error_mapper=list_communication_by_conversation_error_mapper,
            request_options=request_options,
        )
