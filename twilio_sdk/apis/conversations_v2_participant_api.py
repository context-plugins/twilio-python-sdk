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
from ..errors.create_participant_in_conversation_error import (
    CreateParticipantInConversationErrorBody,
    create_participant_in_conversation_error_mapper,
)
from ..errors.fetch_participant2_error import FetchParticipant2ErrorBody, fetch_participant2_error_mapper
from ..errors.list_participant_by_conversation_error import (
    ListParticipantByConversationErrorBody,
    list_participant_by_conversation_error_mapper,
)
from ..errors.update_participant_in_conversation_error import (
    UpdateParticipantInConversationErrorBody,
    update_participant_in_conversation_error_mapper,
)
from ..models.conversations_v2_participant import ConversationsV2Participant
from ..models.v2_conversations_participants_request import (
    V2ConversationsParticipantsRequest,
    V2ConversationsParticipantsRequestDict,
)
from ..models.v2_conversations_participants_request1 import (
    V2ConversationsParticipantsRequest1,
    V2ConversationsParticipantsRequest1Dict,
)
from ..models.v2_conversations_participants_response import V2ConversationsParticipantsResponse
from ..server.server import Server


class ConversationsV2ParticipantApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV2ParticipantApiWithRawResponse(client, server, auth)

    def create_participant_in_conversation(
        self,
        conversation_sid: str,
        *,
        body: V2ConversationsParticipantsRequest | V2ConversationsParticipantsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Participant:
        """Create a Participant.

        Args:
            conversation_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Conflict Too Many Requests Internal Server Error Service Unavailable
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.create_participant_in_conversation(
            conversation_sid, body=body, request_options=request_options
        ).unwrap()

    def fetch_participant2(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Participant:
        """Retrieve a Participant.

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.fetch_participant2(
            conversation_sid, sid, request_options=request_options
        ).unwrap()

    def list_participant_by_conversation(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ConversationsParticipantsResponse:
        """Retrieve a list of Participants in a Conversation.

        Args:
            conversation_sid: Value sent with the request.
            page_size: Maximum number of items to return
            page_token: Page token for pagination
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.list_participant_by_conversation(
            conversation_sid, page_size=page_size, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_participant_in_conversation(
        self,
        conversation_sid: str,
        sid: str,
        *,
        body: V2ConversationsParticipantsRequest1 | V2ConversationsParticipantsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Participant:
        """Update an existing Participant

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return self._with_raw_response.update_participant_in_conversation(
            conversation_sid, sid, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV2ParticipantApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV2ParticipantApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV2ParticipantApiWithRawResponse(client, server, auth)

    async def create_participant_in_conversation(
        self,
        conversation_sid: str,
        *,
        body: V2ConversationsParticipantsRequest | V2ConversationsParticipantsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Participant:
        """Create a Participant.

        Args:
            conversation_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Conflict Too Many Requests Internal Server Error Service Unavailable
                ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.create_participant_in_conversation(
                conversation_sid, body=body, request_options=request_options
            )
        ).unwrap()

    async def fetch_participant2(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV2Participant:
        """Retrieve a Participant.

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
            await self._with_raw_response.fetch_participant2(conversation_sid, sid, request_options=request_options)
        ).unwrap()

    async def list_participant_by_conversation(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2ConversationsParticipantsResponse:
        """Retrieve a list of Participants in a Conversation.

        Args:
            conversation_sid: Value sent with the request.
            page_size: Maximum number of items to return
            page_token: Page token for pagination
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.list_participant_by_conversation(
                conversation_sid, page_size=page_size, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_participant_in_conversation(
        self,
        conversation_sid: str,
        sid: str,
        *,
        body: V2ConversationsParticipantsRequest1 | V2ConversationsParticipantsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV2Participant:
        """Update an existing Participant

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Not Found Too Many Requests Internal Server Error Service Unavailable ``error`` is
                ``AccountsCallsRecordingsSidJson201041408Error1 | RawError``."""
        return (
            await self._with_raw_response.update_participant_in_conversation(
                conversation_sid, sid, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV2ParticipantApiWithRawResponse:
        return self._with_raw_response


class ConversationsV2ParticipantApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_participant_in_conversation(
        self,
        conversation_sid: str,
        *,
        body: V2ConversationsParticipantsRequest | V2ConversationsParticipantsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Participant, CreateParticipantInConversationErrorBody]:
        """Create a Participant.

        Args:
            conversation_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Participants"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsParticipantsRequest | V2ConversationsParticipantsRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Participant],
            error_mapper=create_participant_in_conversation_error_mapper,
            request_options=request_options,
        )

    def fetch_participant2(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Participant, FetchParticipant2ErrorBody]:
        """Retrieve a Participant.

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Participant],
            error_mapper=fetch_participant2_error_mapper,
            request_options=request_options,
        )

    def list_participant_by_conversation(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ConversationsParticipantsResponse, ListParticipantByConversationErrorBody]:
        """Retrieve a list of Participants in a Conversation.

        Args:
            conversation_sid: Value sent with the request.
            page_size: Maximum number of items to return
            page_token: Page token for pagination
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Participants"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[param[int | None]("pageSize", page_size), param[str | None]("pageToken", page_token)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ConversationsParticipantsResponse],
            error_mapper=list_participant_by_conversation_error_mapper,
            request_options=request_options,
        )

    def update_participant_in_conversation(
        self,
        conversation_sid: str,
        sid: str,
        *,
        body: V2ConversationsParticipantsRequest1 | V2ConversationsParticipantsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Participant, UpdateParticipantInConversationErrorBody]:
        """Update an existing Participant

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsParticipantsRequest1 | V2ConversationsParticipantsRequest1Dict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Participant],
            error_mapper=update_participant_in_conversation_error_mapper,
            request_options=request_options,
        )


class AsyncConversationsV2ParticipantApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_participant_in_conversation(
        self,
        conversation_sid: str,
        *,
        body: V2ConversationsParticipantsRequest | V2ConversationsParticipantsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Participant, CreateParticipantInConversationErrorBody]:
        """Create a Participant.

        Args:
            conversation_sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Participants"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsParticipantsRequest | V2ConversationsParticipantsRequestDict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Participant],
            error_mapper=create_participant_in_conversation_error_mapper,
            request_options=request_options,
        )

    async def fetch_participant2(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV2Participant, FetchParticipant2ErrorBody]:
        """Retrieve a Participant.

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Participant],
            error_mapper=fetch_participant2_error_mapper,
            request_options=request_options,
        )

    async def list_participant_by_conversation(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = 50,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2ConversationsParticipantsResponse, ListParticipantByConversationErrorBody]:
        """Retrieve a list of Participants in a Conversation.

        Args:
            conversation_sid: Value sent with the request.
            page_size: Maximum number of items to return
            page_token: Page token for pagination
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Participants"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[param[int | None]("pageSize", page_size), param[str | None]("pageToken", page_token)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2ConversationsParticipantsResponse],
            error_mapper=list_participant_by_conversation_error_mapper,
            request_options=request_options,
        )

    async def update_participant_in_conversation(
        self,
        conversation_sid: str,
        sid: str,
        *,
        body: V2ConversationsParticipantsRequest1 | V2ConversationsParticipantsRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV2Participant, UpdateParticipantInConversationErrorBody]:
        """Update an existing Participant

        Args:
            conversation_sid: Value sent with the request.
            sid: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default7("/v2/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2ConversationsParticipantsRequest1 | V2ConversationsParticipantsRequest1Dict | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV2Participant],
            error_mapper=update_participant_in_conversation_error_mapper,
            request_options=request_options,
        )
