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
from ..models.flex_v2_web_channel import FlexV2WebChannel
from ..server.server import Server


class FlexV2WebChannels:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV2WebChannelsWithRawResponse(client, server, auth)

    def create_web_channel2(
        self,
        address_sid: str,
        *,
        ui_version: str | None = None,
        chat_friendly_name: str | None = None,
        customer_friendly_name: str | None = None,
        pre_engagement_data: str | None = None,
        identity: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV2WebChannel:
        """Send a ``POST`` request.

        Args:
            address_sid: The SID of the Conversations Address. See `Address Configuration Resource
                <https://www.twilio.com/docs/conversations/api/address-configuration-resource>`__ for configuration
                details. When a conversation is created on the Flex backend, the callback URL will be set to the
                corresponding Studio Flow SID or webhook URL in your address configuration.
            ui_version: The Ui-Version HTTP request header
            chat_friendly_name: The Conversation's friendly name. See the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for an example.
            customer_friendly_name: The Conversation participant's friendly name. See the `Conversation Participant
                Resource <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__ for an
                example.
            pre_engagement_data: The pre-engagement data.
            identity: The Identity of the guest user. See the `Conversation User Resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__ for an example.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_web_channel2(
            address_sid,
            ui_version=ui_version,
            chat_friendly_name=chat_friendly_name,
            customer_friendly_name=customer_friendly_name,
            pre_engagement_data=pre_engagement_data,
            identity=identity,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV2WebChannelsWithRawResponse:
        return self._with_raw_response


class AsyncFlexV2WebChannels:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV2WebChannelsWithRawResponse(client, server, auth)

    async def create_web_channel2(
        self,
        address_sid: str,
        *,
        ui_version: str | None = None,
        chat_friendly_name: str | None = None,
        customer_friendly_name: str | None = None,
        pre_engagement_data: str | None = None,
        identity: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV2WebChannel:
        """Send a ``POST`` request.

        Args:
            address_sid: The SID of the Conversations Address. See `Address Configuration Resource
                <https://www.twilio.com/docs/conversations/api/address-configuration-resource>`__ for configuration
                details. When a conversation is created on the Flex backend, the callback URL will be set to the
                corresponding Studio Flow SID or webhook URL in your address configuration.
            ui_version: The Ui-Version HTTP request header
            chat_friendly_name: The Conversation's friendly name. See the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for an example.
            customer_friendly_name: The Conversation participant's friendly name. See the `Conversation Participant
                Resource <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__ for an
                example.
            pre_engagement_data: The pre-engagement data.
            identity: The Identity of the guest user. See the `Conversation User Resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__ for an example.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_web_channel2(
                address_sid,
                ui_version=ui_version,
                chat_friendly_name=chat_friendly_name,
                customer_friendly_name=customer_friendly_name,
                pre_engagement_data=pre_engagement_data,
                identity=identity,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV2WebChannelsWithRawResponse:
        return self._with_raw_response


class FlexV2WebChannelsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_web_channel2(
        self,
        address_sid: str,
        *,
        ui_version: str | None = None,
        chat_friendly_name: str | None = None,
        customer_friendly_name: str | None = None,
        pre_engagement_data: str | None = None,
        identity: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV2WebChannel, RawError]:
        """Send a ``POST`` request.

        Args:
            address_sid: The SID of the Conversations Address. See `Address Configuration Resource
                <https://www.twilio.com/docs/conversations/api/address-configuration-resource>`__ for configuration
                details. When a conversation is created on the Flex backend, the callback URL will be set to the
                corresponding Studio Flow SID or webhook URL in your address configuration.
            ui_version: The Ui-Version HTTP request header
            chat_friendly_name: The Conversation's friendly name. See the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for an example.
            customer_friendly_name: The Conversation participant's friendly name. See the `Conversation Participant
                Resource <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__ for an
                example.
            pre_engagement_data: The pre-engagement data.
            identity: The Identity of the guest user. See the `Conversation User Resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__ for an example.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v2/WebChats"),
            headers=[param[str | None]("Ui-Version", ui_version), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("AddressSid", address_sid),
                    param[str | None]("ChatFriendlyName", chat_friendly_name),
                    param[str | None]("CustomerFriendlyName", customer_friendly_name),
                    param[str | None]("PreEngagementData", pre_engagement_data),
                    param[str | None]("Identity", identity),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV2WebChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV2WebChannelsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_web_channel2(
        self,
        address_sid: str,
        *,
        ui_version: str | None = None,
        chat_friendly_name: str | None = None,
        customer_friendly_name: str | None = None,
        pre_engagement_data: str | None = None,
        identity: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV2WebChannel, RawError]:
        """Send a ``POST`` request.

        Args:
            address_sid: The SID of the Conversations Address. See `Address Configuration Resource
                <https://www.twilio.com/docs/conversations/api/address-configuration-resource>`__ for configuration
                details. When a conversation is created on the Flex backend, the callback URL will be set to the
                corresponding Studio Flow SID or webhook URL in your address configuration.
            ui_version: The Ui-Version HTTP request header
            chat_friendly_name: The Conversation's friendly name. See the `Conversation resource
                <https://www.twilio.com/docs/conversations/api/conversation-resource>`__ for an example.
            customer_friendly_name: The Conversation participant's friendly name. See the `Conversation Participant
                Resource <https://www.twilio.com/docs/conversations/api/conversation-participant-resource>`__ for an
                example.
            pre_engagement_data: The pre-engagement data.
            identity: The Identity of the guest user. See the `Conversation User Resource
                <https://www.twilio.com/docs/conversations/api/user-resource>`__ for an example.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v2/WebChats"),
            headers=[param[str | None]("Ui-Version", ui_version), param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[str]("AddressSid", address_sid),
                    param[str | None]("ChatFriendlyName", chat_friendly_name),
                    param[str | None]("CustomerFriendlyName", customer_friendly_name),
                    param[str | None]("PreEngagementData", pre_engagement_data),
                    param[str | None]("Identity", identity),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV2WebChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
