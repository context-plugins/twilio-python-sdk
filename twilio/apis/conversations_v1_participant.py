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
from ..models.conversations_v1_conversation_conversation_participant import (
    ConversationsV1ConversationConversationParticipant,
)
from ..models.conversations_v1_service_service_conversation_service_conversation_participant import (
    ConversationsV1ServiceServiceConversationServiceConversationParticipant,
)
from ..models.enums.confirmation import ConfirmationOrStr
from ..models.list_conversation_participant_response import ListConversationParticipantResponse
from ..models.list_service_conversation_participant_response import ListServiceConversationParticipantResponse
from ..server.server import Server


class ConversationsV1Participant:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1ParticipantWithRawResponse(client, server, auth)

    def create_conversation_participant(
        self,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        identity: str | None = None,
        messaging_binding_address: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_binding_projected_address: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationParticipant:
        """Add a new participant to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number.
                Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address)
                is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
            messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the
                participant is in contact with. This field, together with participant address, is only null when the
                participant is interacting from an SDK endpoint (see the 'identity' field).
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                Communication mask for the Conversation participant with Identity.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_conversation_participant(
            conversation_sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            identity=identity,
            messaging_binding_address=messaging_binding_address,
            messaging_binding_proxy_address=messaging_binding_proxy_address,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            messaging_binding_projected_address=messaging_binding_projected_address,
            role_sid=role_sid,
            request_options=request_options,
        ).unwrap()

    def create_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        identity: str | None = None,
        messaging_binding_address: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_binding_projected_address: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationParticipant:
        """Add a new participant to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the `Conversation SDK
                <https://www.twilio.com/docs/conversations/sdk-overview>`__ to communicate. Limited to 256 characters.
            messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number.
                Together with the Proxy address, this determines a participant uniquely. This field (with
                ``proxy_address``) is only null when the participant is interacting from an SDK endpoint (see the
                ``identity`` field).
            messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the
                participant is in contact with. This field, together with participant address, is only null when the
                participant is interacting from an SDK endpoint (see the ``identity`` field).
            date_created: The date on which this resource was created.
            date_updated: The date on which this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set ``{}`` will be
                returned.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service_conversation_participant(
            chat_service_sid,
            conversation_sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            identity=identity,
            messaging_binding_address=messaging_binding_address,
            messaging_binding_proxy_address=messaging_binding_proxy_address,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            messaging_binding_projected_address=messaging_binding_projected_address,
            role_sid=role_sid,
            request_options=request_options,
        ).unwrap()

    def delete_conversation_participant(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a participant from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_conversation_participant(
            conversation_sid, sid, x_twilio_webhook_enabled=x_twilio_webhook_enabled, request_options=request_options
        ).unwrap()

    def delete_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a participant from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service_conversation_participant(
            chat_service_sid,
            conversation_sid,
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            request_options=request_options,
        ).unwrap()

    def fetch_conversation_participant(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConversationConversationParticipant:
        """Fetch a participant of the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a
                Participant's ``identity`` rather than the SID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_conversation_participant(
            conversation_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationParticipant:
        """Fetch a participant of the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a
                Participant's ``identity`` rather than the SID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_conversation_participant(
            chat_service_sid, conversation_sid, sid, request_options=request_options
        ).unwrap()

    def list_conversation_participant(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationParticipantResponse:
        """Retrieve a list of all participants of the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for participants.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_conversation_participant(
            conversation_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def list_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationParticipantResponse:
        """Retrieve a list of all participants of the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for participants.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_conversation_participant(
            chat_service_sid,
            conversation_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_conversation_participant(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        messaging_binding_projected_address: str | None = None,
        identity: str | None = None,
        last_read_message_index: int | None = None,
        last_read_timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationParticipant:
        """Update an existing participant in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact
                with. 'null' value will remove it.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                'null' value will remove it.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            last_read_message_index: Index of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            last_read_timestamp: Timestamp of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_conversation_participant(
            conversation_sid,
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            role_sid=role_sid,
            messaging_binding_proxy_address=messaging_binding_proxy_address,
            messaging_binding_projected_address=messaging_binding_projected_address,
            identity=identity,
            last_read_message_index=last_read_message_index,
            last_read_timestamp=last_read_timestamp,
            request_options=request_options,
        ).unwrap()

    def update_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        identity: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        messaging_binding_projected_address: str | None = None,
        last_read_message_index: int | None = None,
        last_read_timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationParticipant:
        """Update an existing participant in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            date_created: The date on which this resource was created.
            date_updated: The date on which this resource was last updated.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the `Conversation SDK
                <https://www.twilio.com/docs/conversations/sdk-overview>`__ to communicate. Limited to 256 characters.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set ``{}`` will be
                returned.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact
                with. 'null' value will remove it.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                'null' value will remove it.
            last_read_message_index: Index of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            last_read_timestamp: Timestamp of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_conversation_participant(
            chat_service_sid,
            conversation_sid,
            sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            date_created=date_created,
            date_updated=date_updated,
            identity=identity,
            attributes=attributes,
            role_sid=role_sid,
            messaging_binding_proxy_address=messaging_binding_proxy_address,
            messaging_binding_projected_address=messaging_binding_projected_address,
            last_read_message_index=last_read_message_index,
            last_read_timestamp=last_read_timestamp,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1ParticipantWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1Participant:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1ParticipantWithRawResponse(client, server, auth)

    async def create_conversation_participant(
        self,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        identity: str | None = None,
        messaging_binding_address: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_binding_projected_address: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationParticipant:
        """Add a new participant to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number.
                Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address)
                is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
            messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the
                participant is in contact with. This field, together with participant address, is only null when the
                participant is interacting from an SDK endpoint (see the 'identity' field).
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                Communication mask for the Conversation participant with Identity.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_conversation_participant(
                conversation_sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                identity=identity,
                messaging_binding_address=messaging_binding_address,
                messaging_binding_proxy_address=messaging_binding_proxy_address,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                messaging_binding_projected_address=messaging_binding_projected_address,
                role_sid=role_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def create_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        identity: str | None = None,
        messaging_binding_address: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_binding_projected_address: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationParticipant:
        """Add a new participant to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the `Conversation SDK
                <https://www.twilio.com/docs/conversations/sdk-overview>`__ to communicate. Limited to 256 characters.
            messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number.
                Together with the Proxy address, this determines a participant uniquely. This field (with
                ``proxy_address``) is only null when the participant is interacting from an SDK endpoint (see the
                ``identity`` field).
            messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the
                participant is in contact with. This field, together with participant address, is only null when the
                participant is interacting from an SDK endpoint (see the ``identity`` field).
            date_created: The date on which this resource was created.
            date_updated: The date on which this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set ``{}`` will be
                returned.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service_conversation_participant(
                chat_service_sid,
                conversation_sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                identity=identity,
                messaging_binding_address=messaging_binding_address,
                messaging_binding_proxy_address=messaging_binding_proxy_address,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                messaging_binding_projected_address=messaging_binding_projected_address,
                role_sid=role_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_conversation_participant(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a participant from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_conversation_participant(
                conversation_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a participant from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_service_conversation_participant(
                chat_service_sid,
                conversation_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                request_options=request_options,
            )
        ).unwrap()

    async def fetch_conversation_participant(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConversationConversationParticipant:
        """Fetch a participant of the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a
                Participant's ``identity`` rather than the SID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_conversation_participant(
                conversation_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationParticipant:
        """Fetch a participant of the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a
                Participant's ``identity`` rather than the SID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_conversation_participant(
                chat_service_sid, conversation_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_conversation_participant(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationParticipantResponse:
        """Retrieve a list of all participants of the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for participants.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_conversation_participant(
                conversation_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def list_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationParticipantResponse:
        """Retrieve a list of all participants of the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for participants.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_conversation_participant(
                chat_service_sid,
                conversation_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_conversation_participant(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        messaging_binding_projected_address: str | None = None,
        identity: str | None = None,
        last_read_message_index: int | None = None,
        last_read_timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationParticipant:
        """Update an existing participant in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact
                with. 'null' value will remove it.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                'null' value will remove it.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            last_read_message_index: Index of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            last_read_timestamp: Timestamp of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_conversation_participant(
                conversation_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                date_created=date_created,
                date_updated=date_updated,
                attributes=attributes,
                role_sid=role_sid,
                messaging_binding_proxy_address=messaging_binding_proxy_address,
                messaging_binding_projected_address=messaging_binding_projected_address,
                identity=identity,
                last_read_message_index=last_read_message_index,
                last_read_timestamp=last_read_timestamp,
                request_options=request_options,
            )
        ).unwrap()

    async def update_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        identity: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        messaging_binding_projected_address: str | None = None,
        last_read_message_index: int | None = None,
        last_read_timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationParticipant:
        """Update an existing participant in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            date_created: The date on which this resource was created.
            date_updated: The date on which this resource was last updated.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the `Conversation SDK
                <https://www.twilio.com/docs/conversations/sdk-overview>`__ to communicate. Limited to 256 characters.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set ``{}`` will be
                returned.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact
                with. 'null' value will remove it.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                'null' value will remove it.
            last_read_message_index: Index of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            last_read_timestamp: Timestamp of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_conversation_participant(
                chat_service_sid,
                conversation_sid,
                sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                date_created=date_created,
                date_updated=date_updated,
                identity=identity,
                attributes=attributes,
                role_sid=role_sid,
                messaging_binding_proxy_address=messaging_binding_proxy_address,
                messaging_binding_projected_address=messaging_binding_projected_address,
                last_read_message_index=last_read_message_index,
                last_read_timestamp=last_read_timestamp,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1ParticipantWithRawResponse:
        return self._with_raw_response


class ConversationsV1ParticipantWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_conversation_participant(
        self,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        identity: str | None = None,
        messaging_binding_address: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_binding_projected_address: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationParticipant, RawError]:
        """Add a new participant to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number.
                Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address)
                is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
            messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the
                participant is in contact with. This field, together with participant address, is only null when the
                participant is interacting from an SDK endpoint (see the 'identity' field).
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                Communication mask for the Conversation participant with Identity.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Identity", identity),
                    param[str | None]("MessagingBinding.Address", messaging_binding_address),
                    param[str | None]("MessagingBinding.ProxyAddress", messaging_binding_proxy_address),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingBinding.ProjectedAddress", messaging_binding_projected_address),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        identity: str | None = None,
        messaging_binding_address: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_binding_projected_address: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]:
        """Add a new participant to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the `Conversation SDK
                <https://www.twilio.com/docs/conversations/sdk-overview>`__ to communicate. Limited to 256 characters.
            messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number.
                Together with the Proxy address, this determines a participant uniquely. This field (with
                ``proxy_address``) is only null when the participant is interacting from an SDK endpoint (see the
                ``identity`` field).
            messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the
                participant is in contact with. This field, together with participant address, is only null when the
                participant is interacting from an SDK endpoint (see the ``identity`` field).
            date_created: The date on which this resource was created.
            date_updated: The date on which this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set ``{}`` will be
                returned.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Identity", identity),
                    param[str | None]("MessagingBinding.Address", messaging_binding_address),
                    param[str | None]("MessagingBinding.ProxyAddress", messaging_binding_proxy_address),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingBinding.ProjectedAddress", messaging_binding_projected_address),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_conversation_participant(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a participant from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a participant from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}"
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

    def fetch_conversation_participant(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConversationConversationParticipant, RawError]:
        """Fetch a participant of the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a
                Participant's ``identity`` rather than the SID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]:
        """Fetch a participant of the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a
                Participant's ``identity`` rather than the SID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_conversation_participant(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationParticipantResponse, RawError]:
        """Retrieve a list of all participants of the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for participants.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationParticipantResponse, RawError]:
        """Retrieve a list of all participants of the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for participants.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceConversationParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_conversation_participant(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        messaging_binding_projected_address: str | None = None,
        identity: str | None = None,
        last_read_message_index: int | None = None,
        last_read_timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationParticipant, RawError]:
        """Update an existing participant in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact
                with. 'null' value will remove it.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                'null' value will remove it.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            last_read_message_index: Index of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            last_read_timestamp: Timestamp of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                    param[str | None]("MessagingBinding.ProxyAddress", messaging_binding_proxy_address),
                    param[str | None]("MessagingBinding.ProjectedAddress", messaging_binding_projected_address),
                    param[str | None]("Identity", identity),
                    param[int | None]("LastReadMessageIndex", last_read_message_index),
                    param[str | None]("LastReadTimestamp", last_read_timestamp),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        identity: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        messaging_binding_projected_address: str | None = None,
        last_read_message_index: int | None = None,
        last_read_timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]:
        """Update an existing participant in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            date_created: The date on which this resource was created.
            date_updated: The date on which this resource was last updated.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the `Conversation SDK
                <https://www.twilio.com/docs/conversations/sdk-overview>`__ to communicate. Limited to 256 characters.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set ``{}`` will be
                returned.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact
                with. 'null' value will remove it.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                'null' value will remove it.
            last_read_message_index: Index of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            last_read_timestamp: Timestamp of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Identity", identity),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                    param[str | None]("MessagingBinding.ProxyAddress", messaging_binding_proxy_address),
                    param[str | None]("MessagingBinding.ProjectedAddress", messaging_binding_projected_address),
                    param[int | None]("LastReadMessageIndex", last_read_message_index),
                    param[str | None]("LastReadTimestamp", last_read_timestamp),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1ParticipantWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_conversation_participant(
        self,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        identity: str | None = None,
        messaging_binding_address: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_binding_projected_address: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationParticipant, RawError]:
        """Add a new participant to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number.
                Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address)
                is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
            messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the
                participant is in contact with. This field, together with participant address, is only null when the
                participant is interacting from an SDK endpoint (see the 'identity' field).
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                Communication mask for the Conversation participant with Identity.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Identity", identity),
                    param[str | None]("MessagingBinding.Address", messaging_binding_address),
                    param[str | None]("MessagingBinding.ProxyAddress", messaging_binding_proxy_address),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingBinding.ProjectedAddress", messaging_binding_projected_address),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        identity: str | None = None,
        messaging_binding_address: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        messaging_binding_projected_address: str | None = None,
        role_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]:
        """Add a new participant to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the `Conversation SDK
                <https://www.twilio.com/docs/conversations/sdk-overview>`__ to communicate. Limited to 256 characters.
            messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number.
                Together with the Proxy address, this determines a participant uniquely. This field (with
                ``proxy_address``) is only null when the participant is interacting from an SDK endpoint (see the
                ``identity`` field).
            messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the
                participant is in contact with. This field, together with participant address, is only null when the
                participant is interacting from an SDK endpoint (see the ``identity`` field).
            date_created: The date on which this resource was created.
            date_updated: The date on which this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set ``{}`` will be
                returned.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[str | None]("Identity", identity),
                    param[str | None]("MessagingBinding.Address", messaging_binding_address),
                    param[str | None]("MessagingBinding.ProxyAddress", messaging_binding_proxy_address),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("MessagingBinding.ProjectedAddress", messaging_binding_projected_address),
                    param[str | None]("RoleSid", role_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_conversation_participant(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a participant from the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a participant from the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}"
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

    async def fetch_conversation_participant(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConversationConversationParticipant, RawError]:
        """Fetch a participant of the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a
                Participant's ``identity`` rather than the SID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]:
        """Fetch a participant of the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource. Alternatively, you can pass a
                Participant's ``identity`` rather than the SID.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_conversation_participant(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationParticipantResponse, RawError]:
        """Retrieve a list of all participants of the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for participants.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationParticipantResponse, RawError]:
        """Retrieve a list of all participants of the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for participants.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 100.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListServiceConversationParticipantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_conversation_participant(
        self,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        messaging_binding_projected_address: str | None = None,
        identity: str | None = None,
        last_read_message_index: int | None = None,
        last_read_timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationParticipant, RawError]:
        """Update an existing participant in the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact
                with. 'null' value will remove it.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                'null' value will remove it.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
            last_read_message_index: Index of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            last_read_timestamp: Timestamp of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Participants/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                    param[str | None]("MessagingBinding.ProxyAddress", messaging_binding_proxy_address),
                    param[str | None]("MessagingBinding.ProjectedAddress", messaging_binding_projected_address),
                    param[str | None]("Identity", identity),
                    param[int | None]("LastReadMessageIndex", last_read_message_index),
                    param[str | None]("LastReadTimestamp", last_read_timestamp),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_conversation_participant(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        identity: str | None = None,
        attributes: str | None = None,
        role_sid: str | None = None,
        messaging_binding_proxy_address: str | None = None,
        messaging_binding_projected_address: str | None = None,
        last_read_message_index: int | None = None,
        last_read_timestamp: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationParticipant, RawError]:
        """Update an existing participant in the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this participant.
            sid: A 34 character string that uniquely identifies this resource.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            date_created: The date on which this resource was created.
            date_updated: The date on which this resource was last updated.
            identity: A unique string identifier for the conversation participant as `Conversation User
                <https://www.twilio.com/docs/conversations/api/user-resource>`__. This parameter is non-null if (and
                only if) the participant is using the `Conversation SDK
                <https://www.twilio.com/docs/conversations/sdk-overview>`__ to communicate. Limited to 256 characters.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set ``{}`` will be
                returned.
            role_sid: The SID of a conversation-level `Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ to assign to the participant.
            messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact
                with. 'null' value will remove it.
            messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS.
                'null' value will remove it.
            last_read_message_index: Index of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            last_read_timestamp: Timestamp of last “read” message in the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for the Participant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            headers=[param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled)],
            body=form_body(
                [
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("Identity", identity),
                    param[str | None]("Attributes", attributes),
                    param[str | None]("RoleSid", role_sid),
                    param[str | None]("MessagingBinding.ProxyAddress", messaging_binding_proxy_address),
                    param[str | None]("MessagingBinding.ProjectedAddress", messaging_binding_projected_address),
                    param[int | None]("LastReadMessageIndex", last_read_message_index),
                    param[str | None]("LastReadTimestamp", last_read_timestamp),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationParticipant],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
