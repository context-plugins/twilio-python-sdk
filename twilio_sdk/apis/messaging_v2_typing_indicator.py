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
from ..models.enums.channel import ChannelOrStr
from ..models.v2_indicators_typing_json_response import V2IndicatorsTypingJsonResponse
from ..server.server import Server


class MessagingV2TypingIndicator:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV2TypingIndicatorWithRawResponse(client, server, auth)

    def create_typing_indicator(
        self, channel: ChannelOrStr, message_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2IndicatorsTypingJsonResponse:
        """Send a typing indicator to notify the recipient that you are composing a message. Currently supported for
        whatsapp channel only. For WhatsApp, ``messageId`` is required.

        Args:
            channel: Shared channel identifier
            message_id: Message SID that identifies the conversation thread for the typing indicator. Must be a valid
                Twilio Message SID (SM*) or Media SID (MM*) from an existing WhatsApp conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typing indicator was successfully sent to the recipient.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_typing_indicator(
            channel, message_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MessagingV2TypingIndicatorWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV2TypingIndicator:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV2TypingIndicatorWithRawResponse(client, server, auth)

    async def create_typing_indicator(
        self, channel: ChannelOrStr, message_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2IndicatorsTypingJsonResponse:
        """Send a typing indicator to notify the recipient that you are composing a message. Currently supported for
        whatsapp channel only. For WhatsApp, ``messageId`` is required.

        Args:
            channel: Shared channel identifier
            message_id: Message SID that identifies the conversation thread for the typing indicator. Must be a valid
                Twilio Message SID (SM*) or Media SID (MM*) from an existing WhatsApp conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typing indicator was successfully sent to the recipient.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_typing_indicator(channel, message_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV2TypingIndicatorWithRawResponse:
        return self._with_raw_response


class MessagingV2TypingIndicatorWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_typing_indicator(
        self, channel: ChannelOrStr, message_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2IndicatorsTypingJsonResponse, RawError]:
        """Send a typing indicator to notify the recipient that you are composing a message. Currently supported for
        whatsapp channel only. For WhatsApp, ``messageId`` is required.

        Args:
            channel: Shared channel identifier
            message_id: Message SID that identifies the conversation thread for the typing indicator. Must be a valid
                Twilio Message SID (SM*) or Media SID (MM*) from an existing WhatsApp conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v2/Indicators/Typing.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[ChannelOrStr]("channel", channel), param[str]("messageId", message_id)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2IndicatorsTypingJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMessagingV2TypingIndicatorWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_typing_indicator(
        self, channel: ChannelOrStr, message_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2IndicatorsTypingJsonResponse, RawError]:
        """Send a typing indicator to notify the recipient that you are composing a message. Currently supported for
        whatsapp channel only. For WhatsApp, ``messageId`` is required.

        Args:
            channel: Shared channel identifier
            message_id: Message SID that identifies the conversation thread for the typing indicator. Must be a valid
                Twilio Message SID (SM*) or Media SID (MM*) from an existing WhatsApp conversation.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v2/Indicators/Typing.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body([param[ChannelOrStr]("channel", channel), param[str]("messageId", message_id)]),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2IndicatorsTypingJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
