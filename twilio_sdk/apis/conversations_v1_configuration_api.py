from __future__ import annotations

from uuid import UUID, uuid4

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
from ..models.conversations_v1_configuration import ConversationsV1Configuration
from ..models.conversations_v1_service_service_configuration import ConversationsV1ServiceServiceConfiguration
from ..server.server import Server


class ConversationsV1ConfigurationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConversationsV1ConfigurationApiWithRawResponse(client, server, auth)

    def fetch_configuration(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Configuration:
        """Fetch the global configuration of conversations on your account

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_configuration(request_options=request_options).unwrap()

    def fetch_service_configuration(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceConfiguration:
        """Fetch the configuration of a conversation service

        Args:
            chat_service_sid: The SID of the Service configuration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_service_configuration(
            chat_service_sid, request_options=request_options
        ).unwrap()

    def update_configuration(
        self,
        *,
        default_chat_service_sid: str | None = None,
        default_messaging_service_sid: str | None = None,
        default_inactive_timer: str | None = None,
        default_closed_timer: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Configuration:
        """Update the global configuration of conversations on your account

        Args:
            default_chat_service_sid: The SID of the default `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to use when creating a conversation.
            default_messaging_service_sid: The SID of the default `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to use when creating a conversation.
            default_inactive_timer: Default ISO8601 duration when conversation will be switched to ``inactive`` state.
                Minimum value for this timer is 1 minute.
            default_closed_timer: Default ISO8601 duration when conversation will be switched to ``closed`` state.
                Minimum value for this timer is 10 minutes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_configuration(
            default_chat_service_sid=default_chat_service_sid,
            default_messaging_service_sid=default_messaging_service_sid,
            default_inactive_timer=default_inactive_timer,
            default_closed_timer=default_closed_timer,
            request_options=request_options,
        ).unwrap()

    def update_service_configuration(
        self,
        chat_service_sid: str,
        *,
        default_conversation_creator_role_sid: str | None = None,
        default_conversation_role_sid: str | None = None,
        default_chat_service_role_sid: str | None = None,
        reachability_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConfiguration:
        """Update configuration settings of a conversation service

        Args:
            chat_service_sid: The SID of the Service configuration resource to update.
            default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when
                they join a new conversation. See `Conversation Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info about roles.
            default_conversation_role_sid: The conversation-level role assigned to users when they are added to a
                conversation. See `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                for more info about roles.
            default_chat_service_role_sid: The service-level role assigned to users when they are added to the service.
                See `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info
                about roles.
            reachability_enabled: Whether the `Reachability Indicator
                <https://www.twilio.com/docs/conversations/reachability>`__ is enabled for this Conversations Service.
                The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_service_configuration(
            chat_service_sid,
            default_conversation_creator_role_sid=default_conversation_creator_role_sid,
            default_conversation_role_sid=default_conversation_role_sid,
            default_chat_service_role_sid=default_chat_service_role_sid,
            reachability_enabled=reachability_enabled,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConversationsV1ConfigurationApiWithRawResponse:
        return self._with_raw_response


class AsyncConversationsV1ConfigurationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConversationsV1ConfigurationApiWithRawResponse(client, server, auth)

    async def fetch_configuration(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1Configuration:
        """Fetch the global configuration of conversations on your account

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fetch_configuration(request_options=request_options)).unwrap()

    async def fetch_service_configuration(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConversationsV1ServiceServiceConfiguration:
        """Fetch the configuration of a conversation service

        Args:
            chat_service_sid: The SID of the Service configuration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_service_configuration(chat_service_sid, request_options=request_options)
        ).unwrap()

    async def update_configuration(
        self,
        *,
        default_chat_service_sid: str | None = None,
        default_messaging_service_sid: str | None = None,
        default_inactive_timer: str | None = None,
        default_closed_timer: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1Configuration:
        """Update the global configuration of conversations on your account

        Args:
            default_chat_service_sid: The SID of the default `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to use when creating a conversation.
            default_messaging_service_sid: The SID of the default `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to use when creating a conversation.
            default_inactive_timer: Default ISO8601 duration when conversation will be switched to ``inactive`` state.
                Minimum value for this timer is 1 minute.
            default_closed_timer: Default ISO8601 duration when conversation will be switched to ``closed`` state.
                Minimum value for this timer is 10 minutes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_configuration(
                default_chat_service_sid=default_chat_service_sid,
                default_messaging_service_sid=default_messaging_service_sid,
                default_inactive_timer=default_inactive_timer,
                default_closed_timer=default_closed_timer,
                request_options=request_options,
            )
        ).unwrap()

    async def update_service_configuration(
        self,
        chat_service_sid: str,
        *,
        default_conversation_creator_role_sid: str | None = None,
        default_conversation_role_sid: str | None = None,
        default_chat_service_role_sid: str | None = None,
        reachability_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConversationsV1ServiceServiceConfiguration:
        """Update configuration settings of a conversation service

        Args:
            chat_service_sid: The SID of the Service configuration resource to update.
            default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when
                they join a new conversation. See `Conversation Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info about roles.
            default_conversation_role_sid: The conversation-level role assigned to users when they are added to a
                conversation. See `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                for more info about roles.
            default_chat_service_role_sid: The service-level role assigned to users when they are added to the service.
                See `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info
                about roles.
            reachability_enabled: Whether the `Reachability Indicator
                <https://www.twilio.com/docs/conversations/reachability>`__ is enabled for this Conversations Service.
                The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_service_configuration(
                chat_service_sid,
                default_conversation_creator_role_sid=default_conversation_creator_role_sid,
                default_conversation_role_sid=default_conversation_role_sid,
                default_chat_service_role_sid=default_chat_service_role_sid,
                reachability_enabled=reachability_enabled,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConversationsV1ConfigurationApiWithRawResponse:
        return self._with_raw_response


class ConversationsV1ConfigurationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_configuration(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Configuration, RawError]:
        """Fetch the global configuration of conversations on your account

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Configuration"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Configuration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_service_configuration(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceConfiguration, RawError]:
        """Fetch the configuration of a conversation service

        Args:
            chat_service_sid: The SID of the Service configuration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_configuration(
        self,
        *,
        default_chat_service_sid: str | None = None,
        default_messaging_service_sid: str | None = None,
        default_inactive_timer: str | None = None,
        default_closed_timer: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Configuration, RawError]:
        """Update the global configuration of conversations on your account

        Args:
            default_chat_service_sid: The SID of the default `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to use when creating a conversation.
            default_messaging_service_sid: The SID of the default `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to use when creating a conversation.
            default_inactive_timer: Default ISO8601 duration when conversation will be switched to ``inactive`` state.
                Minimum value for this timer is 1 minute.
            default_closed_timer: Default ISO8601 duration when conversation will be switched to ``closed`` state.
                Minimum value for this timer is 10 minutes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Configuration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("DefaultChatServiceSid", default_chat_service_sid),
                    param[str | None]("DefaultMessagingServiceSid", default_messaging_service_sid),
                    param[str | None]("DefaultInactiveTimer", default_inactive_timer),
                    param[str | None]("DefaultClosedTimer", default_closed_timer),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Configuration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_service_configuration(
        self,
        chat_service_sid: str,
        *,
        default_conversation_creator_role_sid: str | None = None,
        default_conversation_role_sid: str | None = None,
        default_chat_service_role_sid: str | None = None,
        reachability_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConfiguration, RawError]:
        """Update configuration settings of a conversation service

        Args:
            chat_service_sid: The SID of the Service configuration resource to update.
            default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when
                they join a new conversation. See `Conversation Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info about roles.
            default_conversation_role_sid: The conversation-level role assigned to users when they are added to a
                conversation. See `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                for more info about roles.
            default_chat_service_role_sid: The service-level role assigned to users when they are added to the service.
                See `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info
                about roles.
            reachability_enabled: Whether the `Reachability Indicator
                <https://www.twilio.com/docs/conversations/reachability>`__ is enabled for this Conversations Service.
                The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("DefaultConversationCreatorRoleSid", default_conversation_creator_role_sid),
                    param[str | None]("DefaultConversationRoleSid", default_conversation_role_sid),
                    param[str | None]("DefaultChatServiceRoleSid", default_chat_service_role_sid),
                    param[bool | None]("ReachabilityEnabled", reachability_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncConversationsV1ConfigurationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_configuration(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1Configuration, RawError]:
        """Fetch the global configuration of conversations on your account

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Configuration"),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Configuration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_service_configuration(
        self, chat_service_sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConversationsV1ServiceServiceConfiguration, RawError]:
        """Fetch the configuration of a conversation service

        Args:
            chat_service_sid: The SID of the Service configuration resource to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_configuration(
        self,
        *,
        default_chat_service_sid: str | None = None,
        default_messaging_service_sid: str | None = None,
        default_inactive_timer: str | None = None,
        default_closed_timer: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1Configuration, RawError]:
        """Update the global configuration of conversations on your account

        Args:
            default_chat_service_sid: The SID of the default `Conversation Service
                <https://www.twilio.com/docs/conversations/api/service-resource>`__ to use when creating a conversation.
            default_messaging_service_sid: The SID of the default `Messaging Service
                <https://www.twilio.com/docs/messaging/api/service-resource>`__ to use when creating a conversation.
            default_inactive_timer: Default ISO8601 duration when conversation will be switched to ``inactive`` state.
                Minimum value for this timer is 1 minute.
            default_closed_timer: Default ISO8601 duration when conversation will be switched to ``closed`` state.
                Minimum value for this timer is 10 minutes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Configuration"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("DefaultChatServiceSid", default_chat_service_sid),
                    param[str | None]("DefaultMessagingServiceSid", default_messaging_service_sid),
                    param[str | None]("DefaultInactiveTimer", default_inactive_timer),
                    param[str | None]("DefaultClosedTimer", default_closed_timer),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1Configuration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_service_configuration(
        self,
        chat_service_sid: str,
        *,
        default_conversation_creator_role_sid: str | None = None,
        default_conversation_role_sid: str | None = None,
        default_chat_service_role_sid: str | None = None,
        reachability_enabled: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConversationsV1ServiceServiceConfiguration, RawError]:
        """Update configuration settings of a conversation service

        Args:
            chat_service_sid: The SID of the Service configuration resource to update.
            default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when
                they join a new conversation. See `Conversation Role
                <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info about roles.
            default_conversation_role_sid: The conversation-level role assigned to users when they are added to a
                conversation. See `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__
                for more info about roles.
            default_chat_service_role_sid: The service-level role assigned to users when they are added to the service.
                See `Conversation Role <https://www.twilio.com/docs/conversations/api/role-resource>`__ for more info
                about roles.
            reachability_enabled: Whether the `Reachability Indicator
                <https://www.twilio.com/docs/conversations/reachability>`__ is enabled for this Conversations Service.
                The default is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default7("/v1/Services/{ChatServiceSid}/Configuration"),
            path_params=[param[str]("ChatServiceSid", chat_service_sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str | None]("DefaultConversationCreatorRoleSid", default_conversation_creator_role_sid),
                    param[str | None]("DefaultConversationRoleSid", default_conversation_role_sid),
                    param[str | None]("DefaultChatServiceRoleSid", default_chat_service_role_sid),
                    param[bool | None]("ReachabilityEnabled", reachability_enabled),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ConversationsV1ServiceServiceConfiguration],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
