from __future__ import annotations

from typing import Any
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
from ..models.enums.interaction_channel_enum_update_channel_status import InteractionChannelEnumUpdateChannelStatusOrStr
from ..models.flex_v1_interaction_interaction_channel import FlexV1InteractionInteractionChannel
from ..models.list_interaction_channel_response import ListInteractionChannelResponse
from ..server.server import Server


class FlexV1InteractionChannel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FlexV1InteractionChannelWithRawResponse(client, server, auth)

    def fetch_interaction_channel(
        self, interaction_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InteractionInteractionChannel:
        """Fetch a Channel for an Interaction.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fetch_interaction_channel(
            interaction_sid, sid, request_options=request_options
        ).unwrap()

    def list_interaction_channel(
        self,
        interaction_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInteractionChannelResponse:
        """List all Channels for an Interaction.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_interaction_channel(
            interaction_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        ).unwrap()

    def update_interaction_channel(
        self,
        interaction_sid: str,
        sid: str,
        status: InteractionChannelEnumUpdateChannelStatusOrStr,
        *,
        routing: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannel:
        """Update an existing Interaction Channel.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
            status: Value sent with the request.
            routing: It changes the state of associated tasks. Routing status is required, When the channel status is
                set to ``inactive``. Allowed Value for routing status is ``closed``. Otherwise Optional, if not
                specified, all tasks will be set to ``wrapping``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_interaction_channel(
            interaction_sid, sid, status, routing=routing, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FlexV1InteractionChannelWithRawResponse:
        return self._with_raw_response


class AsyncFlexV1InteractionChannel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFlexV1InteractionChannelWithRawResponse(client, server, auth)

    async def fetch_interaction_channel(
        self, interaction_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FlexV1InteractionInteractionChannel:
        """Fetch a Channel for an Interaction.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fetch_interaction_channel(
                interaction_sid, sid, request_options=request_options
            )
        ).unwrap()

    async def list_interaction_channel(
        self,
        interaction_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInteractionChannelResponse:
        """List all Channels for an Interaction.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_interaction_channel(
                interaction_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
            )
        ).unwrap()

    async def update_interaction_channel(
        self,
        interaction_sid: str,
        sid: str,
        status: InteractionChannelEnumUpdateChannelStatusOrStr,
        *,
        routing: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FlexV1InteractionInteractionChannel:
        """Update an existing Interaction Channel.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
            status: Value sent with the request.
            routing: It changes the state of associated tasks. Routing status is required, When the channel status is
                set to ``inactive``. Allowed Value for routing status is ``closed``. Otherwise Optional, if not
                specified, all tasks will be set to ``wrapping``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_interaction_channel(
                interaction_sid, sid, status, routing=routing, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFlexV1InteractionChannelWithRawResponse:
        return self._with_raw_response


class FlexV1InteractionChannelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch_interaction_channel(
        self, interaction_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InteractionInteractionChannel, RawError]:
        """Fetch a Channel for an Interaction.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{Sid}"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_interaction_channel(
        self,
        interaction_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInteractionChannelResponse, RawError]:
        """List all Channels for an Interaction.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels"),
            path_params=[param[str]("InteractionSid", interaction_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInteractionChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_interaction_channel(
        self,
        interaction_sid: str,
        sid: str,
        status: InteractionChannelEnumUpdateChannelStatusOrStr,
        *,
        routing: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannel, RawError]:
        """Update an existing Interaction Channel.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
            status: Value sent with the request.
            routing: It changes the state of associated tasks. Routing status is required, When the channel status is
                set to ``inactive``. Allowed Value for routing status is ``closed``. Otherwise Optional, if not
                specified, all tasks will be set to ``wrapping``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{Sid}"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[InteractionChannelEnumUpdateChannelStatusOrStr]("Status", status),
                    param[Any | None]("Routing", routing),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFlexV1InteractionChannelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch_interaction_channel(
        self, interaction_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FlexV1InteractionInteractionChannel, RawError]:
        """Fetch a Channel for an Interaction.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{Sid}"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("Sid", sid)],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_interaction_channel(
        self,
        interaction_sid: str,
        *,
        page_size: int | None = None,
        page: int | None = None,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInteractionChannelResponse, RawError]:
        """List all Channels for an Interaction.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
            page: The page index. This value is simply for client state.
            page_token: The page token. This is provided by the API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels"),
            path_params=[param[str]("InteractionSid", interaction_sid)],
            query_params=[
                param[int | None]("PageSize", page_size),
                param[int | None]("Page", page),
                param[str | None]("PageToken", page_token),
            ],
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[ListInteractionChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_interaction_channel(
        self,
        interaction_sid: str,
        sid: str,
        status: InteractionChannelEnumUpdateChannelStatusOrStr,
        *,
        routing: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FlexV1InteractionInteractionChannel, RawError]:
        """Update an existing Interaction Channel.

        Args:
            interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
            sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
            status: Value sent with the request.
            routing: It changes the state of associated tasks. Routing status is required, When the channel status is
                set to ``inactive``. Allowed Value for routing status is ``closed``. Otherwise Optional, if not
                specified, all tasks will be set to ``wrapping``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/v1/Interactions/{InteractionSid}/Channels/{Sid}"),
            path_params=[param[str]("InteractionSid", interaction_sid), param[str]("Sid", sid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                [
                    param[InteractionChannelEnumUpdateChannelStatusOrStr]("Status", status),
                    param[Any | None]("Routing", routing),
                ],
            ),
            auth_scheme=self._auth.account_sid_auth_token,
            decoder=json_decoder[FlexV1InteractionInteractionChannel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
