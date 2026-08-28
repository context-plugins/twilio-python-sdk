from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    form_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.conversations_v1_service_service_configuration_service_notification import (
    ConversationsV1ServiceServiceConfigurationServiceNotification,
)
from ..server.server import Server


class ConversationsV1Notification:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1NotificationWithRawResponse(client, server, auth)

    def fetch_service_notification(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceConfigurationServiceNotification:
        """Fetch push notification service settings

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Configuration applies to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_notification(
            chat_service_sid, request_options=request_options
        ).unwrap()

    def update_service_notification(
        self,
        chat_service_sid: str,
        *,
        log_enabled: bool | None = None,
        new_message_enabled: bool | None = None,
        new_message_template: str | None = None,
        new_message_sound: str | None = None,
        new_message_badge_count_enabled: bool | None = None,
        added_to_conversation_enabled: bool | None = None,
        added_to_conversation_template: str | None = None,
        added_to_conversation_sound: str | None = None,
        removed_from_conversation_enabled: bool | None = None,
        removed_from_conversation_template: str | None = None,
        removed_from_conversation_sound: str | None = None,
        new_message_with_media_enabled: bool | None = None,
        new_message_with_media_template: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConfigurationServiceNotification:
        """Update push notification service settings

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Configuration applies to.
            log_enabled: Weather the notification logging is enabled.
            new_message_enabled: Whether to send a notification when a new message is added to a conversation. The
                default is ``false``.
            new_message_template: The template to use to create the notification text displayed when a new message is
                added to a conversation and ``new_message.enabled`` is ``true``.
            new_message_sound: The name of the sound to play when a new message is added to a conversation and
                ``new_message.enabled`` is ``true``.
            new_message_badge_count_enabled: Whether the new message badge is enabled. The default is ``false``.
            added_to_conversation_enabled: Whether to send a notification when a participant is added to a conversation.
                The default is ``false``.
            added_to_conversation_template: The template to use to create the notification text displayed when a
                participant is added to a conversation and ``added_to_conversation.enabled`` is ``true``.
            added_to_conversation_sound: The name of the sound to play when a participant is added to a conversation and
                ``added_to_conversation.enabled`` is ``true``.
            removed_from_conversation_enabled: Whether to send a notification to a user when they are removed from a
                conversation. The default is ``false``.
            removed_from_conversation_template: The template to use to create the notification text displayed to a user
                when they are removed from a conversation and ``removed_from_conversation.enabled`` is ``true``.
            removed_from_conversation_sound: The name of the sound to play to a user when they are removed from a
                conversation and ``removed_from_conversation.enabled`` is ``true``.
            new_message_with_media_enabled: Whether to send a notification when a new message with media/file
                attachments is added to a conversation. The default is ``false``.
            new_message_with_media_template: The template to use to create the notification text displayed when a new
                message with media/file attachments is added to a conversation and ``new_message.attachments.enabled``
                is ``true``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_notification(
            chat_service_sid,
            log_enabled=log_enabled,
            new_message_enabled=new_message_enabled,
            new_message_template=new_message_template,
            new_message_sound=new_message_sound,
            new_message_badge_count_enabled=new_message_badge_count_enabled,
            added_to_conversation_enabled=added_to_conversation_enabled,
            added_to_conversation_template=added_to_conversation_template,
            added_to_conversation_sound=added_to_conversation_sound,
            removed_from_conversation_enabled=removed_from_conversation_enabled,
            removed_from_conversation_template=removed_from_conversation_template,
            removed_from_conversation_sound=removed_from_conversation_sound,
            new_message_with_media_enabled=new_message_with_media_enabled,
            new_message_with_media_template=new_message_with_media_template,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1NotificationWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1Notification:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1NotificationWithRawResponse(client, server, auth)

    async def fetch_service_notification(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceConfigurationServiceNotification:
        """Fetch push notification service settings

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Configuration applies to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_notification(chat_service_sid, request_options=request_options)
        ).unwrap()

    async def update_service_notification(
        self,
        chat_service_sid: str,
        *,
        log_enabled: bool | None = None,
        new_message_enabled: bool | None = None,
        new_message_template: str | None = None,
        new_message_sound: str | None = None,
        new_message_badge_count_enabled: bool | None = None,
        added_to_conversation_enabled: bool | None = None,
        added_to_conversation_template: str | None = None,
        added_to_conversation_sound: str | None = None,
        removed_from_conversation_enabled: bool | None = None,
        removed_from_conversation_template: str | None = None,
        removed_from_conversation_sound: str | None = None,
        new_message_with_media_enabled: bool | None = None,
        new_message_with_media_template: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConfigurationServiceNotification:
        """Update push notification service settings

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Configuration applies to.
            log_enabled: Weather the notification logging is enabled.
            new_message_enabled: Whether to send a notification when a new message is added to a conversation. The
                default is ``false``.
            new_message_template: The template to use to create the notification text displayed when a new message is
                added to a conversation and ``new_message.enabled`` is ``true``.
            new_message_sound: The name of the sound to play when a new message is added to a conversation and
                ``new_message.enabled`` is ``true``.
            new_message_badge_count_enabled: Whether the new message badge is enabled. The default is ``false``.
            added_to_conversation_enabled: Whether to send a notification when a participant is added to a conversation.
                The default is ``false``.
            added_to_conversation_template: The template to use to create the notification text displayed when a
                participant is added to a conversation and ``added_to_conversation.enabled`` is ``true``.
            added_to_conversation_sound: The name of the sound to play when a participant is added to a conversation and
                ``added_to_conversation.enabled`` is ``true``.
            removed_from_conversation_enabled: Whether to send a notification to a user when they are removed from a
                conversation. The default is ``false``.
            removed_from_conversation_template: The template to use to create the notification text displayed to a user
                when they are removed from a conversation and ``removed_from_conversation.enabled`` is ``true``.
            removed_from_conversation_sound: The name of the sound to play to a user when they are removed from a
                conversation and ``removed_from_conversation.enabled`` is ``true``.
            new_message_with_media_enabled: Whether to send a notification when a new message with media/file
                attachments is added to a conversation. The default is ``false``.
            new_message_with_media_template: The template to use to create the notification text displayed when a new
                message with media/file attachments is added to a conversation and ``new_message.attachments.enabled``
                is ``true``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_notification(
                chat_service_sid,
                log_enabled=log_enabled,
                new_message_enabled=new_message_enabled,
                new_message_template=new_message_template,
                new_message_sound=new_message_sound,
                new_message_badge_count_enabled=new_message_badge_count_enabled,
                added_to_conversation_enabled=added_to_conversation_enabled,
                added_to_conversation_template=added_to_conversation_template,
                added_to_conversation_sound=added_to_conversation_sound,
                removed_from_conversation_enabled=removed_from_conversation_enabled,
                removed_from_conversation_template=removed_from_conversation_template,
                removed_from_conversation_sound=removed_from_conversation_sound,
                new_message_with_media_enabled=new_message_with_media_enabled,
                new_message_with_media_template=new_message_with_media_template,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1NotificationWithRawResponse:
        return self._with_raw_response


class ConversationsV1NotificationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_service_notification(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceConfigurationServiceNotification, RawError]:
        """Fetch push notification service settings

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Configuration applies to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration/Notifications"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfigurationServiceNotification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_notification(
        self,
        chat_service_sid: str,
        *,
        log_enabled: bool | None = None,
        new_message_enabled: bool | None = None,
        new_message_template: str | None = None,
        new_message_sound: str | None = None,
        new_message_badge_count_enabled: bool | None = None,
        added_to_conversation_enabled: bool | None = None,
        added_to_conversation_template: str | None = None,
        added_to_conversation_sound: str | None = None,
        removed_from_conversation_enabled: bool | None = None,
        removed_from_conversation_template: str | None = None,
        removed_from_conversation_sound: str | None = None,
        new_message_with_media_enabled: bool | None = None,
        new_message_with_media_template: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConfigurationServiceNotification, RawError]:
        """Update push notification service settings

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Configuration applies to.
            log_enabled: Weather the notification logging is enabled.
            new_message_enabled: Whether to send a notification when a new message is added to a conversation. The
                default is ``false``.
            new_message_template: The template to use to create the notification text displayed when a new message is
                added to a conversation and ``new_message.enabled`` is ``true``.
            new_message_sound: The name of the sound to play when a new message is added to a conversation and
                ``new_message.enabled`` is ``true``.
            new_message_badge_count_enabled: Whether the new message badge is enabled. The default is ``false``.
            added_to_conversation_enabled: Whether to send a notification when a participant is added to a conversation.
                The default is ``false``.
            added_to_conversation_template: The template to use to create the notification text displayed when a
                participant is added to a conversation and ``added_to_conversation.enabled`` is ``true``.
            added_to_conversation_sound: The name of the sound to play when a participant is added to a conversation and
                ``added_to_conversation.enabled`` is ``true``.
            removed_from_conversation_enabled: Whether to send a notification to a user when they are removed from a
                conversation. The default is ``false``.
            removed_from_conversation_template: The template to use to create the notification text displayed to a user
                when they are removed from a conversation and ``removed_from_conversation.enabled`` is ``true``.
            removed_from_conversation_sound: The name of the sound to play to a user when they are removed from a
                conversation and ``removed_from_conversation.enabled`` is ``true``.
            new_message_with_media_enabled: Whether to send a notification when a new message with media/file
                attachments is added to a conversation. The default is ``false``.
            new_message_with_media_template: The template to use to create the notification text displayed when a new
                message with media/file attachments is added to a conversation and ``new_message.attachments.enabled``
                is ``true``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration/Notifications"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            body=form_body(
                [
                    param[bool | None]("LogEnabled", log_enabled),
                    param[bool | None]("NewMessage.Enabled", new_message_enabled),
                    param[str | None]("NewMessage.Template", new_message_template),
                    param[str | None]("NewMessage.Sound", new_message_sound),
                    param[bool | None]("NewMessage.BadgeCountEnabled", new_message_badge_count_enabled),
                    param[bool | None]("AddedToConversation.Enabled", added_to_conversation_enabled),
                    param[str | None]("AddedToConversation.Template", added_to_conversation_template),
                    param[str | None]("AddedToConversation.Sound", added_to_conversation_sound),
                    param[bool | None]("RemovedFromConversation.Enabled", removed_from_conversation_enabled),
                    param[str | None]("RemovedFromConversation.Template", removed_from_conversation_template),
                    param[str | None]("RemovedFromConversation.Sound", removed_from_conversation_sound),
                    param[bool | None]("NewMessage.WithMedia.Enabled", new_message_with_media_enabled),
                    param[str | None]("NewMessage.WithMedia.Template", new_message_with_media_template),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfigurationServiceNotification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1NotificationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_service_notification(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceConfigurationServiceNotification, RawError]:
        """Fetch push notification service settings

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Configuration applies to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration/Notifications"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfigurationServiceNotification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_notification(
        self,
        chat_service_sid: str,
        *,
        log_enabled: bool | None = None,
        new_message_enabled: bool | None = None,
        new_message_template: str | None = None,
        new_message_sound: str | None = None,
        new_message_badge_count_enabled: bool | None = None,
        added_to_conversation_enabled: bool | None = None,
        added_to_conversation_template: str | None = None,
        added_to_conversation_sound: str | None = None,
        removed_from_conversation_enabled: bool | None = None,
        removed_from_conversation_template: str | None = None,
        removed_from_conversation_sound: str | None = None,
        new_message_with_media_enabled: bool | None = None,
        new_message_with_media_template: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConfigurationServiceNotification, RawError]:
        """Update push notification service settings

        Args:
            chat_service_sid: The SID of the `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ the Configuration applies to.
            log_enabled: Weather the notification logging is enabled.
            new_message_enabled: Whether to send a notification when a new message is added to a conversation. The
                default is ``false``.
            new_message_template: The template to use to create the notification text displayed when a new message is
                added to a conversation and ``new_message.enabled`` is ``true``.
            new_message_sound: The name of the sound to play when a new message is added to a conversation and
                ``new_message.enabled`` is ``true``.
            new_message_badge_count_enabled: Whether the new message badge is enabled. The default is ``false``.
            added_to_conversation_enabled: Whether to send a notification when a participant is added to a conversation.
                The default is ``false``.
            added_to_conversation_template: The template to use to create the notification text displayed when a
                participant is added to a conversation and ``added_to_conversation.enabled`` is ``true``.
            added_to_conversation_sound: The name of the sound to play when a participant is added to a conversation and
                ``added_to_conversation.enabled`` is ``true``.
            removed_from_conversation_enabled: Whether to send a notification to a user when they are removed from a
                conversation. The default is ``false``.
            removed_from_conversation_template: The template to use to create the notification text displayed to a user
                when they are removed from a conversation and ``removed_from_conversation.enabled`` is ``true``.
            removed_from_conversation_sound: The name of the sound to play to a user when they are removed from a
                conversation and ``removed_from_conversation.enabled`` is ``true``.
            new_message_with_media_enabled: Whether to send a notification when a new message with media/file
                attachments is added to a conversation. The default is ``false``.
            new_message_with_media_template: The template to use to create the notification text displayed when a new
                message with media/file attachments is added to a conversation and ``new_message.attachments.enabled``
                is ``true``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration/Notifications"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            body=form_body(
                [
                    param[bool | None]("LogEnabled", log_enabled),
                    param[bool | None]("NewMessage.Enabled", new_message_enabled),
                    param[str | None]("NewMessage.Template", new_message_template),
                    param[str | None]("NewMessage.Sound", new_message_sound),
                    param[bool | None]("NewMessage.BadgeCountEnabled", new_message_badge_count_enabled),
                    param[bool | None]("AddedToConversation.Enabled", added_to_conversation_enabled),
                    param[str | None]("AddedToConversation.Template", added_to_conversation_template),
                    param[str | None]("AddedToConversation.Sound", added_to_conversation_sound),
                    param[bool | None]("RemovedFromConversation.Enabled", removed_from_conversation_enabled),
                    param[str | None]("RemovedFromConversation.Template", removed_from_conversation_template),
                    param[str | None]("RemovedFromConversation.Sound", removed_from_conversation_sound),
                    param[bool | None]("NewMessage.WithMedia.Enabled", new_message_with_media_enabled),
                    param[str | None]("NewMessage.WithMedia.Template", new_message_with_media_template),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfigurationServiceNotification],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
