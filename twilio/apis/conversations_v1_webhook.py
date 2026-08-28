from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.conversations_v1_configuration_configuration_webhook import (
    ConversationsV1ConfigurationConfigurationWebhook,
)
from ..models.conversations_v1_conversation_conversation_scoped_webhook import (
    ConversationsV1ConversationConversationScopedWebhook,
)
from ..models.conversations_v1_service_service_configuration_service_webhook_configuration import (
    ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration,
)
from ..models.conversations_v1_service_service_conversation_service_conversation_scoped_webhook import (
    ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook,
)
from ..models.enums.configuration_webhook_enum_target import ConfigurationWebhookEnumTargetOrStr
from ..models.enums.conversation_scoped_webhook_enum_method import ConversationScopedWebhookEnumMethodOrStr
from ..models.enums.conversation_scoped_webhook_enum_target import ConversationScopedWebhookEnumTargetOrStr
from ..models.enums.service_conversation_scoped_webhook_enum_method import (
    ServiceConversationScopedWebhookEnumMethodOrStr,
)
from ..models.enums.service_conversation_scoped_webhook_enum_target import (
    ServiceConversationScopedWebhookEnumTargetOrStr,
)
from ..models.list_conversation_scoped_webhook_response import ListConversationScopedWebhookResponse
from ..models.list_service_conversation_scoped_webhook_response import ListServiceConversationScopedWebhookResponse
from ..server.server import Server


