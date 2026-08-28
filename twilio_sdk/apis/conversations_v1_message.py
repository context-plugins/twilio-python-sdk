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
from ..models.conversations_v1_conversation_conversation_message import ConversationsV1ConversationConversationMessage
from ..models.conversations_v1_service_service_conversation_service_conversation_message import (
    ConversationsV1ServiceServiceConversationServiceConversationMessage,
)
from ..models.enums.challenge_enum_list_orders import ChallengeEnumListOrdersOrStr
from ..models.enums.confirmation import ConfirmationOrStr
from ..models.list_conversation_message_response import ListConversationMessageResponse
from ..models.list_service_conversation_message_response import ListServiceConversationMessageResponse
from ..server.server import Server


class ConversationsV1Message:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1MessageWithRawResponse(client, server, auth)

    def create_conversation_message(
        self,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        media_sid: str | None = None,
        content_sid: str | None = None,
        content_variables: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationMessage:
        """Add a new message to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            media_sid: The Media SID to be attached to the new Message.
            content_sid: The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__
                template, required for template-generated messages. **Note** that if this field is set, ``Body`` and
                ``MediaSid`` parameters are ignored.
            content_variables: A structurally valid JSON string that contains values to resolve Rich Content template
                variables.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_conversation_message(
            conversation_sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            author=author,
            body=body,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            media_sid=media_sid,
            content_sid=content_sid,
            content_variables=content_variables,
            subject=subject,
            request_options=request_options,
        ).unwrap()

    def create_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        media_sid: str | None = None,
        content_sid: str | None = None,
        content_variables: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationMessage:
        """Add a new message to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            media_sid: The Media SID to be attached to the new Message.
            content_sid: The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__
                template, required for template-generated messages. **Note** that if this field is set, ``Body`` and
                ``MediaSid`` parameters are ignored.
            content_variables: A structurally valid JSON string that contains values to resolve Rich Content template
                variables.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service_conversation_message(
            chat_service_sid,
            conversation_sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            author=author,
            body=body,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            media_sid=media_sid,
            content_sid=content_sid,
            content_variables=content_variables,
            subject=subject,
            request_options=request_options,
        ).unwrap()

    def delete_conversation_message(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a message from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_conversation_message(
            conversation_sid, sid, x_twilio_webhook_enabled=x_twilio_webhook_enabled, request_options=request_options
        ).unwrap()

    def delete_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a message from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service_conversation_message(
            chat_service_sid,
            conversation_sid,
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            request_options=request_options,
        ).unwrap()

    def fetch_conversation_message(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConversationConversationMessage:
        """Fetch a message from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_conversation_message(
            conversation_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationMessage:
        """Fetch a message from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_conversation_message(
            chat_service_sid, conversation_sid, sid, request_options=request_options
        ).unwrap()

    def list_conversation_message(
        self,
        conversation_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationMessageResponse:
        """Retrieve a list of all messages in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for messages.
            order: The sort order of the returned messages. Can be: ``asc`` (ascending) or ``desc`` (descending), with
                ``asc`` as the default.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_conversation_message(
            conversation_sid,
            order=order,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def list_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationMessageResponse:
        """Retrieve a list of all messages in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for messages.
            order: The sort order of the returned messages. Can be: ``asc`` (ascending) or ``desc`` (descending), with
                ``asc`` as the default.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_conversation_message(
            chat_service_sid,
            conversation_sid,
            order=order,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_conversation_message(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationMessage:
        """Update an existing message in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_conversation_message(
            conversation_sid,
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            author=author,
            body=body,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            subject=subject,
            request_options=request_options,
        ).unwrap()

    def update_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationMessage:
        """Update an existing message in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_conversation_message(
            chat_service_sid,
            conversation_sid,
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            author=author,
            body=body,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            subject=subject,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1MessageWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1Message:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1MessageWithRawResponse(client, server, auth)

    async def create_conversation_message(
        self,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        media_sid: str | None = None,
        content_sid: str | None = None,
        content_variables: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationMessage:
        """Add a new message to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            media_sid: The Media SID to be attached to the new Message.
            content_sid: The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__
                template, required for template-generated messages. **Note** that if this field is set, ``Body`` and
                ``MediaSid`` parameters are ignored.
            content_variables: A structurally valid JSON string that contains values to resolve Rich Content template
                variables.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_conversation_message(
                conversation_sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                author=author,
                body=body,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                media_sid=media_sid,
                content_sid=content_sid,
                content_variables=content_variables,
                subject=subject,
                request_options=request_options,
            )
        ).unwrap()

    async def create_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        media_sid: str | None = None,
        content_sid: str | None = None,
        content_variables: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationMessage:
        """Add a new message to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            media_sid: The Media SID to be attached to the new Message.
            content_sid: The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__
                template, required for template-generated messages. **Note** that if this field is set, ``Body`` and
                ``MediaSid`` parameters are ignored.
            content_variables: A structurally valid JSON string that contains values to resolve Rich Content template
                variables.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service_conversation_message(
                chat_service_sid,
                conversation_sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                author=author,
                body=body,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                media_sid=media_sid,
                content_sid=content_sid,
                content_variables=content_variables,
                subject=subject,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_conversation_message(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a message from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_conversation_message(
                conversation_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a message from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_service_conversation_message(
                chat_service_sid,
                conversation_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_conversation_message(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConversationConversationMessage:
        """Fetch a message from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_conversation_message(
                conversation_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationMessage:
        """Fetch a message from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_conversation_message(
                chat_service_sid, conversation_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_conversation_message(
        self,
        conversation_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationMessageResponse:
        """Retrieve a list of all messages in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for messages.
            order: The sort order of the returned messages. Can be: ``asc`` (ascending) or ``desc`` (descending), with
                ``asc`` as the default.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_conversation_message(
                conversation_sid,
                order=order,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def list_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationMessageResponse:
        """Retrieve a list of all messages in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for messages.
            order: The sort order of the returned messages. Can be: ``asc`` (ascending) or ``desc`` (descending), with
                ``asc`` as the default.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_conversation_message(
                chat_service_sid,
                conversation_sid,
                order=order,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_conversation_message(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationMessage:
        """Update an existing message in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_conversation_message(
                conversation_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                author=author,
                body=body,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                subject=subject,
                request_options=request_options,
            )
        ).unwrap()

    async def update_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationMessage:
        """Update an existing message in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_conversation_message(
                chat_service_sid,
                conversation_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                author=author,
                body=body,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                subject=subject,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1MessageWithRawResponse:
        return self._with_raw_response


class ConversationsV1MessageWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_conversation_message(
        self,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        media_sid: str | None = None,
        content_sid: str | None = None,
        content_variables: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationMessage, RawError]:
        """Add a new message to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            media_sid: The Media SID to be attached to the new Message.
            content_sid: The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__
                template, required for template-generated messages. **Note** that if this field is set, ``Body`` and
                ``MediaSid`` parameters are ignored.
            content_variables: A structurally valid JSON string that contains values to resolve Rich Content template
                variables.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Author", author),
                    param[str | None]("Body", body),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MediaSid", media_sid),
                    param[str | None]("ContentSid", content_sid),
                    param[str | None]("ContentVariables", content_variables),
                    param[str | None]("Subject", subject),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        media_sid: str | None = None,
        content_sid: str | None = None,
        content_variables: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]:
        """Add a new message to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            media_sid: The Media SID to be attached to the new Message.
            content_sid: The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__
                template, required for template-generated messages. **Note** that if this field is set, ``Body`` and
                ``MediaSid`` parameters are ignored.
            content_variables: A structurally valid JSON string that contains values to resolve Rich Content template
                variables.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Author", author),
                    param[str | None]("Body", body),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MediaSid", media_sid),
                    param[str | None]("ContentSid", content_sid),
                    param[str | None]("ContentVariables", content_variables),
                    param[str | None]("Subject", subject),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_conversation_message(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a message from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a message from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_conversation_message(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConversationConversationMessage, RawError]:
        """Fetch a message from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]:
        """Fetch a message from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_conversation_message(
        self,
        conversation_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationMessageResponse, RawError]:
        """Retrieve a list of all messages in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for messages.
            order: The sort order of the returned messages. Can be: ``asc`` (ascending) or ``desc`` (descending), with
                ``asc`` as the default.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[
                param[ChallengeEnumListOrdersOrStr | None]("Order", order),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationMessageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationMessageResponse, RawError]:
        """Retrieve a list of all messages in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for messages.
            order: The sort order of the returned messages. Can be: ``asc`` (ascending) or ``desc`` (descending), with
                ``asc`` as the default.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            query_params=[
                param[ChallengeEnumListOrdersOrStr | None]("Order", order),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceConversationMessageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_conversation_message(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationMessage, RawError]:
        """Update an existing message in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Author", author),
                    param[str | None]("Body", body),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("Subject", subject),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]:
        """Update an existing message in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Author", author),
                    param[str | None]("Body", body),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("Subject", subject),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1MessageWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_conversation_message(
        self,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        media_sid: str | None = None,
        content_sid: str | None = None,
        content_variables: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationMessage, RawError]:
        """Add a new message to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            media_sid: The Media SID to be attached to the new Message.
            content_sid: The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__
                template, required for template-generated messages. **Note** that if this field is set, ``Body`` and
                ``MediaSid`` parameters are ignored.
            content_variables: A structurally valid JSON string that contains values to resolve Rich Content template
                variables.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Author", author),
                    param[str | None]("Body", body),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MediaSid", media_sid),
                    param[str | None]("ContentSid", content_sid),
                    param[str | None]("ContentVariables", content_variables),
                    param[str | None]("Subject", subject),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        media_sid: str | None = None,
        content_sid: str | None = None,
        content_variables: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]:
        """Add a new message to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            media_sid: The Media SID to be attached to the new Message.
            content_sid: The unique ID of the multi-channel `Rich Content <https://www.twilio.com/docs/content>`__
                template, required for template-generated messages. **Note** that if this field is set, ``Body`` and
                ``MediaSid`` parameters are ignored.
            content_variables: A structurally valid JSON string that contains values to resolve Rich Content template
                variables.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Author", author),
                    param[str | None]("Body", body),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MediaSid", media_sid),
                    param[str | None]("ContentSid", content_sid),
                    param[str | None]("ContentVariables", content_variables),
                    param[str | None]("Subject", subject),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_conversation_message(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a message from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a message from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_conversation_message(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConversationConversationMessage, RawError]:
        """Fetch a message from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]:
        """Fetch a message from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_conversation_message(
        self,
        conversation_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationMessageResponse, RawError]:
        """Retrieve a list of all messages in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for messages.
            order: The sort order of the returned messages. Can be: ``asc`` (ascending) or ``desc`` (descending), with
                ``asc`` as the default.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[
                param[ChallengeEnumListOrdersOrStr | None]("Order", order),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationMessageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        order: ChallengeEnumListOrdersOrStr | None = None,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationMessageResponse, RawError]:
        """Retrieve a list of all messages in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for messages.
            order: The sort order of the returned messages. Can be: ``asc`` (ascending) or ``desc`` (descending), with
                ``asc`` as the default.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            query_params=[
                param[ChallengeEnumListOrdersOrStr | None]("Order", order),
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceConversationMessageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_conversation_message(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationMessage, RawError]:
        """Update an existing message in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Messages/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Author", author),
                    param[str | None]("Body", body),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("Subject", subject),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_conversation_message(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        author: str | None = None,
        body: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        subject: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationMessage, RawError]:
        """Update an existing message in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this message.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            author: The channel specific identifier of the message's author. Defaults to ``system``.
            body: The content of the message, can be up to 1,600 characters long.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated. ``null`` if the message has not been edited.
            attributes: A string metadata field you can use to store any data you wish. The string value must contain
                structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.
            subject: The subject of the message, can be up to 256 characters long.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Author", author),
                    param[str | None]("Body", body),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("Subject", subject),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationMessage],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
