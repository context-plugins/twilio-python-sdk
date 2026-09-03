from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.conversations_v1_conversation_with_participants import ConversationsV1ConversationWithParticipants
from ..models.conversations_v1_service_service_conversation_with_participants import (
    ConversationsV1ServiceServiceConversationWithParticipants,
)
from ..models.enums.confirmation import ConfirmationOrStr
from ..models.enums.conversation_with_participants_enum_state import ConversationWithParticipantsEnumStateOrStr
from ..models.enums.service_conversation_with_participants_enum_state import (
    ServiceConversationWithParticipantsEnumStateOrStr,
)
from ..server.server import Server


class ConversationsV1ConversationWithParticipantsApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1ConversationWithParticipantsApiWithRawResponse(client, server, auth)

    def create_conversation_with_participants(
        self,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ConversationWithParticipantsEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        participant: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationWithParticipants:
        """Create a new conversation with the list of participants in your account's default service

        Args:
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            participant: The participant to be added to the conversation in JSON format. The JSON object attributes are
                as parameters in `Participant Resource
                <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__. The maximum number
                of participants that can be added in a single request is 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_conversation_with_participants(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            unique_name=unique_name,
            date_created=date_created,
            date_updated=date_updated,
            messaging_service_sid=messaging_service_sid,
            attributes=attributes,
            state=state,
            timers_inactive=timers_inactive,
            timers_closed=timers_closed,
            bindings_email_address=bindings_email_address,
            bindings_email_name=bindings_email_name,
            participant=participant,
            request_options=request_options,
        ).unwrap()

    def create_service_conversation_with_participants(
        self,
        chat_service_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ServiceConversationWithParticipantsEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        participant: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationWithParticipants:
        """Create a new conversation with the list of participants in your account's default service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            participant: The participant to be added to the conversation in JSON format. The JSON object attributes are
                as parameters in `Participant Resource
                <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__. The maximum number
                of participants that can be added in a single request is 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service_conversation_with_participants(
            chat_service_sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            unique_name=unique_name,
            date_created=date_created,
            date_updated=date_updated,
            messaging_service_sid=messaging_service_sid,
            attributes=attributes,
            state=state,
            timers_inactive=timers_inactive,
            timers_closed=timers_closed,
            bindings_email_address=bindings_email_address,
            bindings_email_name=bindings_email_name,
            participant=participant,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1ConversationWithParticipantsApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1ConversationWithParticipantsApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1ConversationWithParticipantsApiWithRawResponse(
            client, server, auth
        )

    async def create_conversation_with_participants(
        self,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ConversationWithParticipantsEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        participant: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationWithParticipants:
        """Create a new conversation with the list of participants in your account's default service

        Args:
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            participant: The participant to be added to the conversation in JSON format. The JSON object attributes are
                as parameters in `Participant Resource
                <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__. The maximum number
                of participants that can be added in a single request is 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_conversation_with_participants(
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                unique_name=unique_name,
                date_created=date_created,
                date_updated=date_updated,
                messaging_service_sid=messaging_service_sid,
                attributes=attributes,
                state=state,
                timers_inactive=timers_inactive,
                timers_closed=timers_closed,
                bindings_email_address=bindings_email_address,
                bindings_email_name=bindings_email_name,
                participant=participant,
                request_options=request_options,
            )
        ).unwrap()

    async def create_service_conversation_with_participants(
        self,
        chat_service_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ServiceConversationWithParticipantsEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        participant: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationWithParticipants:
        """Create a new conversation with the list of participants in your account's default service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            participant: The participant to be added to the conversation in JSON format. The JSON object attributes are
                as parameters in `Participant Resource
                <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__. The maximum number
                of participants that can be added in a single request is 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service_conversation_with_participants(
                chat_service_sid,
                x_twilio_webhook_enabled=x_twilio_webhook_enabled,
                friendly_name=friendly_name,
                unique_name=unique_name,
                date_created=date_created,
                date_updated=date_updated,
                messaging_service_sid=messaging_service_sid,
                attributes=attributes,
                state=state,
                timers_inactive=timers_inactive,
                timers_closed=timers_closed,
                bindings_email_address=bindings_email_address,
                bindings_email_name=bindings_email_name,
                participant=participant,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1ConversationWithParticipantsApiWithRawResponse:
        return self._with_raw_response


class ConversationsV1ConversationWithParticipantsApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_conversation_with_participants(
        self,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ConversationWithParticipantsEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        participant: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationWithParticipants, RawError]:
        """Create a new conversation with the list of participants in your account's default service

        Args:
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            participant: The participant to be added to the conversation in JSON format. The JSON object attributes are
                as parameters in `Participant Resource
                <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__. The maximum number
                of participants that can be added in a single request is 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/ConversationWithParticipants"),
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("UniqueName", unique_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[str | None]("Attributes", attributes),
                    param[ConversationWithParticipantsEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                    param[list[str] | None]("Participant", participant),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationWithParticipants],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_service_conversation_with_participants(
        self,
        chat_service_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ServiceConversationWithParticipantsEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        participant: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationWithParticipants, RawError]:
        """Create a new conversation with the list of participants in your account's default service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            participant: The participant to be added to the conversation in JSON format. The JSON object attributes are
                as parameters in `Participant Resource
                <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__. The maximum number
                of participants that can be added in a single request is 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/ConversationWithParticipants"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("UniqueName", unique_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[str | None]("Attributes", attributes),
                    param[ServiceConversationWithParticipantsEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                    param[list[str] | None]("Participant", participant),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationWithParticipants],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1ConversationWithParticipantsApiWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_conversation_with_participants(
        self,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ConversationWithParticipantsEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        participant: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationWithParticipants, RawError]:
        """Create a new conversation with the list of participants in your account's default service

        Args:
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            participant: The participant to be added to the conversation in JSON format. The JSON object attributes are
                as parameters in `Participant Resource
                <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__. The maximum number
                of participants that can be added in a single request is 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/ConversationWithParticipants"),
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("UniqueName", unique_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[str | None]("Attributes", attributes),
                    param[ConversationWithParticipantsEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                    param[list[str] | None]("Participant", participant),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationWithParticipants],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_service_conversation_with_participants(
        self,
        chat_service_sid: str,
        *,
        x_twilio_webhook_enabled: ConfirmationOrStr | None = None,
        friendly_name: str | None = None,
        unique_name: str | None = None,
        date_created: RFC3339DateTime | None = None,
        date_updated: RFC3339DateTime | None = None,
        messaging_service_sid: str | None = None,
        attributes: str | None = None,
        state: ServiceConversationWithParticipantsEnumStateOrStr | None = None,
        timers_inactive: str | None = None,
        timers_closed: str | None = None,
        bindings_email_address: str | None = None,
        bindings_email_name: str | None = None,
        participant: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationWithParticipants, RawError]:
        """Create a new conversation with the list of participants in your account's default service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Conversation resource is
                associated with.
            x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
            friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
            unique_name: An application-defined string that uniquely identifies the resource. It can be used to address
                the resource in place of the resource's ``sid`` in the URL.
            date_created: The date that this resource was created.
            date_updated: The date that this resource was last updated.
            messaging_service_sid: The unique ID of the `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ this conversation belongs to.
            attributes: An optional string metadata field you can use to store any data you wish. The string value must
                contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be
                returned.
            state: Current state of this conversation. Can be either ``initializing``, ``active``, ``inactive`` or
                ``closed`` and defaults to ``active``
            timers_inactive: ISO8601 duration when conversation will be switched to ``inactive`` state. Minimum value
                for this timer is 1 minute.
            timers_closed: ISO8601 duration when conversation will be switched to ``closed`` state. Minimum value for
                this timer is 10 minutes.
            bindings_email_address: The default email address that will be used when sending outbound emails in this
                conversation.
            bindings_email_name: The default name that will be used when sending outbound emails in this conversation.
            participant: The participant to be added to the conversation in JSON format. The JSON object attributes are
                as parameters in `Participant Resource
                <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__. The maximum number
                of participants that can be added in a single request is 10.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/ConversationWithParticipants"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[
                param[ConfirmationOrStr | None]("X-Twilio-Webhook-Enabled", x_twilio_webhook_enabled),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(
                [
                    param[str | None]("FriendlyName", friendly_name),
                    param[str | None]("UniqueName", unique_name),
                    param[RFC3339DateTime | None]("DateCreated", date_created),
                    param[RFC3339DateTime | None]("DateUpdated", date_updated),
                    param[str | None]("MessagingServiceSid", messaging_service_sid),
                    param[str | None]("Attributes", attributes),
                    param[ServiceConversationWithParticipantsEnumStateOrStr | None]("State", state),
                    param[str | None]("Timers.Inactive", timers_inactive),
                    param[str | None]("Timers.Closed", timers_closed),
                    param[str | None]("Bindings.Email.Address", bindings_email_address),
                    param[str | None]("Bindings.Email.Name", bindings_email_name),
                    param[list[str] | None]("Participant", participant),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationWithParticipants],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
