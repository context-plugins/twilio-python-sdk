from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.conversations_v1_service_service_user_service_user_conversation import (
    ConversationsV1ServiceServiceUserServiceUserConversation,
)
from ..models.conversations_v1_user_user_conversation import ConversationsV1UserUserConversation
from ..models.enums.service_user_conversation_enum_notification_level import (
    ServiceUserConversationEnumNotificationLevelOrStr,
)
from ..models.enums.user_conversation_enum_notification_level import UserConversationEnumNotificationLevelOrStr
from ..models.list_service_user_conversation_response import ListServiceUserConversationResponse
from ..models.list_user_conversation_response import ListUserConversationResponse
from ..server.server import Server


class ConversationsV1UserConversation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1UserConversationWithRawResponse(client, server, auth)

    def delete_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service_user_conversation(
            chat_service_sid, user_sid, conversation_sid, request_options=request_options
        ).unwrap()

    def delete_user_conversation(
        self, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_user_conversation(
            user_sid, conversation_sid, request_options=request_options
        ).unwrap()

    def fetch_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceUserServiceUserConversation:
        """Fetch a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_user_conversation(
            chat_service_sid, user_sid, conversation_sid, request_options=request_options
        ).unwrap()

    def fetch_user_conversation(
        self, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1UserUserConversation:
        """Fetch a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_user_conversation(
            user_sid, conversation_sid, request_options=request_options
        ).unwrap()

    def list_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceUserConversationResponse:
        """Retrieve a list of all User Conversations for the User.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_user_conversation(
            chat_service_sid,
            user_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def list_user_conversation(
        self,
        user_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUserConversationResponse:
        """Retrieve a list of all User Conversations for the User.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_user_conversation(
            user_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        notification_level: ServiceUserConversationEnumNotificationLevelOrStr | None = None,
        last_read_timestamp: RFC3339DateTime | None = None,
        last_read_message_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceUserServiceUserConversation:
        """Update a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            notification_level: The Notification Level of this User Conversation. One of ``default`` or ``muted``.
            last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601
                format.
            last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_user_conversation(
            chat_service_sid,
            user_sid,
            conversation_sid,
            notification_level=notification_level,
            last_read_timestamp=last_read_timestamp,
            last_read_message_index=last_read_message_index,
            request_options=request_options,
        ).unwrap()

    def update_user_conversation(
        self,
        user_sid: str,
        conversation_sid: str,
        *,
        notification_level: UserConversationEnumNotificationLevelOrStr | None = None,
        last_read_timestamp: RFC3339DateTime | None = None,
        last_read_message_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1UserUserConversation:
        """Update a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            notification_level: The Notification Level of this User Conversation. One of ``default`` or ``muted``.
            last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601
                format.
            last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_user_conversation(
            user_sid,
            conversation_sid,
            notification_level=notification_level,
            last_read_timestamp=last_read_timestamp,
            last_read_message_index=last_read_message_index,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1UserConversationWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1UserConversation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1UserConversationWithRawResponse(client, server, auth)

    async def delete_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Delete a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_service_user_conversation(
                chat_service_sid, user_sid, conversation_sid, request_options=request_options
            )
        ).unwrap()

    async def delete_user_conversation(
        self, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Delete a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_user_conversation(
                user_sid, conversation_sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceUserServiceUserConversation:
        """Fetch a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_user_conversation(
                chat_service_sid, user_sid, conversation_sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_user_conversation(
        self, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1UserUserConversation:
        """Fetch a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_user_conversation(
                user_sid, conversation_sid, request_options=request_options
            )
        ).unwrap()

    async def list_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceUserConversationResponse:
        """Retrieve a list of all User Conversations for the User.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_user_conversation(
                chat_service_sid,
                user_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def list_user_conversation(
        self,
        user_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListUserConversationResponse:
        """Retrieve a list of all User Conversations for the User.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_user_conversation(
                user_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        notification_level: ServiceUserConversationEnumNotificationLevelOrStr | None = None,
        last_read_timestamp: RFC3339DateTime | None = None,
        last_read_message_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceUserServiceUserConversation:
        """Update a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            notification_level: The Notification Level of this User Conversation. One of ``default`` or ``muted``.
            last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601
                format.
            last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_user_conversation(
                chat_service_sid,
                user_sid,
                conversation_sid,
                notification_level=notification_level,
                last_read_timestamp=last_read_timestamp,
                last_read_message_index=last_read_message_index,
                request_options=request_options,
            )
        ).unwrap()

    async def update_user_conversation(
        self,
        user_sid: str,
        conversation_sid: str,
        *,
        notification_level: UserConversationEnumNotificationLevelOrStr | None = None,
        last_read_timestamp: RFC3339DateTime | None = None,
        last_read_message_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1UserUserConversation:
        """Update a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            notification_level: The Notification Level of this User Conversation. One of ``default`` or ``muted``.
            last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601
                format.
            last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_user_conversation(
                user_sid,
                conversation_sid,
                notification_level=notification_level,
                last_read_timestamp=last_read_timestamp,
                last_read_message_index=last_read_message_index,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1UserConversationWithRawResponse:
        return self._with_raw_response


class ConversationsV1UserConversationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Delete a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("UserSid", user_sid),
                param[str]("ConversationSid", conversation_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_user_conversation(
        self, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Users/{UserSid}/Conversations/{ConversationSid}"),
            path_params=[param[str]("UserSid", user_sid), param[str]("ConversationSid", conversation_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceUserServiceUserConversation, RawError]:
        """Fetch a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("UserSid", user_sid),
                param[str]("ConversationSid", conversation_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUserServiceUserConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_user_conversation(
        self, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1UserUserConversation, RawError]:
        """Fetch a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Users/{UserSid}/Conversations/{ConversationSid}"),
            path_params=[param[str]("UserSid", user_sid), param[str]("ConversationSid", conversation_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1UserUserConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceUserConversationResponse, RawError]:
        """Retrieve a list of all User Conversations for the User.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("UserSid", user_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceUserConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_user_conversation(
        self,
        user_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUserConversationResponse, RawError]:
        """Retrieve a list of all User Conversations for the User.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Users/{UserSid}/Conversations"),
            path_params=[param[str]("UserSid", user_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUserConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        notification_level: ServiceUserConversationEnumNotificationLevelOrStr | None = None,
        last_read_timestamp: RFC3339DateTime | None = None,
        last_read_message_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceUserServiceUserConversation, RawError]:
        """Update a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            notification_level: The Notification Level of this User Conversation. One of ``default`` or ``muted``.
            last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601
                format.
            last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("UserSid", user_sid),
                param[str]("ConversationSid", conversation_sid),
            ],
            body=form_body(
                [
                    param[ServiceUserConversationEnumNotificationLevelOrStr | None](
                        "NotificationLevel", notification_level
                    ),
                    param[RFC3339DateTime | None]("LastReadTimestamp", last_read_timestamp),
                    param[int | None]("LastReadMessageIndex", last_read_message_index),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUserServiceUserConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_user_conversation(
        self,
        user_sid: str,
        conversation_sid: str,
        *,
        notification_level: UserConversationEnumNotificationLevelOrStr | None = None,
        last_read_timestamp: RFC3339DateTime | None = None,
        last_read_message_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1UserUserConversation, RawError]:
        """Update a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            notification_level: The Notification Level of this User Conversation. One of ``default`` or ``muted``.
            last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601
                format.
            last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Users/{UserSid}/Conversations/{ConversationSid}"),
            path_params=[param[str]("UserSid", user_sid), param[str]("ConversationSid", conversation_sid)],
            body=form_body(
                [
                    param[UserConversationEnumNotificationLevelOrStr | None]("NotificationLevel", notification_level),
                    param[RFC3339DateTime | None]("LastReadTimestamp", last_read_timestamp),
                    param[int | None]("LastReadMessageIndex", last_read_message_index),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1UserUserConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1UserConversationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Delete a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("UserSid", user_sid),
                param[str]("ConversationSid", conversation_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_user_conversation(
        self, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Delete a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Users/{UserSid}/Conversations/{ConversationSid}"),
            path_params=[param[str]("UserSid", user_sid), param[str]("ConversationSid", conversation_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceUserServiceUserConversation, RawError]:
        """Fetch a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("UserSid", user_sid),
                param[str]("ConversationSid", conversation_sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUserServiceUserConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_user_conversation(
        self, user_sid: str, conversation_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1UserUserConversation, RawError]:
        """Fetch a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Users/{UserSid}/Conversations/{ConversationSid}"),
            path_params=[param[str]("UserSid", user_sid), param[str]("ConversationSid", conversation_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1UserUserConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceUserConversationResponse, RawError]:
        """Retrieve a list of all User Conversations for the User.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid), param[str]("UserSid", user_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceUserConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_user_conversation(
        self,
        user_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListUserConversationResponse, RawError]:
        """Retrieve a list of all User Conversations for the User.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 50.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Users/{UserSid}/Conversations"),
            path_params=[param[str]("UserSid", user_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListUserConversationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_user_conversation(
        self,
        chat_service_sid: str,
        user_sid: str,
        conversation_sid: str,
        *,
        notification_level: ServiceUserConversationEnumNotificationLevelOrStr | None = None,
        last_read_timestamp: RFC3339DateTime | None = None,
        last_read_message_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceUserServiceUserConversation, RawError]:
        """Update a specific User Conversation.

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            notification_level: The Notification Level of this User Conversation. One of ``default`` or ``muted``.
            last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601
                format.
            last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("UserSid", user_sid),
                param[str]("ConversationSid", conversation_sid),
            ],
            body=form_body(
                [
                    param[ServiceUserConversationEnumNotificationLevelOrStr | None](
                        "NotificationLevel", notification_level
                    ),
                    param[RFC3339DateTime | None]("LastReadTimestamp", last_read_timestamp),
                    param[int | None]("LastReadMessageIndex", last_read_message_index),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceUserServiceUserConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_user_conversation(
        self,
        user_sid: str,
        conversation_sid: str,
        *,
        notification_level: UserConversationEnumNotificationLevelOrStr | None = None,
        last_read_timestamp: RFC3339DateTime | None = None,
        last_read_message_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1UserUserConversation, RawError]:
        """Update a specific User Conversation.

        Args:
            user_sid: The unique SID identifier of the `User resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This value can be either the ``sid``
                or the ``identity`` of the User resource.
            conversation_sid: The unique SID identifier of the Conversation. This value can be either the ``sid`` or the
                ``unique_name`` of the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__.
            notification_level: The Notification Level of this User Conversation. One of ``default`` or ``muted``.
            last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601
                format.
            last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Users/{UserSid}/Conversations/{ConversationSid}"),
            path_params=[param[str]("UserSid", user_sid), param[str]("ConversationSid", conversation_sid)],
            body=form_body(
                [
                    param[UserConversationEnumNotificationLevelOrStr | None]("NotificationLevel", notification_level),
                    param[RFC3339DateTime | None]("LastReadTimestamp", last_read_timestamp),
                    param[int | None]("LastReadMessageIndex", last_read_message_index),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1UserUserConversation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
