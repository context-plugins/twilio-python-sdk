from __future__ import annotations

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
from ..errors.create_conversation_action_error import (
    CreateConversationActionErrorBody,
    create_conversation_action_error_mapper,
)
from ..errors.fetch_conversation_action_error import (
    FetchConversationActionErrorBody,
    fetch_conversation_action_error_mapper,
)
from ..models.conversations_v2_action import ConversationsV2Action
from ..models.conversations_v2_send_message_action_request import (
    ConversationsV2SendMessageActionRequest,
    ConversationsV2SendMessageActionRequestDict,
)
from ..server.server import Server


class ConversationsV2ActionApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV2ActionApiWithRawResponse(client, server, auth)

    def create_conversation_action(
        self,
        conversation_id: str,
        body: ConversationsV2SendMessageActionRequest | ConversationsV2SendMessageActionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Action:
        """Creates an Action within a Conversation. Currently supports SEND_MESSAGE, which sends a message to recipients
        via the configured channel.

        Returns 202 Accepted with the Action in PENDING status. Poll ``GET
        /v2/Conversations/{ConversationId}/Actions/{ActionId}`` to check completion.

        Args:
            conversation_id: Value sent with the request.
            body: The action to perform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Action accepted. Returns the Action in PENDING status.

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.create_conversation_action(
            conversation_id, body, request_options=request_options
        ).unwrap()

    def fetch_conversation_action(
        self, conversation_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Action:
        """Retrieve the current status of an Action.

        Args:
            conversation_id: Value sent with the request.
            action_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Action status.

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.fetch_conversation_action(
            conversation_id, action_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV2ActionApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV2ActionApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV2ActionApiWithRawResponse(client, server, auth)

    async def create_conversation_action(
        self,
        conversation_id: str,
        body: ConversationsV2SendMessageActionRequest | ConversationsV2SendMessageActionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Action:
        """Creates an Action within a Conversation. Currently supports SEND_MESSAGE, which sends a message to recipients
        via the configured channel.

        Returns 202 Accepted with the Action in PENDING status. Poll ``GET
        /v2/Conversations/{ConversationId}/Actions/{ActionId}`` to check completion.

        Args:
            conversation_id: Value sent with the request.
            body: The action to perform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Action accepted. Returns the Action in PENDING status.

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.create_conversation_action(
                conversation_id, body, request_options=request_options
            )
        ).unwrap()

    async def fetch_conversation_action(
        self, conversation_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Action:
        """Retrieve the current status of an Action.

        Args:
            conversation_id: Value sent with the request.
            action_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Action status.

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.fetch_conversation_action(
                conversation_id, action_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV2ActionApiWithRawResponse:
        return self._with_raw_response


class ConversationsV2ActionApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_conversation_action(
        self,
        conversation_id: str,
        body: ConversationsV2SendMessageActionRequest | ConversationsV2SendMessageActionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Action, CreateConversationActionErrorBody]:
        """Creates an Action within a Conversation. Currently supports SEND_MESSAGE, which sends a message to recipients
        via the configured channel.

        Returns 202 Accepted with the Action in PENDING status. Poll ``GET
        /v2/Conversations/{ConversationId}/Actions/{ActionId}`` to check completion.

        Args:
            conversation_id: Value sent with the request.
            body: The action to perform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/Conversations/{ConversationId}/Actions"),
            path_params=[param[str]("ConversationId", conversation_id)],
            body=json_body[ConversationsV2SendMessageActionRequest | ConversationsV2SendMessageActionRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Action],
            error_mapper=create_conversation_action_error_mapper,
            request_options=request_options,
        )

    def fetch_conversation_action(
        self, conversation_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Action, FetchConversationActionErrorBody]:
        """Retrieve the current status of an Action.

        Args:
            conversation_id: Value sent with the request.
            action_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationId}/Actions/{ActionId}"),
            path_params=[param[str]("ConversationId", conversation_id), param[str]("ActionId", action_id)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Action],
            error_mapper=fetch_conversation_action_error_mapper,
            request_options=request_options,
        )


class AsyncConversationsV2ActionApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_conversation_action(
        self,
        conversation_id: str,
        body: ConversationsV2SendMessageActionRequest | ConversationsV2SendMessageActionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Action, CreateConversationActionErrorBody]:
        """Creates an Action within a Conversation. Currently supports SEND_MESSAGE, which sends a message to recipients
        via the configured channel.

        Returns 202 Accepted with the Action in PENDING status. Poll ``GET
        /v2/Conversations/{ConversationId}/Actions/{ActionId}`` to check completion.

        Args:
            conversation_id: Value sent with the request.
            body: The action to perform.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/Conversations/{ConversationId}/Actions"),
            path_params=[param[str]("ConversationId", conversation_id)],
            body=json_body[ConversationsV2SendMessageActionRequest | ConversationsV2SendMessageActionRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Action],
            error_mapper=create_conversation_action_error_mapper,
            request_options=request_options,
        )

    async def fetch_conversation_action(
        self, conversation_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Action, FetchConversationActionErrorBody]:
        """Retrieve the current status of an Action.

        Args:
            conversation_id: Value sent with the request.
            action_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationId}/Actions/{ActionId}"),
            path_params=[param[str]("ConversationId", conversation_id), param[str]("ActionId", action_id)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Action],
            error_mapper=fetch_conversation_action_error_mapper,
            request_options=request_options,
        )
