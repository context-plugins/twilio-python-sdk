from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.list_participant_conversation_response import ListParticipantConversationResponse
from ..models.list_service_participant_conversation_response import ListServiceParticipantConversationResponse
from ..server.server import Server


class ConversationsV1ParticipantConversationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1ParticipantConversationApiWithRawResponse(client, server, auth)

    def list_participant_conversation(
        self,
        *,
        identity: str | None = None,
        address: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListParticipantConversationResponse:
        """Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one
        parameter should be specified.

        Args:
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            address: A unique string identifier for the conversation participant who's not a Conversation User. This
                parameter could be found in messaging_binding.address field of Participant resource. It should be
                url-encoded.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_participant_conversation(
            identity=identity,
            address=address,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def list_service_participant_conversation(
        self,
        chat_service_sid: str,
        *,
        identity: str | None = None,
        address: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceParticipantConversationResponse:
        """Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one
        parameter should be specified.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant Conversations
                resource is associated with.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            address: A unique string identifier for the conversation participant who's not a Conversation User. This
                parameter could be found in messaging_binding.address field of Participant resource. It should be
                url-encoded.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_participant_conversation(
            chat_service_sid,
            identity=identity,
            address=address,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1ParticipantConversationApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1ParticipantConversationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1ParticipantConversationApiWithRawResponse(client, server, auth)

    async def list_participant_conversation(
        self,
        *,
        identity: str | None = None,
        address: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListParticipantConversationResponse:
        """Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one
        parameter should be specified.

        Args:
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            address: A unique string identifier for the conversation participant who's not a Conversation User. This
                parameter could be found in messaging_binding.address field of Participant resource. It should be
                url-encoded.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_participant_conversation(
                identity=identity,
                address=address,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def list_service_participant_conversation(
        self,
        chat_service_sid: str,
        *,
        identity: str | None = None,
        address: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceParticipantConversationResponse:
        """Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one
        parameter should be specified.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant Conversations
                resource is associated with.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            address: A unique string identifier for the conversation participant who's not a Conversation User. This
                parameter could be found in messaging_binding.address field of Participant resource. It should be
                url-encoded.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_participant_conversation(
                chat_service_sid,
                identity=identity,
                address=address,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1ParticipantConversationApiWithRawResponse:
        return self._with_raw_response


class ConversationsV1ParticipantConversationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_participant_conversation(
        self,
        *,
        identity: str | None = None,
        address: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListParticipantConversationResponse, RawError]:
        """Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one
        parameter should be specified.

        Args:
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            address: A unique string identifier for the conversation participant who's not a Conversation User. This
                parameter could be found in messaging_binding.address field of Participant resource. It should be
                url-encoded.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/ParticipantConversations"),
            query_params=[
                param[str | None]("Identity", identity),
                param[str | None]("Address", address),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListParticipantConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_participant_conversation(
        self,
        chat_service_sid: str,
        *,
        identity: str | None = None,
        address: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceParticipantConversationResponse, RawError]:
        """Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one
        parameter should be specified.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant Conversations
                resource is associated with.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            address: A unique string identifier for the conversation participant who's not a Conversation User. This
                parameter could be found in messaging_binding.address field of Participant resource. It should be
                url-encoded.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/ParticipantConversations"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[str | None]("Identity", identity),
                param[str | None]("Address", address),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceParticipantConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1ParticipantConversationApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def list_participant_conversation(
        self,
        *,
        identity: str | None = None,
        address: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListParticipantConversationResponse, RawError]:
        """Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one
        parameter should be specified.

        Args:
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            address: A unique string identifier for the conversation participant who's not a Conversation User. This
                parameter could be found in messaging_binding.address field of Participant resource. It should be
                url-encoded.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/ParticipantConversations"),
            query_params=[
                param[str | None]("Identity", identity),
                param[str | None]("Address", address),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListParticipantConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_participant_conversation(
        self,
        chat_service_sid: str,
        *,
        identity: str | None = None,
        address: str | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceParticipantConversationResponse, RawError]:
        """Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one
        parameter should be specified.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant Conversations
                resource is associated with.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            address: A unique string identifier for the conversation participant who's not a Conversation User. This
                parameter could be found in messaging_binding.address field of Participant resource. It should be
                url-encoded.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/ParticipantConversations"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            query_params=[
                param[str | None]("Identity", identity),
                param[str | None]("Address", address),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceParticipantConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