class ConversationsV1Webhook:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1WebhookWithRawResponse(client, server, auth)

    def create_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        target: ConversationScopedWebhookEnumTargetOrStr,
        *,
        configuration_url: str | None = None,
        configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        configuration_replay_after: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationScopedWebhook:
        """Create a new webhook scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            target: The target of this webhook: ``webhook``, ``studio``, ``trigger``
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            configuration_replay_after: The message index for which and it's successors the webhook will be replayed.
                Not set by default
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_conversation_scoped_webhook(
            conversation_sid,
            target,
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
            configuration_replay_after=configuration_replay_after,
            request_options=request_options,
        ).unwrap()

    def create_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        target: ServiceConversationScopedWebhookEnumTargetOrStr,
        *,
        configuration_url: str | None = None,
        configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        configuration_replay_after: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook:
        """Create a new webhook scoped to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            target: The target of this webhook: ``webhook``, ``studio``, ``trigger``
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            configuration_replay_after: The message index for which and it's successors the webhook will be replayed.
                Not set by default
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_service_conversation_scoped_webhook(
            chat_service_sid,
            conversation_sid,
            target,
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
            configuration_replay_after=configuration_replay_after,
            request_options=request_options,
        ).unwrap()

    def delete_conversation_scoped_webhook(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an existing webhook scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_conversation_scoped_webhook(
            conversation_sid, sid, request_options=request_options
        ).unwrap()

    def delete_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove an existing webhook scoped to the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_service_conversation_scoped_webhook(
            chat_service_sid, conversation_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_configuration_webhook(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConfigurationConfigurationWebhook:
        """A Webhook resource manages a service-level set of callback URLs and their configuration for receiving all
        conversation events.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_configuration_webhook(request_options=request_options).unwrap()

    def fetch_conversation_scoped_webhook(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConversationConversationScopedWebhook:
        """Fetch the configuration of a conversation-scoped webhook

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_conversation_scoped_webhook(
            conversation_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook:
        """Fetch the configuration of a conversation-scoped webhook

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_conversation_scoped_webhook(
            chat_service_sid, conversation_sid, sid, request_options=request_options
        ).unwrap()

    def fetch_service_webhook_configuration(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration:
        """Fetch a specific service webhook configuration.

        Args:
            chat_service_sid: The unique ID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ this conversation belongs to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_webhook_configuration(
            chat_service_sid, request_options=request_options
        ).unwrap()

    def list_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationScopedWebhookResponse:
        """Retrieve a list of all webhooks scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            page_size: How many resources to return in each list page. The default is 5, and the maximum is 5.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_conversation_scoped_webhook(
            conversation_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def list_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationScopedWebhookResponse:
        """Retrieve a list of all webhooks scoped to the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            page_size: How many resources to return in each list page. The default is 5, and the maximum is 5.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_service_conversation_scoped_webhook(
            chat_service_sid,
            conversation_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        ).unwrap()

    def update_configuration_webhook(
        self,
        *,
        method: str | None = None,
        filters: list[str] | None = None,
        pre_webhook_url: str | None = None,
        post_webhook_url: str | None = None,
        target: ConfigurationWebhookEnumTargetOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConfigurationConfigurationWebhook:
        """A Webhook resource manages a service-level set of callback URLs and their configuration for receiving all
        conversation events.

        Args:
            method: The HTTP method to be used when sending a webhook request.
            filters: The list of webhook event triggers that are enabled for this Service: ``onMessageAdded``,
                ``onMessageUpdated``, ``onMessageRemoved``, ``onMessageAdd``, ``onMessageUpdate``, ``onMessageRemove``,
                ``onConversationUpdated``, ``onConversationRemoved``, ``onConversationAdd``, ``onConversationAdded``,
                ``onConversationRemove``, ``onConversationUpdate``, ``onConversationStateUpdated``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onParticipantAdd``,
                ``onParticipantRemove``, ``onParticipantUpdate``, ``onDeliveryUpdated``, ``onUserAdded``,
                ``onUserUpdate``, ``onUserUpdated``
            pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
            post_webhook_url: The absolute url the post-event webhook request should be sent to.
            target: The routing target of the webhook. Can be ordinary or route internally to Flex
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_configuration_webhook(
            method=method,
            filters=filters,
            pre_webhook_url=pre_webhook_url,
            post_webhook_url=post_webhook_url,
            target=target,
            request_options=request_options,
        ).unwrap()

    def update_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        sid: str,
        *,
        configuration_url: str | None = None,
        configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationScopedWebhook:
        """Update an existing conversation-scoped webhook

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_conversation_scoped_webhook(
            conversation_sid,
            sid,
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
            request_options=request_options,
        ).unwrap()

    def update_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        configuration_url: str | None = None,
        configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook:
        """Update an existing conversation-scoped webhook

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_conversation_scoped_webhook(
            chat_service_sid,
            conversation_sid,
            sid,
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
            request_options=request_options,
        ).unwrap()

    def update_service_webhook_configuration(
        self,
        chat_service_sid: str,
        *,
        pre_webhook_url: str | None = None,
        post_webhook_url: str | None = None,
        filters: list[str] | None = None,
        method: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration:
        """Update a specific Webhook.

        Args:
            chat_service_sid: The unique ID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ this conversation belongs to.
            pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
            post_webhook_url: The absolute url the post-event webhook request should be sent to.
            filters: The list of events that your configured webhook targets will receive. Events not configured here
                will not fire. Possible values are ``onParticipantAdd``, ``onParticipantAdded``, ``onDeliveryUpdated``,
                ``onConversationUpdated``, ``onConversationRemove``, ``onParticipantRemove``, ``onConversationUpdate``,
                ``onMessageAdd``, ``onMessageRemoved``, ``onParticipantUpdated``, ``onConversationAdded``,
                ``onMessageAdded``, ``onConversationAdd``, ``onConversationRemoved``, ``onParticipantUpdate``,
                ``onMessageRemove``, ``onMessageUpdated``, ``onParticipantRemoved``, ``onMessageUpdate`` or
                ``onConversationStateUpdated``.
            method: The HTTP method to be used when sending a webhook request. One of ``GET`` or ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_webhook_configuration(
            chat_service_sid,
            pre_webhook_url=pre_webhook_url,
            post_webhook_url=post_webhook_url,
            filters=filters,
            method=method,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1WebhookWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1Webhook:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1WebhookWithRawResponse(client, server, auth)

    async def create_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        target: ConversationScopedWebhookEnumTargetOrStr,
        *,
        configuration_url: str | None = None,
        configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        configuration_replay_after: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationScopedWebhook:
        """Create a new webhook scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            target: The target of this webhook: ``webhook``, ``studio``, ``trigger``
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            configuration_replay_after: The message index for which and it's successors the webhook will be replayed.
                Not set by default
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_conversation_scoped_webhook(
                conversation_sid,
                target,
                configuration_url=configuration_url,
                configuration_method=configuration_method,
                configuration_filters=configuration_filters,
                configuration_triggers=configuration_triggers,
                configuration_flow_sid=configuration_flow_sid,
                configuration_replay_after=configuration_replay_after,
                request_options=request_options,
            )
        ).unwrap()

    async def create_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        target: ServiceConversationScopedWebhookEnumTargetOrStr,
        *,
        configuration_url: str | None = None,
        configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        configuration_replay_after: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook:
        """Create a new webhook scoped to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            target: The target of this webhook: ``webhook``, ``studio``, ``trigger``
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            configuration_replay_after: The message index for which and it's successors the webhook will be replayed.
                Not set by default
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_service_conversation_scoped_webhook(
                chat_service_sid,
                conversation_sid,
                target,
                configuration_url=configuration_url,
                configuration_method=configuration_method,
                configuration_filters=configuration_filters,
                configuration_triggers=configuration_triggers,
                configuration_flow_sid=configuration_flow_sid,
                configuration_replay_after=configuration_replay_after,
                request_options=request_options,
            )
        ).unwrap()

    async def delete_conversation_scoped_webhook(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove an existing webhook scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_conversation_scoped_webhook(
                conversation_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def delete_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove an existing webhook scoped to the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The resource was deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_service_conversation_scoped_webhook(
                chat_service_sid, conversation_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_configuration_webhook(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConfigurationConfigurationWebhook:
        """A Webhook resource manages a service-level set of callback URLs and their configuration for receiving all
        conversation events.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_configuration_webhook(request_options=request_options)).unwrap()

    async def fetch_conversation_scoped_webhook(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ConversationConversationScopedWebhook:
        """Fetch the configuration of a conversation-scoped webhook

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_conversation_scoped_webhook(
                conversation_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook:
        """Fetch the configuration of a conversation-scoped webhook

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_conversation_scoped_webhook(
                chat_service_sid, conversation_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def fetch_service_webhook_configuration(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration:
        """Fetch a specific service webhook configuration.

        Args:
            chat_service_sid: The unique ID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ this conversation belongs to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_webhook_configuration(
                chat_service_sid, request_options=request_options
            )
        ).unwrap()

    async def list_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListConversationScopedWebhookResponse:
        """Retrieve a list of all webhooks scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            page_size: How many resources to return in each list page. The default is 5, and the maximum is 5.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_conversation_scoped_webhook(
                conversation_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def list_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceConversationScopedWebhookResponse:
        """Retrieve a list of all webhooks scoped to the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            page_size: How many resources to return in each list page. The default is 5, and the maximum is 5.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_service_conversation_scoped_webhook(
                chat_service_sid,
                conversation_sid,
                page_size=page_size,
                page=page,
                page_token=page_token,
                request_options=request_options,
            )
        ).unwrap()

    async def update_configuration_webhook(
        self,
        *,
        method: str | None = None,
        filters: list[str] | None = None,
        pre_webhook_url: str | None = None,
        post_webhook_url: str | None = None,
        target: ConfigurationWebhookEnumTargetOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConfigurationConfigurationWebhook:
        """A Webhook resource manages a service-level set of callback URLs and their configuration for receiving all
        conversation events.

        Args:
            method: The HTTP method to be used when sending a webhook request.
            filters: The list of webhook event triggers that are enabled for this Service: ``onMessageAdded``,
                ``onMessageUpdated``, ``onMessageRemoved``, ``onMessageAdd``, ``onMessageUpdate``, ``onMessageRemove``,
                ``onConversationUpdated``, ``onConversationRemoved``, ``onConversationAdd``, ``onConversationAdded``,
                ``onConversationRemove``, ``onConversationUpdate``, ``onConversationStateUpdated``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onParticipantAdd``,
                ``onParticipantRemove``, ``onParticipantUpdate``, ``onDeliveryUpdated``, ``onUserAdded``,
                ``onUserUpdate``, ``onUserUpdated``
            pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
            post_webhook_url: The absolute url the post-event webhook request should be sent to.
            target: The routing target of the webhook. Can be ordinary or route internally to Flex
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_configuration_webhook(
                method=method,
                filters=filters,
                pre_webhook_url=pre_webhook_url,
                post_webhook_url=post_webhook_url,
                target=target,
                request_options=request_options,
            )
        ).unwrap()

    async def update_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        sid: str,
        *,
        configuration_url: str | None = None,
        configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ConversationConversationScopedWebhook:
        """Update an existing conversation-scoped webhook

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_conversation_scoped_webhook(
                conversation_sid,
                sid,
                configuration_url=configuration_url,
                configuration_method=configuration_method,
                configuration_filters=configuration_filters,
                configuration_triggers=configuration_triggers,
                configuration_flow_sid=configuration_flow_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def update_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        configuration_url: str | None = None,
        configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook:
        """Update an existing conversation-scoped webhook

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_conversation_scoped_webhook(
                chat_service_sid,
                conversation_sid,
                sid,
                configuration_url=configuration_url,
                configuration_method=configuration_method,
                configuration_filters=configuration_filters,
                configuration_triggers=configuration_triggers,
                configuration_flow_sid=configuration_flow_sid,
                request_options=request_options,
            )
        ).unwrap()

    async def update_service_webhook_configuration(
        self,
        chat_service_sid: str,
        *,
        pre_webhook_url: str | None = None,
        post_webhook_url: str | None = None,
        filters: list[str] | None = None,
        method: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration:
        """Update a specific Webhook.

        Args:
            chat_service_sid: The unique ID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ this conversation belongs to.
            pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
            post_webhook_url: The absolute url the post-event webhook request should be sent to.
            filters: The list of events that your configured webhook targets will receive. Events not configured here
                will not fire. Possible values are ``onParticipantAdd``, ``onParticipantAdded``, ``onDeliveryUpdated``,
                ``onConversationUpdated``, ``onConversationRemove``, ``onParticipantRemove``, ``onConversationUpdate``,
                ``onMessageAdd``, ``onMessageRemoved``, ``onParticipantUpdated``, ``onConversationAdded``,
                ``onMessageAdded``, ``onConversationAdd``, ``onConversationRemoved``, ``onParticipantUpdate``,
                ``onMessageRemove``, ``onMessageUpdated``, ``onParticipantRemoved``, ``onMessageUpdate`` or
                ``onConversationStateUpdated``.
            method: The HTTP method to be used when sending a webhook request. One of ``GET`` or ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_webhook_configuration(
                chat_service_sid,
                pre_webhook_url=pre_webhook_url,
                post_webhook_url=post_webhook_url,
                filters=filters,
                method=method,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1WebhookWithRawResponse:
        return self._with_raw_response


class ConversationsV1WebhookWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        target: ConversationScopedWebhookEnumTargetOrStr,
        *,
        configuration_url: str | None = None,
        configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        configuration_replay_after: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]:
        """Create a new webhook scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            target: The target of this webhook: ``webhook``, ``studio``, ``trigger``
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            configuration_replay_after: The message index for which and it's successors the webhook will be replayed.
                Not set by default
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            body=form_body(
                [
                    param[ConversationScopedWebhookEnumTargetOrStr]("Target", target),
                    param[str | None]("Configuration.Url", configuration_url),
                    param[ConversationScopedWebhookEnumMethodOrStr | None](
                        "Configuration.Method", configuration_method
                    ),
                    param[list[str] | None]("Configuration.Filters", configuration_filters),
                    param[list[str] | None]("Configuration.Triggers", configuration_triggers),
                    param[str | None]("Configuration.FlowSid", configuration_flow_sid),
                    param[int | None]("Configuration.ReplayAfter", configuration_replay_after),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        target: ServiceConversationScopedWebhookEnumTargetOrStr,
        *,
        configuration_url: str | None = None,
        configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        configuration_replay_after: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]:
        """Create a new webhook scoped to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            target: The target of this webhook: ``webhook``, ``studio``, ``trigger``
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            configuration_replay_after: The message index for which and it's successors the webhook will be replayed.
                Not set by default
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            body=form_body(
                [
                    param[ServiceConversationScopedWebhookEnumTargetOrStr]("Target", target),
                    param[str | None]("Configuration.Url", configuration_url),
                    param[ServiceConversationScopedWebhookEnumMethodOrStr | None](
                        "Configuration.Method", configuration_method
                    ),
                    param[list[str] | None]("Configuration.Filters", configuration_filters),
                    param[list[str] | None]("Configuration.Triggers", configuration_triggers),
                    param[str | None]("Configuration.FlowSid", configuration_flow_sid),
                    param[int | None]("Configuration.ReplayAfter", configuration_replay_after),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_conversation_scoped_webhook(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an existing webhook scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove an existing webhook scoped to the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_configuration_webhook(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConfigurationConfigurationWebhook, RawError]:
        """A Webhook resource manages a service-level set of callback URLs and their configuration for receiving all
        conversation events.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Configuration/Webhooks"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationConfigurationWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_conversation_scoped_webhook(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]:
        """Fetch the configuration of a conversation-scoped webhook

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]:
        """Fetch the configuration of a conversation-scoped webhook

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_webhook_configuration(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration, RawError]:
        """Fetch a specific service webhook configuration.

        Args:
            chat_service_sid: The unique ID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ this conversation belongs to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration/Webhooks"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationScopedWebhookResponse, RawError]:
        """Retrieve a list of all webhooks scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            page_size: How many resources to return in each list page. The default is 5, and the maximum is 5.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationScopedWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationScopedWebhookResponse, RawError]:
        """Retrieve a list of all webhooks scoped to the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            page_size: How many resources to return in each list page. The default is 5, and the maximum is 5.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks"
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
            decoder=json_decoder[ListServiceConversationScopedWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_configuration_webhook(
        self,
        *,
        method: str | None = None,
        filters: list[str] | None = None,
        pre_webhook_url: str | None = None,
        post_webhook_url: str | None = None,
        target: ConfigurationWebhookEnumTargetOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConfigurationConfigurationWebhook, RawError]:
        """A Webhook resource manages a service-level set of callback URLs and their configuration for receiving all
        conversation events.

        Args:
            method: The HTTP method to be used when sending a webhook request.
            filters: The list of webhook event triggers that are enabled for this Service: ``onMessageAdded``,
                ``onMessageUpdated``, ``onMessageRemoved``, ``onMessageAdd``, ``onMessageUpdate``, ``onMessageRemove``,
                ``onConversationUpdated``, ``onConversationRemoved``, ``onConversationAdd``, ``onConversationAdded``,
                ``onConversationRemove``, ``onConversationUpdate``, ``onConversationStateUpdated``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onParticipantAdd``,
                ``onParticipantRemove``, ``onParticipantUpdate``, ``onDeliveryUpdated``, ``onUserAdded``,
                ``onUserUpdate``, ``onUserUpdated``
            pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
            post_webhook_url: The absolute url the post-event webhook request should be sent to.
            target: The routing target of the webhook. Can be ordinary or route internally to Flex
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Configuration/Webhooks"),
            body=form_body(
                [
                    param[str | None]("Method", method),
                    param[list[str] | None]("Filters", filters),
                    param[str | None]("PreWebhookUrl", pre_webhook_url),
                    param[str | None]("PostWebhookUrl", post_webhook_url),
                    param[ConfigurationWebhookEnumTargetOrStr | None]("Target", target),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationConfigurationWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        sid: str,
        *,
        configuration_url: str | None = None,
        configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]:
        """Update an existing conversation-scoped webhook

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("Configuration.Url", configuration_url),
                    param[ConversationScopedWebhookEnumMethodOrStr | None](
                        "Configuration.Method", configuration_method
                    ),
                    param[list[str] | None]("Configuration.Filters", configuration_filters),
                    param[list[str] | None]("Configuration.Triggers", configuration_triggers),
                    param[str | None]("Configuration.FlowSid", configuration_flow_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        configuration_url: str | None = None,
        configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]:
        """Update an existing conversation-scoped webhook

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            body=form_body(
                [
                    param[str | None]("Configuration.Url", configuration_url),
                    param[ServiceConversationScopedWebhookEnumMethodOrStr | None](
                        "Configuration.Method", configuration_method
                    ),
                    param[list[str] | None]("Configuration.Filters", configuration_filters),
                    param[list[str] | None]("Configuration.Triggers", configuration_triggers),
                    param[str | None]("Configuration.FlowSid", configuration_flow_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_webhook_configuration(
        self,
        chat_service_sid: str,
        *,
        pre_webhook_url: str | None = None,
        post_webhook_url: str | None = None,
        filters: list[str] | None = None,
        method: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration, RawError]:
        """Update a specific Webhook.

        Args:
            chat_service_sid: The unique ID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ this conversation belongs to.
            pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
            post_webhook_url: The absolute url the post-event webhook request should be sent to.
            filters: The list of events that your configured webhook targets will receive. Events not configured here
                will not fire. Possible values are ``onParticipantAdd``, ``onParticipantAdded``, ``onDeliveryUpdated``,
                ``onConversationUpdated``, ``onConversationRemove``, ``onParticipantRemove``, ``onConversationUpdate``,
                ``onMessageAdd``, ``onMessageRemoved``, ``onParticipantUpdated``, ``onConversationAdded``,
                ``onMessageAdded``, ``onConversationAdd``, ``onConversationRemoved``, ``onParticipantUpdate``,
                ``onMessageRemove``, ``onMessageUpdated``, ``onParticipantRemoved``, ``onMessageUpdate`` or
                ``onConversationStateUpdated``.
            method: The HTTP method to be used when sending a webhook request. One of ``GET`` or ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration/Webhooks"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            body=form_body(
                [
                    param[str | None]("PreWebhookUrl", pre_webhook_url),
                    param[str | None]("PostWebhookUrl", post_webhook_url),
                    param[list[str] | None]("Filters", filters),
                    param[str | None]("Method", method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1WebhookWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        target: ConversationScopedWebhookEnumTargetOrStr,
        *,
        configuration_url: str | None = None,
        configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        configuration_replay_after: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]:
        """Create a new webhook scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            target: The target of this webhook: ``webhook``, ``studio``, ``trigger``
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            configuration_replay_after: The message index for which and it's successors the webhook will be replayed.
                Not set by default
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            body=form_body(
                [
                    param[ConversationScopedWebhookEnumTargetOrStr]("Target", target),
                    param[str | None]("Configuration.Url", configuration_url),
                    param[ConversationScopedWebhookEnumMethodOrStr | None](
                        "Configuration.Method", configuration_method
                    ),
                    param[list[str] | None]("Configuration.Filters", configuration_filters),
                    param[list[str] | None]("Configuration.Triggers", configuration_triggers),
                    param[str | None]("Configuration.FlowSid", configuration_flow_sid),
                    param[int | None]("Configuration.ReplayAfter", configuration_replay_after),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        target: ServiceConversationScopedWebhookEnumTargetOrStr,
        *,
        configuration_url: str | None = None,
        configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        configuration_replay_after: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]:
        """Create a new webhook scoped to the conversation in a specific service

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            target: The target of this webhook: ``webhook``, ``studio``, ``trigger``
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            configuration_replay_after: The message index for which and it's successors the webhook will be replayed.
                Not set by default
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid), param[str]("ConversationSid", conversation_sid)
            ],
            body=form_body(
                [
                    param[ServiceConversationScopedWebhookEnumTargetOrStr]("Target", target),
                    param[str | None]("Configuration.Url", configuration_url),
                    param[ServiceConversationScopedWebhookEnumMethodOrStr | None](
                        "Configuration.Method", configuration_method
                    ),
                    param[list[str] | None]("Configuration.Filters", configuration_filters),
                    param[list[str] | None]("Configuration.Triggers", configuration_triggers),
                    param[str | None]("Configuration.FlowSid", configuration_flow_sid),
                    param[int | None]("Configuration.ReplayAfter", configuration_replay_after),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_conversation_scoped_webhook(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Remove an existing webhook scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove an existing webhook scoped to the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_configuration_webhook(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConfigurationConfigurationWebhook, RawError]:
        """A Webhook resource manages a service-level set of callback URLs and their configuration for receiving all
        conversation events.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Configuration/Webhooks"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationConfigurationWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_conversation_scoped_webhook(
        self, conversation_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]:
        """Fetch the configuration of a conversation-scoped webhook

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]:
        """Fetch the configuration of a conversation-scoped webhook

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_webhook_configuration(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration, RawError]:
        """Fetch a specific service webhook configuration.

        Args:
            chat_service_sid: The unique ID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ this conversation belongs to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration/Webhooks"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListConversationScopedWebhookResponse, RawError]:
        """Retrieve a list of all webhooks scoped to the conversation

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            page_size: How many resources to return in each list page. The default is 5, and the maximum is 5.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks"),
            path_params=[param[str]("ConversationSid", conversation_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListConversationScopedWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceConversationScopedWebhookResponse, RawError]:
        """Retrieve a list of all webhooks scoped to the conversation

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            page_size: How many resources to return in each list page. The default is 5, and the maximum is 5.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks"
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
            decoder=json_decoder[ListServiceConversationScopedWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_configuration_webhook(
        self,
        *,
        method: str | None = None,
        filters: list[str] | None = None,
        pre_webhook_url: str | None = None,
        post_webhook_url: str | None = None,
        target: ConfigurationWebhookEnumTargetOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConfigurationConfigurationWebhook, RawError]:
        """A Webhook resource manages a service-level set of callback URLs and their configuration for receiving all
        conversation events.

        Args:
            method: The HTTP method to be used when sending a webhook request.
            filters: The list of webhook event triggers that are enabled for this Service: ``onMessageAdded``,
                ``onMessageUpdated``, ``onMessageRemoved``, ``onMessageAdd``, ``onMessageUpdate``, ``onMessageRemove``,
                ``onConversationUpdated``, ``onConversationRemoved``, ``onConversationAdd``, ``onConversationAdded``,
                ``onConversationRemove``, ``onConversationUpdate``, ``onConversationStateUpdated``,
                ``onParticipantAdded``, ``onParticipantUpdated``, ``onParticipantRemoved``, ``onParticipantAdd``,
                ``onParticipantRemove``, ``onParticipantUpdate``, ``onDeliveryUpdated``, ``onUserAdded``,
                ``onUserUpdate``, ``onUserUpdated``
            pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
            post_webhook_url: The absolute url the post-event webhook request should be sent to.
            target: The routing target of the webhook. Can be ordinary or route internally to Flex
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Configuration/Webhooks"),
            body=form_body(
                [
                    param[str | None]("Method", method),
                    param[list[str] | None]("Filters", filters),
                    param[str | None]("PreWebhookUrl", pre_webhook_url),
                    param[str | None]("PostWebhookUrl", post_webhook_url),
                    param[ConfigurationWebhookEnumTargetOrStr | None]("Target", target),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConfigurationConfigurationWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_conversation_scoped_webhook(
        self,
        conversation_sid: str,
        sid: str,
        *,
        configuration_url: str | None = None,
        configuration_method: ConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ConversationConversationScopedWebhook, RawError]:
        """Update an existing conversation-scoped webhook

        Args:
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Conversations/{ConversationSid}/Webhooks/{Sid}"),
            path_params=[param[str]("ConversationSid", conversation_sid), param[str]("Sid", sid)],
            body=form_body(
                [
                    param[str | None]("Configuration.Url", configuration_url),
                    param[ConversationScopedWebhookEnumMethodOrStr | None](
                        "Configuration.Method", configuration_method
                    ),
                    param[list[str] | None]("Configuration.Filters", configuration_filters),
                    param[list[str] | None]("Configuration.Triggers", configuration_triggers),
                    param[str | None]("Configuration.FlowSid", configuration_flow_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ConversationConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_conversation_scoped_webhook(
        self,
        chat_service_sid: str,
        conversation_sid: str,
        sid: str,
        *,
        configuration_url: str | None = None,
        configuration_method: ServiceConversationScopedWebhookEnumMethodOrStr | None = None,
        configuration_filters: list[str] | None = None,
        configuration_triggers: list[str] | None = None,
        configuration_flow_sid: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook, RawError]:
        """Update an existing conversation-scoped webhook

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Participant resource is
                associated with.
            conversation_sid: The unique ID of the `Conversation
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for this webhook.
            sid: A 34 character string that uniquely identifies this resource.
            configuration_url: The absolute url the webhook request should be sent to.
            configuration_method: Value sent with the request.
            configuration_filters: The list of events, firing webhook event for this Conversation.
            configuration_triggers: The list of keywords, firing webhook event for this Conversation.
            configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7(
                "/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}"
            ),
            path_params=[
                param[str]("ChatServiceSid", chat_service_sid),
                param[str]("ConversationSid", conversation_sid),
                param[str]("Sid", sid),
            ],
            body=form_body(
                [
                    param[str | None]("Configuration.Url", configuration_url),
                    param[ServiceConversationScopedWebhookEnumMethodOrStr | None](
                        "Configuration.Method", configuration_method
                    ),
                    param[list[str] | None]("Configuration.Filters", configuration_filters),
                    param[list[str] | None]("Configuration.Triggers", configuration_triggers),
                    param[str | None]("Configuration.FlowSid", configuration_flow_sid),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_webhook_configuration(
        self,
        chat_service_sid: str,
        *,
        pre_webhook_url: str | None = None,
        post_webhook_url: str | None = None,
        filters: list[str] | None = None,
        method: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration, RawError]:
        """Update a specific Webhook.

        Args:
            chat_service_sid: The unique ID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ this conversation belongs to.
            pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
            post_webhook_url: The absolute url the post-event webhook request should be sent to.
            filters: The list of events that your configured webhook targets will receive. Events not configured here
                will not fire. Possible values are ``onParticipantAdd``, ``onParticipantAdded``, ``onDeliveryUpdated``,
                ``onConversationUpdated``, ``onConversationRemove``, ``onParticipantRemove``, ``onConversationUpdate``,
                ``onMessageAdd``, ``onMessageRemoved``, ``onParticipantUpdated``, ``onConversationAdded``,
                ``onMessageAdded``, ``onConversationAdd``, ``onConversationRemoved``, ``onParticipantUpdate``,
                ``onMessageRemove``, ``onMessageUpdated``, ``onParticipantRemoved``, ``onMessageUpdate`` or
                ``onConversationStateUpdated``.
            method: The HTTP method to be used when sending a webhook request. One of ``GET`` or ``POST``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration/Webhooks"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            body=form_body(
                [
                    param[str | None]("PreWebhookUrl", pre_webhook_url),
                    param[str | None]("PostWebhookUrl", post_webhook_url),
                    param[list[str] | None]("Filters", filters),
                    param[str | None]("Method", method),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
