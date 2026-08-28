from __future__ import annotations

from typing import Any

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.flex_v1_interaction_interaction_channel_interaction_transfer import (
    FlexV1InteractionInteractionChannelInteractionTransfer,
)
from ..server.server import Server


class FlexV1InteractionTransfer:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InteractionTransferWithRawResponse(client, server, auth)

    def create_interaction_transfer(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionTransfer:
        """Create a new Transfer.

        Args:
            interaction_sid: The Interaction Sid for the Interaction
            channel_sid: The Channel Sid for the Channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_interaction_transfer(
            interaction_sid, channel_sid, body=body, request_options=request_options
        ).unwrap()

    def fetch_interaction_transfer(
        self, interaction_sid: str, channel_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InteractionInteractionChannelInteractionTransfer:
        """Fetch a specific Transfer by SID.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Transfer.
            sid: The unique string created by Twilio to identify a Transfer resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_interaction_transfer(
            interaction_sid, channel_sid, sid, request_options=request_options
        ).unwrap()

    def update_interaction_transfer(
        self,
        interaction_sid: str,
        channel_sid: str,
        sid: str,
        *,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionTransfer:
        """Update an existing Transfer.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Transfer.
            sid: The unique string created by Twilio to identify a Transfer resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_interaction_transfer(
            interaction_sid, channel_sid, sid, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InteractionTransferWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InteractionTransfer:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InteractionTransferWithRawResponse(client, server, auth)

    async def create_interaction_transfer(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionTransfer:
        """Create a new Transfer.

        Args:
            interaction_sid: The Interaction Sid for the Interaction
            channel_sid: The Channel Sid for the Channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_interaction_transfer(
                interaction_sid, channel_sid, body=body, request_options=request_options
            )
        ).unwrap()

    async def fetch_interaction_transfer(
        self, interaction_sid: str, channel_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InteractionInteractionChannelInteractionTransfer:
        """Fetch a specific Transfer by SID.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Transfer.
            sid: The unique string created by Twilio to identify a Transfer resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_interaction_transfer(
                interaction_sid, channel_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def update_interaction_transfer(
        self,
        interaction_sid: str,
        channel_sid: str,
        sid: str,
        *,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannelInteractionTransfer:
        """Update an existing Transfer.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Transfer.
            sid: The unique string created by Twilio to identify a Transfer resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_interaction_transfer(
                interaction_sid, channel_sid, sid, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InteractionTransferWithRawResponse:
        return self._with_raw_response


class FlexV1InteractionTransferWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_interaction_transfer(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]:
        """Create a new Transfer.

        Args:
            interaction_sid: The Interaction Sid for the Interaction
            channel_sid: The Channel Sid for the Channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionTransfer],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fetch_interaction_transfer(
        self, interaction_sid: str, channel_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]:
        """Fetch a specific Transfer by SID.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Transfer.
            sid: The unique string created by Twilio to identify a Transfer resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13(
                "/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers/{Sid}"
            ),
            path_params=[
                param[str]("InteractionSid", interaction_sid),
                param[str]("ChannelSid", channel_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionTransfer],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_interaction_transfer(
        self,
        interaction_sid: str,
        channel_sid: str,
        sid: str,
        *,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]:
        """Update an existing Transfer.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Transfer.
            sid: The unique string created by Twilio to identify a Transfer resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13(
                "/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers/{Sid}"
            ),
            path_params=[
                param[str]("InteractionSid", interaction_sid),
                param[str]("ChannelSid", channel_sid),
                param[str]("Sid", sid),
            ],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionTransfer],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InteractionTransferWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_interaction_transfer(
        self,
        interaction_sid: str,
        channel_sid: str,
        *,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]:
        """Create a new Transfer.

        Args:
            interaction_sid: The Interaction Sid for the Interaction
            channel_sid: The Channel Sid for the Channel.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("ChannelSid", channel_sid)],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionTransfer],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fetch_interaction_transfer(
        self, interaction_sid: str, channel_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]:
        """Fetch a specific Transfer by SID.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Transfer.
            sid: The unique string created by Twilio to identify a Transfer resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13(
                "/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers/{Sid}"
            ),
            path_params=[
                param[str]("InteractionSid", interaction_sid),
                param[str]("ChannelSid", channel_sid),
                param[str]("Sid", sid),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionTransfer],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_interaction_transfer(
        self,
        interaction_sid: str,
        channel_sid: str,
        sid: str,
        *,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannelInteractionTransfer, RawError]:
        """Update an existing Transfer.

        Args:
            interaction_sid: The Interaction Sid for this channel.
            channel_sid: The Channel Sid for this Transfer.
            sid: The unique string created by Twilio to identify a Transfer resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13(
                "/v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Transfers/{Sid}"
            ),
            path_params=[
                param[str]("InteractionSid", interaction_sid),
                param[str]("ChannelSid", channel_sid),
                param[str]("Sid", sid),
            ],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannelInteractionTransfer],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
