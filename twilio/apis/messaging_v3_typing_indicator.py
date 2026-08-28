from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
)
from ..errors.create_v3_typing_indicator_error import (
    CreateV3TypingIndicatorErrorBody,
    create_v3_typing_indicator_error_mapper,
)
from ..models.unions.typing_indicator_request import TypingIndicatorRequest, TypingIndicatorRequestDict
from ..models.v2_indicators_typing_json_response import V2IndicatorsTypingJsonResponse
from ..server.server import Server


class MessagingV3TypingIndicator:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingV3TypingIndicatorWithRawResponse(client, server, auth)

    def create_v3_typing_indicator(
        self,
        body: TypingIndicatorRequest | TypingIndicatorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2IndicatorsTypingJsonResponse:
        """Send a typing indicator to notify the recipient that you are composing a message. Supported channels:
        WhatsApp, Apple Messages for Business. The request body varies by channel — use the ``channel`` field as the
        discriminator.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typing indicator was successfully sent to the recipient.

        Raises:
            ApiError: Invalid request. The request body is missing required fields or contains invalid values.
                Authentication credentials are missing or invalid. The account is not authorized to send typing
                indicators for this channel. ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 |
                RawError``."""
        return self._with_raw_response.create_v3_typing_indicator(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MessagingV3TypingIndicatorWithRawResponse:
        return self._with_raw_response


class AsyncMessagingV3TypingIndicator:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingV3TypingIndicatorWithRawResponse(client, server, auth)

    async def create_v3_typing_indicator(
        self,
        body: TypingIndicatorRequest | TypingIndicatorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2IndicatorsTypingJsonResponse:
        """Send a typing indicator to notify the recipient that you are composing a message. Supported channels:
        WhatsApp, Apple Messages for Business. The request body varies by channel — use the ``channel`` field as the
        discriminator.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typing indicator was successfully sent to the recipient.

        Raises:
            ApiError: Invalid request. The request body is missing required fields or contains invalid values.
                Authentication credentials are missing or invalid. The account is not authorized to send typing
                indicators for this channel. ``error`` is ``AccountsCallsRecordingsSidJson201041408Error1 |
                RawError``."""
        return (
            await self._with_raw_response.create_v3_typing_indicator(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMessagingV3TypingIndicatorWithRawResponse:
        return self._with_raw_response


class MessagingV3TypingIndicatorWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_v3_typing_indicator(
        self,
        body: TypingIndicatorRequest | TypingIndicatorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2IndicatorsTypingJsonResponse, CreateV3TypingIndicatorErrorBody]:
        """Send a typing indicator to notify the recipient that you are composing a message. Supported channels:
        WhatsApp, Apple Messages for Business. The request body varies by channel — use the ``channel`` field as the
        discriminator.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v3/Indicators/Typing.json"),
            body=json_body[TypingIndicatorRequest | TypingIndicatorRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2IndicatorsTypingJsonResponse],
            error_mapper=create_v3_typing_indicator_error_mapper,
            request_options=request_options,
        )


class AsyncMessagingV3TypingIndicatorWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_v3_typing_indicator(
        self,
        body: TypingIndicatorRequest | TypingIndicatorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2IndicatorsTypingJsonResponse, CreateV3TypingIndicatorErrorBody]:
        """Send a typing indicator to notify the recipient that you are composing a message. Supported channels:
        WhatsApp, Apple Messages for Business. The request body varies by channel — use the ``channel`` field as the
        discriminator.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/v3/Indicators/Typing.json"),
            body=json_body[TypingIndicatorRequest | TypingIndicatorRequestDict](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[V2IndicatorsTypingJsonResponse],
            error_mapper=create_v3_typing_indicator_error_mapper,
            request_options=request_options,
        )
